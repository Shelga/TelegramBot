from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv

import matplotlib.pyplot as plt
import numpy as np



load_dotenv()

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['show_previous_week'])
def send_previous_values(message):


    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    previous_values_p = cursor.execute("SELECT message FROM weight_from ORDER BY id DESC LIMIT 7;")
    previous_values_p = cursor.fetchall()

    previous_values_w = []
    for i in previous_values_p:
        previous_values_w.append(float(i[0]))
    previous_values_w.reverse()

    previous_days_p = cursor.execute("SELECT date FROM weight_from ORDER BY id DESC LIMIT 7;")
    previous_days_p = cursor.fetchall()

    previous_days_w = []
    for i in previous_days_p:
        previous_days_w.append(i[0])
    previous_days_w.reverse()

    print("previous_days_w", previous_days_w)
    print("previous_values_w", previous_values_w)
    connect.commit()


    # t = previous_days_w
    # s = previous_values_w

    # fig, ax = plt.subplots()
    # ax.plot(t, s)

    # ax.set(xlabel='time (d)', ylabel='weight (kg)',
    #    title='Weight change chart for 7 days')
    # ax.grid()

    # fig.savefig("test.png")
    # # plt.show()

    # file = open('test.png', 'rb')


    # bot.send_photo(message.chat.id, file)
    # bot.send_photo(message.chat.id, "FILEID")
#     # bot.send_message(message.chat.id, f"Your previous weight is: {previous_values_w}")









    # connect = sqlite3.connect('message.db')
    # cursor = connect.cursor()
    # cursor.execute("DELETE from weight_from where id = 98")
    # connect.commit()







print('STARTED...')

bot.polling()