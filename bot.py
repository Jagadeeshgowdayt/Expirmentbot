import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

# Configure logging
tlogging = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Read token and channels
token = os.getenv('BOT_TOKEN')
channels = os.getenv('CHANNEL_IDS', '').split()

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    for chat_id in channels:
        try:
            await context.bot.send_message(chat_id=chat_id, text=text)
        except Exception as e:
            logging.error(f"Failed to send to {chat_id}: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    # Listen to direct messages only
    app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT, broadcast))
    app.run_polling()
