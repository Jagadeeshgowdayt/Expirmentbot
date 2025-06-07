from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace this with your actual token
TOKEN = "7583784576:AAFVZaHyv6JGUDXTFJ3XYaQ03WRCZQolTEk"

# Define a basic /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Hello! Your bot is running successfully on Koyeb!")

# Define your main application
def main():
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    # Start polling
    app.run_polling()

# Run the bot
if __name__ == "__main__":
    main()
    
