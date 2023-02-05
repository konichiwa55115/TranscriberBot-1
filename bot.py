import os
from background import keep_alive
import telebot

BOT_TOKEN = "6089522865:AAG0vUsYSBg-BaSfiG1T5E1QTrorjoMDA4U"

bot = telebot.TeleBot(BOT_TOKEN)

#Greeting message
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, """
    Welcome to Telu Bot! I'm here to help you get a written transcript of your audio or video files. Simply send me the file and choose either .srt or .txt format for the output. I'll take care of the rest! Let's get started.
    """)


#Server
keep_alive() 
bot.polling(non_stop=True, interval=0)
