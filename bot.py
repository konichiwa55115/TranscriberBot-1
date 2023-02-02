import os
import telebot

BOT_TOKEN = os.getenv('BOT_TOKEN')

#initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

#welcome message
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")