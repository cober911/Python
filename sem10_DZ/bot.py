import config
from telebot import TeleBot, types
import xlsxwriter
import log

TOKEN = ''
 
bot = TeleBot(TOKEN)
print('Server start')

user_num1 = ''
user_num2 = ''
user_proc = ''
user_result =   None


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    log.send_text(message)
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + " я бот калькулятор\nВведите число: ", reply_markup=markup)
    bot.register_next_step_handler(msg, process_num1_step)

def process_num1_step(message, user_result = None):
    try:
        global user_num1
        if user_result == None:
            user_num1 = int(message.text)
        else:
            user_num1 = str(user_result)


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('+')
        itembtn2 = types.KeyboardButton('-')
        itembtn3 = types.KeyboardButton('*')
        itembtn4 = types.KeyboardButton('/')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

        msg = bot.send_message(message.chat.id, 'Выберете операцию', reply_markup=markup)
        bot.register_next_step_handler(msg, process_proc_step)
    except Exception as e:
        bot.reply_to(message, 'Ой, что-то пошло не так')


def process_proc_step(message):
    try:
        global user_proc

        user_proc = message.text
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(message.chat.id, "Введите еще число", reply_markup=markup)
        bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e:
        bot.reply_to(message, 'Ой, что-то пошло не так')

def process_num2_step(message):
    try:
        global user_num2
        user_num2 = int(message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('Результат')
        itembtn2 = types.KeyboardButton('Продолжить вычисление')
        markup.add(itembtn1, itembtn2)

        msg = bot.send_message(message.chat.id, "Показать результат или продолжить операцию?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e:
        bot.reply_to(message, 'Ой, что-то пошло не так')

def process_alternative_step(message):
    try:
        calc()

        markup = types.ReplyKeyboardRemove(selective=False)

        if message.text.lower()=="результат":
            bot.send_message(message.chat.id, calcResultPrint(), reply_markup=markup)
        elif message.text.lower()=="продолжить вычисление":
            process_num1_step(message, user_result)
    except Exception as e:
        bot.reply_to(message, 'Ой, что-то пошло не так')


def calcResultPrint():
    global user_num1, user_num2, user_proc, user_result
    return "Результат" + str(user_num1) + '' + user_proc + '' + str(user_num2) + ' = ' + str(user_result)

def calc():
    global user_num1, user_num2, user_proc, user_result
    user_result = eval(str(user_num1) + user_proc + str(user_num2))
    return user_result

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()


if __name__ == '__main__':
    bot.polling(none_stop=True)