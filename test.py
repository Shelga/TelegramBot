from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv



load_dotenv()

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token, parse_mode=None)




  






# @bot.message_handler(commands=['show_previous_week'])
# def send_previous_values(message):

#     print("hello")

#     connect = sqlite3.connect('message.db')
#     cursor = connect.cursor()

#     previous_values_p = cursor.execute("SELECT message FROM weight_from ORDER BY id DESC LIMIT 7;")
#     previous_values_p = cursor.fetchall()
#     previous_values_w = previous_values_p[::-1]



#     print("show", previous_values_w)
#     connect.commit()

#     print("previous_values", previous_values_w)
#     bot.send_message(message.chat.id, f"Your previous weight is: {previous_values_w}")







# @bot.message_handler(commands=['tesg'])
# def tesg(message):
#     connect = sqlite3.connect('message.db')
#     cursor = connect.cursor()


#     cursor.execute("""CREATE TABLE IF NOT EXISTS user_id(
#         id INTEGER
#     )""")

#     connect.commit()

#     id_user = message.chat.id
#     cursor.execute(f"SELECT id FROM user_id WHERE id = {id_user}")
#     id_all = cursor.fetchone()
#     if id_all is None:
#         user_id = [message.chat.id]
#         cursor.execute("INSERT INTO user_id VALUES(?);", user_id)
#         connect.commit()
#     else: 
#         bot.send_message(message.chat.id, "You are already in the chat")


print('STARTED...')

bot.polling()