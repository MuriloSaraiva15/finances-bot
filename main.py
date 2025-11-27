from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram import Message, Update
import requests
import json

bot_token = "8278123611:AAH7P9WBQHoF5AsYFNNGaN6Xf1625JkBZHg"
telegramUrl = "https://api.telegram.org/bot" + bot_token
webAppUrl = "https://script.google.com/macros/s/AKfycbwv05rchOoFj1eHhQx93HUd_mxKplMrSheYIMaEWj2D1v394EuJBaYauARtSiCkJuhLow/exec"


# Criando webhook

def setWebhookUrl():
    webhookUrl = telegramUrl+"/setWebhook?url="+webAppUrl
    print(webhookUrl)

# Configurando start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Eu sou seu bot de finanças. Use /ajuda para ver os comandos disponíveis.')

start_handler = CommandHandler('start', start)

def main():
    application = Application.builder().token(bot_token).build()
    application.add_handler(start_handler)

