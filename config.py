import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_API_TOKEN')
# Токен бота от @BotFather
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

# URL API для курсов валют
CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
