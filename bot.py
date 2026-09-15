from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise RuntimeError("API_ID, API_HASH and BOT_TOKEN must be configured.")

app = Client(
    "autofilter_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Welcome!\n\n"
        "Send a movie or episode name to search."
    )

@app.on_message(filters.text & ~filters.command("start"))
async def search(client, message):
    query = message.text.strip()
    await message.reply_text(
        f"🔎 Searching for:\n\n{query}\n\n"
        "AutoFilter foundation is running."
    )

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
