from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5531217774:AAGevZymiqOHrV4zKMKqI7kWYyBJt1r5FQI").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print('server start')
app.run_polling()

# import matplotlib.pyplot as plt
# import numpy as np
# list = [1,2,3,2,7]
# plt.plot(list)
# plt.show()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# Python is 👍
# >>> print(emoji.emojize('Python is :thumbsup:', language='alias'))
# Python is 👍
# >>> print(emoji.demojize('Python is 👍'))
# Python is :thumbs_up:
# >>> print(emoji.emojize("Python is fun :red_heart:"))
# Python is fun ❤
# >>> print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# Python is fun ❤️ #red heart, not black heart
# >>> print(emoji.is_emoji("👍"))
# True

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4)) 