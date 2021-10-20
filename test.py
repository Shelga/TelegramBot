from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import datetime as dt
from matplotlib.dates import DateFormatter
import matplotlib.ticker

# ## Loading ENV parameters
# load_dotenv()
# token = os.getenv('TOKEN')

# ## Starting a Telegram bot
# bot = telebot.TeleBot(token, parse_mode=None)



# @bot.message_handler(commands=['test'])
# def send_welcome(message):
#     connect = sqlite3.connect('message.db')
#     cursor = connect.cursor()
#     cursor.execute("DELETE from weight_from where id > 107")
#     connect.commit()
    











print('STARTED...')

bot.polling()