from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv



load_dotenv()

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token, parse_mode=None)



@bot.message_handler(commands=['send'])
def send_welcome(message):
    bot.reply_to(message, "Enter your weight")

@bot.message_handler(func=lambda message: True)
def save_to_db(message):
    # connect to the database
    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS weight_from(
        user_id INTEGER,
        date TEXT,
        message TEXT 
    )""")

    connect.commit()


    # user message data
    id_user = message.chat.id
    date_message = datetime.datetime.fromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
    message_user = message.text
    
    params = (id_user, date_message, message_user)
    print((id_user, date_message, message_user))

    if message_user.isdigit():
        cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
        connect.commit()
        print("Done!")
    else:
        bot.send_message(message.chat.id, "Yours input is string")
        print("User input is string")

    
    
        # cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
        # connect.commit()

        # previous_values = cursor.execute("SELECT * FROM weight_from ORDER BY id DESC LIMIT 1;")
        # previous_values = cursor.fetchone()
        # print("send",previous_values[3])
    


    # if message_user.strip().isdigit():
    #     cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
    #     connect.commit()

    #     previous_values = cursor.execute("SELECT * FROM weight_from ORDER BY id DESC LIMIT 1;")
    #     previous_values = cursor.fetchone()
    #     print("send",previous_values[3])
    #     print("User input is Number")
    # else:
    #     bot.send_message(message.chat.id, "Yours input is string")
    #     print("User input is string")

    
    
    # cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
    # connect.commit()

    # previous_values = cursor.execute("SELECT * FROM weight_from ORDER BY id DESC LIMIT 1;")
    # previous_values = cursor.fetchone()
    # print("send",previous_values[3])




    


print('STARTED...')

bot.polling()