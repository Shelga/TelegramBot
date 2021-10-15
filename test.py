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

## Settings for matplot grid
fig, ax = plt.subplots()




## Loading ENV parameters
load_dotenv()
token = os.getenv('TOKEN')

## Starting a Telegram bot
bot = telebot.TeleBot(token, parse_mode=None)

# @bot.message_handler(commands=['show_previous_week'])
# def send_previous_values(message):


#     connect = sqlite3.connect('message.db')
#     cursor = connect.cursor()

#     previous_values_p = cursor.execute("SELECT message FROM weight_from ORDER BY id DESC LIMIT 7;")
#     previous_values_p = cursor.fetchall()

#     previous_values_w = []
#     for i in previous_values_p:
#         previous_values_w.append(float(i[0]))
#     previous_values_w.reverse()

#     previous_days_p = cursor.execute("SELECT date FROM weight_from ORDER BY id DESC LIMIT 7;")
#     previous_days_p = cursor.fetchall()

#     previous_days_w = []
#     for i in previous_days_p:
#         previous_days_w.append(i[0])
#     previous_days_w.reverse()

#     print("previous_days_w", previous_days_w)
#     print("previous_values_w", previous_values_w)
#     connect.commit()


#     x = previous_days_w
#     ax.clear()
    
#     plt.subplot(111)
#     ax.set(xlabel='time (days)', ylabel='weight (kg)',
#        title='Weight change chart for 7 days')

#     ax.grid(which='major',
#         color = 'k',
#         linewidth = 1,
#         linestyle = ':')
#     ax.minorticks_on()
  
#     y = previous_values_w
  
#     ax.plot(x, y, color = 'b', linewidth = 3)


#     ax.tick_params(axis = 'both',   
#         which = 'major', 
#         pad = 5,
#         labelsize = 7,
#         labelbottom = True, 
#         labelleft = True,
#         labelrotation = 45) 

#     fig.savefig("test.png")

#     file = open('test.png', 'rb')

#     bot.send_photo(message.chat.id, file)


#     









    # connect = sqlite3.connect('message.db')
    # cursor = connect.cursor()
    # cursor.execute("DELETE from weight_from where id = 98")
    # connect.commit()







print('STARTED...')

bot.polling()