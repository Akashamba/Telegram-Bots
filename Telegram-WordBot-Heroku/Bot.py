import os
from flask import Flask, request
import telebot
import back

TOKEN = '936679736:AAGsqLr6fuBk0BfRTGCixiJDDSt4ND6CT1E'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    chatid = message.chat.id
    text = 'Hello. Ask me the meaning of any word. For example, try "What is the meaning of concourse"'
    bot.send_message(chatid, text)

    
@bot.message_handler(commands=['help'])
def start(message):
    chatid = message.chat.id
    text = 'To find the meaning of a word, type "What is the meaning of" followed by the word. For example, try "What is the meaning of pandemonium"'
    bot.send_message(chatid, text)

    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    chatid = message.chat.id
    if message.content_type == 'text':
            text = back.getresult(message.text)
            bot.send_message(chatid, text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "working", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='telegram-wordbot.herokuapp.com/' + TOKEN)
    return back.getresult("what is the meaning of apple"), 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
