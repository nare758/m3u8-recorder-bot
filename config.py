import os
import sys
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import MemorySession

load_dotenv()

try:
    API_ID = int(os.environ.get("30523194"))
    API_HASH = os.environ.get("76d62e302ed767a9ea0b8586a9189ca5")
    BOT_TOKEN = os.environ.get("8531617857:AAEutx4YBcpBzJN-hxmfEz1-bQezohbGlI0")
except (TypeError, ValueError):
    print("ERROR: Missing API credentials in .env file")
    sys.exit(1)

RECORDING_PATH = "[use your own path]"

def initialize_client():
    print("Connecting to Telegram...")
    client = TelegramClient(
        MemorySession(),
        API_ID,
        API_HASH,
        flood_sleep_threshold=24 * 60 * 60,
        connection_retries=5,
        retry_delay=1
    )

    try:
        client.start(bot_token=BOT_TOKEN)
        print("Bot connected successfully")
        return client
    except Exception as e:
        print(f"Connection failed: {e}")
        sys.exit(1)

app = initialize_client()
