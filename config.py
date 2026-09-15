import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

DATABASE_URI = os.getenv("DATABASE_URI", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "autofilter")

ADMINS = [int(x.strip()) for x in os.getenv("ADMINS", "").split(",") if x.strip()]

BIN_CHANNEL = int(os.getenv("BIN_CHANNEL", "0"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))

AUTO_FFILTER = os.getenv("AUTO_FFILTER", "True").lower() == "true"
SPELL_CHECK_REPLY = os.getenv("SPELL_CHECK_REPLY", "True").lower() == "true"
BUTTON_MODE = os.getenv("BUTTON_MODE", "True").lower() == "true"

SHORTENER_API = os.getenv("SHORTENER_API", "")
SHORTENER_WEBSITE = os.getenv("SHORTENER_WEBSITE", "gplinks.com")
IS_VERIFY = os.getenv("IS_VERIFY", "True").lower() == "true"
