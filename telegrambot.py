import json
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Function to load configuration dynamically
def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

# Function to save configuration
def save_config(new_config):
    with open("config.json", "w") as config_file:
        json.dump(new_config, config_file, indent=2)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Use /config to manage the system configuration.")

# Display configuration options
async def config_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Edit USE_MOCK", callback_data="edit_USE_MOCK")],
        [InlineKeyboardButton("Edit ROUTINE", callback_data="edit_ROUTINE")],
        [InlineKeyboardButton("Edit STRANGER_CONFIG", callback_data="edit_STRANGER_CONFIG")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose what to edit:", reply_markup=reply_markup)

# Handle inline keyboard interactions
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    config = load_config()

    if query.data == "edit_USE_MOCK":
        keyboard = [
            [InlineKeyboardButton("True", callback_data="set_USE_MOCK:True")],
            [InlineKeyboardButton("False", callback_data="set_USE_MOCK:False")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Choose the new value for USE_MOCK:", reply_markup=reply_markup)
    elif query.data == "edit_ROUTINE":
        routines = [routine["name"] for routine in config.get("ROUTINE_LIST", [])]
        keyboard = [
            [InlineKeyboardButton(routine, callback_data=f"set_ROUTINE:{routine}")]
            for routine in routines
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Choose the new ROUTINE:", reply_markup=reply_markup)
    elif query.data == "edit_STRANGER_CONFIG":
        # Show options for STRANGER_CONFIG
        keyboard = [
            [InlineKeyboardButton("Edit LETTER_POSITIONS", callback_data="edit_LETTER_POSITIONS")],
            [InlineKeyboardButton("Edit WORD_LIST", callback_data="edit_WORD_LIST")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Choose what to edit in STRANGER_CONFIG:", reply_markup=reply_markup)
    elif query.data == "edit_LETTER_POSITIONS":
        await query.edit_message_text(
            "Send the new LETTER_POSITIONS in this format:\nA:1,2,3;B:4,5,6;C:7,8,9"
        )
        context.user_data["awaiting_input"] = "LETTER_POSITIONS"
    elif query.data == "edit_WORD_LIST":
        await query.edit_message_text(
            "Send the new WORD_LIST in this format:\nword1 word2;word3 word4"
        )
        context.user_data["awaiting_input"] = "WORD_LIST"
    elif query.data.startswith("set_USE_MOCK"):
        try:
            new_value = query.data.split(":")[1].lower() == "true"
            config["USE_MOCK"] = new_value
            save_config(config)
            await query.edit_message_text(f"USE_MOCK updated to {new_value}")
        except Exception as e:
            await query.edit_message_text(f"Error during update: {e}")
    elif query.data.startswith("set_ROUTINE"):
        try:
            new_value = query.data.split(":")[1]
            config["ROUTINE"] = new_value
            save_config(config)
            await query.edit_message_text(f"ROUTINE updated to {new_value}")
        except Exception as e:
            await query.edit_message_text(f"Error during update: {e}")

# Handle user input for specific configurations
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config = load_config()
    awaiting_input = context.user_data.get("awaiting_input")

    if awaiting_input == "LETTER_POSITIONS":
        try:
            # Parse user input and convert letters to uppercase
            letters = update.message.text.split(";")
            updated_positions = {
                letter.split(":")[0].strip().upper(): [int(n) for n in letter.split(":")[1].split(",")]
                for letter in letters
            }

            # Update only the specified letters
            config["STRANGER_CONFIG"]["LETTER_POSITIONS"].update(updated_positions)
            save_config(config)
            await update.message.reply_text("LETTER_POSITIONS updated successfully!")
        except Exception as e:
            await update.message.reply_text(f"Error in formatting: {e}")

    elif awaiting_input == "WORD_LIST":
        try:
            # Parse and replace the WORD_LIST
            words = [line.strip() for line in update.message.text.split(";")]
            config["STRANGER_CONFIG"]["WORD_LIST"] = words
            save_config(config)
            await update.message.reply_text("WORD_LIST updated successfully!")
        except Exception as e:
            await update.message.reply_text(f"Error in formatting: {e}")

    # Clear awaiting_input
    context.user_data["awaiting_input"] = None

# Handle errors globally
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Errore: {context.error}")
    if isinstance(update, Update):
        await update.message.reply_text("An error occurred. Please try again.")

# Function to run the Telegram bot
def run_telegram_bot():
    config = load_config()
    TOKEN = config["BOT_CONFIG"]["TOKEN"]

    # Creazione del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Aggiungi handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("config", config_menu))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_error_handler(error_handler)

    async def run():
        await app.run_polling()

    # Creazione di un event loop personalizzato per il thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(run())
    except Exception as e:
        print(f"Errore durante l'esecuzione del bot: {e}")
    finally:
        loop.close()
