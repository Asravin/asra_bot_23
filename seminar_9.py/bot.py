import telebot
import random
import time
import json

token = '5903051935:AAGNyKRC6XV0tySiZQCv79ca9V6xtBVM5O4'
bot = telebot.TeleBot(token)

number = 0

with open('horoscope.json', 'r', encoding='utf-8') as horos:
    dictionary = json.load(horos)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1= telebot.types.KeyboardButton('Cлучайное число')
    item_2= telebot.types.KeyboardButton('Таймер')
    item_3= telebot.types.KeyboardButton('Кинуть кость')
    item_4= telebot.types.KeyboardButton('Как дела?')
    item_5= telebot.types.KeyboardButton('Загадай число')
    item_6= telebot.types.KeyboardButton('Знак зодиака')
    item_7= telebot.types.KeyboardButton('Покажи id стикера')
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7)
    bot.send_message(message.chat.id,'Привет! Выбери нужный пункт меню: ', reply_markup=markup)


def start(message):
    bot.send_message(message.chat.id,'Привет! Как у тебя дела?')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower()=='хорошо':
        bot.send_message(message.chat.id,'Я рад за тебя!')
    elif message.text.lower()=='плохо':
        bot.send_message(message.chat.id,'Что случилось?')
    elif message.text.lower()=='cлучайное число':
        bot.send_message(message.chat.id, str(random.randint(1, 1000)))
    elif message.text.lower()=='таймер':    
        bot.send_message(message.chat.id,'Введите время старта  таймера: ')
        bot.register_next_step_handler(message,alarm)
    elif message.text.lower()=='кинуть кость':
        bot.send_message(message.chat.id, 'Ваша сторона кубика: ' + str(random.randint(1, 6)))
    elif message.text.lower()=='как дела?':
        some_list = ["Отлично", "Сойдет", "Бывало и лучьше", "Все ужасно", "А у тебя как?", "Вполне не плохо"]
        reply = random.randint(0, len(some_list))
        bot.send_message(message.chat.id, some_list[reply])
    elif message.text.lower()=='загадай число':
        global number
        number = random.randint(1, 10)
        bot.send_message(message.chat.id,'Введите ваше число: ')
        bot.register_next_step_handler(message,enigma)
    elif message.text.lower()=='знак зодиака':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_1= telebot.types.KeyboardButton('Овен')
        item_2= telebot.types.KeyboardButton('Телец')
        item_3= telebot.types.KeyboardButton('Близнецы')
        item_4= telebot.types.KeyboardButton('Рак')
        item_5= telebot.types.KeyboardButton('Лев')
        item_6= telebot.types.KeyboardButton('Дева')
        item_7= telebot.types.KeyboardButton('Весы')
        item_8= telebot.types.KeyboardButton('Скорпион')
        item_9= telebot.types.KeyboardButton('Стрелец')
        item_10= telebot.types.KeyboardButton('Козерог')
        item_11= telebot.types.KeyboardButton('Водолей')
        item_12= telebot.types.KeyboardButton('Рыбы')
        
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(message.chat.id,'Выбери свой знак зодиака: ',reply_markup=markup)
        bot.register_next_step_handler(message,horoscope)
    else:
        bot.send_message(message.chat.id,'Даже не знаю, что тебе ответить')

@bot.message_handler(content_types=['text'])
def alarm(message):
    bot.send_message(message.chat.id,'Таймер запущен')
    time = message

@bot.message_handler(content_types=['text'])
def enigma(message):
    if message.text.lower() != f'{number}':
        bot.send_message(message.chat.id, "Неправильно! Давай еще раз)")
        bot.register_next_step_handler(message, enigma)
    else:
        bot.send_message(message.chat.id, "Верно, у тебя получилось! Правильный ответ: " + str(number))

@bot.message_handler(content_types=['text'])
def horoscope(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_0= telebot.types.KeyboardButton('Вернуться назад')
    markup.add(item_0)
    # bot.send_message(message.chat.id,dictionary[message.text],reply_markup=markup)
    if message.text != 'Вернуться назад':
        bot.send_message(message.chat.id,dictionary[message.text],reply_markup=markup)
        bot.register_next_step_handler(message,horoscope)

bot.polling(none_stop=True)


