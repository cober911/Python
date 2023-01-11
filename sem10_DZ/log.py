import xlsxwriter
import telebot
from xlsxwriter import worksheet

import config
from telebot import types
import datetime as dt
count = 1

workbook = xlsxwriter.Workbook('messages.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0, 'Дата')
worksheet.write(0,1, 'Время')
worksheet.write(0,2, 'Отправитель')
worksheet.write(0,3, 'id отправителя')

bot = telebot.TeleBot('5928076518:AAGfNT5aR393EKn9HUVStawFjm-QAYwxbMo')

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    global count
    if message.content_type == 'text':
        # if message.text != 'Результат':
            worksheet.write(count, 0, str(dt.datetime.now().date()))
            worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
            worksheet.write(count, 2, message.chat.username)
            worksheet.write(count, 3, message.from_user.id)
            count += 1
        # else:
            workbook.close()





