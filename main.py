import telebot
import os
from telebot import apihelper

token = '5339797518:AAEYDDERTcC8gGJ24gLhDUa3NwSPK211q10'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('панель')
    bot.send_message(message.chat.id, 'Бот запущен! Вся система в норме.', reply_markup=keyboard)

@bot.message_handler(commands=['passwd_NoName6842'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Сменить пароль', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Удалить файлы сервера', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Остановить сервер', callback_data=5))
    bot.send_message(message.chat.id, text="Выберите функцию:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text.lower() == 'панель':
        bot.send_message(message.chat.id, 'Введите пароль:')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Выполнено!')
    answer = ''
    if call.data == '3':
        answer = 'Пароль изменен!'
        os.system('python3.7 main2.py')
    elif call.data == '4':
        answer = 'Файлы сервера были удалены!'
        os.system('cd /root/\nrm -r new')
    elif call.data == '5':
        answer = 'Сервер был выключен!'
        os.system('pkill python3.7')
        os.system('pkill python3.7')
        os.system('pkill python3.7')
        os.system('pkill python3.7')

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()
