from flask import Flask, request
import bot

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.bot.process_new_updates([update])
    return "ok", 200