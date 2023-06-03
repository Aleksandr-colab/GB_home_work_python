# Задача 1. Напишите бота для техподдержки. 
# Бот должен записывать обращения пользователей в файл.

import random
import telebot
from telebot import types

game_started = False
r_number = 0
counter = 0

token = ''
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn3 = types.KeyboardButton('играть')
markup.add(itembtn3)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Хочешь поиграть? Напиши '/играть'", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def read_text_commands(message):
    data=open('text.txt', mode='a', encoding='utf-8')
    data.write(f'{message.from_user.id}:{message.text}\n')
    data.close()

bot.infinity_polling()