import asyncio
from aiohttp import web
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7583784576:AAFVZaHyv6JGUDXTFJ3XYaQ03WRCZQolTEk"
CHANNEL_IDS = ["-1002822240154"]  # Add more channel IDs here as strings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Broadcasting your message...")
    text = update.message.text.replace('/start', '').strip()
    for channel in CHANNEL_IDS:
        await context.bot.send_message(chat_id=channel, text=text or "Hello from bot!")

# Dummy HTTP server for Koyeb
async def health_check(request):
    return web.Response(text="OK")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    asyncio.create_task(app.run_polling())

    # Start the dummy HTTP server
    server = web.Application()
    server.router.add_get("/", health_check)
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    print("Bot and HTTP server running...")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
