from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv



load_dotenv()

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token, parse_mode=None)


# @bot.message_handler(commands=['send'])
# def send_welcome(message):
#     bot.reply_to(message, "Enter your weight")

# @bot.message_handler(func=lambda message: True)
# def save_to_db(message):
#     # connect to the database
#     connect = sqlite3.connect('message.db')
#     cursor = connect.cursor()

#     cursor.execute("""CREATE TABLE IF NOT EXISTS weight_from(
#         user_id INTEGER,
#         date TEXT,
#         message TEXT 
#     )""")

#     connect.commit()
#     # cursor.close()


#     # user message data
#     id_user = message.chat.id
#     date_message = datetime.datetime.fromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
#     message_user = message.text
    
#     params = (id_user, date_message, message_user)

#     if message_user.replace('.','',1).isdigit():
#         cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
#         connect.commit()
#         cursor.close()

#         bot.send_message(message.chat.id, f"Your weight is: {message_user}")
#     else:
#         bot.send_message(message.chat.id, "Yours input is string. Call the command /send again")
#         print("User input is string. ")




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




    print("show", previous_values_w)
    connect.commit()



    print("previous_values_p", previous_values_p)
    print("previous_values_w", previous_values_w)
    bot.send_message(message.chat.id, f"Your previous weight is: {previous_values_w}")









    # connect = sqlite3.connect('message.db')
    # cursor = connect.cursor()
    # cursor.execute("DELETE from weight_from where id > 2")
    # connect.commit()
    # cursor.close()








print('STARTED...')

bot.polling()