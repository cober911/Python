
from telebot import TeleBot,types

TOKEN = '5928076518:AAGfNT5aR393EKn9HUVStawFjm-QAYwxbMo'

bot = TeleBot(TOKEN)
print('Server start')

@bot.message_handler(commands=['start'])
def but_ts(message):
    murkup = types.InlineKeyboardMarkup(row_width=4) # создали онлайн клавиатуру
    button_1 = types.InlineKeyboardButton(text='Список телефонов', callback_data='id_1' ) # создали кнопку
    button_2 = types.InlineKeyboardButton(text='Поиск ', callback_data='id_2' ) # создали кнопку
    button_3 = types.InlineKeyboardButton(text='Отправить txt', callback_data='id_3' ) # создали кнопку
    button_4 = types.InlineKeyboardButton(text='добавить н/т', callback_data='id_4' ) # создали кнопку
    murkup.add(button_1,button_2,button_3,button_4) # добавили кнопку в клавиатуру
    bot.send_message(message.chat.id, 'Добро пожаловать в телефоный справочник', reply_markup = murkup) 

with open('student_1.txt', 'r', encoding='utf-8') as st:
    data = st.read()


@bot.callback_query_handler(func= lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'id_1':
            bot.send_message(call.message.chat.id, data )

        elif call.data == 'id_2':
            bot.send_message(call.message.chat.id, 'Кто Вам нужен?')
            @bot.message_handler(content_types = ['text'])
            def search_data(message):
                search_value = message.text
                with open('student_1.txt','r', encoding='utf-8') as file:
                    for line in file:
                        if search_value in line:
                            bot.send_message(message.chat.id, f'Вы искали {line}')
                        
        elif call.data == 'id_3':
                doc = open('student_1.txt', 'rb')
                bot.send_document(call.message.chat.id, document=doc)

        elif call.data == 'id_4':
            bot.send_message(call.message.chat.id, f'Добавьте ФИО и номер телефона')
            @bot.message_handler(content_types='text')
            def handle_text(message):
                doc = open('student_1.txt', 'a', encoding='utf-8')
                doc.write("{imia} \n".format(imia=message.text))
                  
bot.polling(non_stop=True)
        