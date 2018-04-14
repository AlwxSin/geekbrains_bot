#!/usr/bin/env python
import random
import pickle

import telebot
from telebot import types
from telebot.types import Message

TOKEN = '386377468:AAHqCK1Xm0x_rBSvNRhDfM5v1Xzr2VfVTFw'
STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'

bot = telebot.TeleBot(TOKEN)

USERS = set()


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'There is no answer =(')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    print(message.from_user.id)
    if 'Alex Goodkid' in message.text:
        bot.reply_to(message, 'Alex is good kid')
        return
    reply = str(random.random())
    if message.from_user.id in USERS:
        reply += f"  {message.from_user}, hello again"
    bot.reply_to(message, reply)
    USERS.add(message.from_user.id)


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)


@bot.inline_handler(lambda query: query.query)
def query_text(inline_query):
    print(inline_query)
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling(timeout=60)
