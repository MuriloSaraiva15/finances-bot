from telegram.ext import Updater, CommandHandler
import requests
import re


bot_token = "8278123611:AAH7P9WBQHoF5AsYFNNGaN6Xf1625JkBZHg"
telegramUrl = "https://api.telegram.org/bot" + bot_token
webAppUrl = "https://script.google.com/macros/s/AKfycbwv05rchOoFj1eHhQx93HUd_mxKplMrSheYIMaEWj2D1v394EuJBaYauARtSiCkJuhLow/exec"


# Criando webhook

def setWebhookUrl():
    webhookUrl = telegramUrl+"/setWebhook?url="+webAppUrl
    print(webhookUrl)


def bop)