from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram import Message, Update
import requests
import json

bot_token = "8278123611:AAH7P9WBQHoF5AsYFNNGaN6Xf1625JkBZHg"
telegramUrl = f"https://api.telegram.org/bot{bot_token}"
webAppUrl = "https://script.google.com/macros/s/AKfycbw7RWRfqEOqqadSAZJBPnWWkOIBHwDx883OyLb46u8u-fOR9Q1i_-UiKKQ6UT3Era1LZw/exec"


# Criando webhook
def set_webhook():
    url =  f"{telegramUrl}/setWebhook?url={webAppUrl}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    resultado = set_webhook()
    print(resultado)





