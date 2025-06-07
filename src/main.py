import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# ─── CONFIG ──────────────────────────────────────────────────────────────────────
BOT_TOKEN    = "7583784576:AAFVZaHyv6JGUDXTFJ3XYaQ03WRCZQolTEk"
CHANNEL_IDS  = ["-1002822240154"]  # add more channel IDs here as strings
# ─────────────────────────────────────────────────────────────────────────────────

# set up basic logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def broadcast_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Receive any text message and forward it to all channels."""
    text = update.effective_message.text
    if not text:
        return  # ignore non-text

    for chat_id in CHANNEL_IDS:
        try:
            await context.bot.send_message(chat_id=chat_id, text=text)
        except Exception as e:
            logger.error(f"Failed to send to {chat_id}: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Catch every text message (you could restrict to private chats if you like)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, broadcast_handler))

    # Run the bot (long-polling). For webhooks, swap this for webhook setup below.
    app.run_polling()
  
