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
        [InlineKeyboardButton("Show Full Configuration", callback_data="show_config")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose what to edit:", reply_markup=reply_markup)

# Handle inline keyboard interactions
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    config = load_config()

    if query.data == "show_config":
        await query.edit_message_text(f"Configurazione attuale:\n{json.dumps(config, indent=2)}")
    elif query.data == "edit_USE_MOCK":
        keyboard = [
            [InlineKeyboardButton("True", callback_data="set_USE_MOCK:True")],
            [InlineKeyboardButton("False", callback_data="set_USE_MOCK:False")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Scegli il valore per USE_MOCK:", reply_markup=reply_markup)
    elif query.data == "edit_ROUTINE":
        routines = ["test_routine", "portal_routine", "stranger_routine", "christmas_routine"]
        keyboard = [
            [InlineKeyboardButton(routine, callback_data=f"set_ROUTINE:{routine}")]
            for routine in routines
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Scegli la nuova ROUTINE:", reply_markup=reply_markup)
    elif query.data.startswith("set_USE_MOCK"):
        try:
            new_value = query.data.split(":")[1].lower() == "true"
            config["USE_MOCK"] = new_value
            save_config(config)
            await query.edit_message_text(f"USE_MOCK aggiornato a {new_value}")
        except Exception as e:
            await query.edit_message_text(f"Errore durante l'aggiornamento: {e}")
    elif query.data.startswith("set_ROUTINE"):
        try:
            new_value = query.data.split(":")[1]
            config["ROUTINE"] = new_value
            save_config(config)
            await query.edit_message_text(f"ROUTINE aggiornata a {new_value}")
        except Exception as e:
            await query.edit_message_text(f"Errore durante l'aggiornamento: {e}")

# Handle user input for specific configurations
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config = load_config()
    awaiting_input = context.user_data.get("awaiting_input")

    if awaiting_input == "LETTER_POSITIONS":
        try:
            letters = update.message.text.split(";")
            letter_positions = {
                letter.split(":")[0].strip(): [int(n) for n in letter.split(":")[1].split(",")]
                for letter in letters
            }
            config["STRANGER_CONFIG"]["LETTER_POSITIONS"] = letter_positions
            save_config(config)
            await update.message.reply_text("LETTER_POSITIONS updated successfully!")
        except Exception as e:
            await update.message.reply_text(f"Error in formatting: {e}")
    elif awaiting_input == "WORD_LIST":
        try:
            words = [line.strip() for line in update.message.text.split(";")]
            config["STRANGER_CONFIG"]["WORD_LIST"] = words
            save_config(config)
            await update.message.reply_text("WORD_LIST updated successfully!")
        except Exception as e:
            await update.message.reply_text(f"Error in formatting: {e}")

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

    # Creazione di un event loop personalizzato per il thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Esegui il polling all'interno del nuovo loop
    loop.run_until_complete(app.run_polling())

