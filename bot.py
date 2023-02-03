import os
from background import keep_alive
import telebot

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

#Greeting message
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Hello':
        bot.reply_to(message, 'Hello! How can I help you today?')


#Server
keep_alive() 
bot.polling(non_stop=True, interval=0)