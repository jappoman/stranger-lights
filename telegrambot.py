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


# Function to run the Telegram bot
def run_telegram_bot():
    config = load_config()
    TOKEN = config["BOT_CONFIG"]["TOKEN"]

    # Create the bot application
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("config", config_menu))
    app.add_handler(CallbackQueryHandler(handle_callback))

    # Run the bot application
    print("Telegram bot is running...")
    app.run_polling()
