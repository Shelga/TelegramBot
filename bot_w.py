from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime


bot = telebot.TeleBot("1999350759:AAFIWJB-no9lxy876tzmEtIZTmycGYwDlUA", parse_mode=None)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 
        "Welcome! I will help you track your weight changes. \n" +
        "To get help press /help. \n" + 
        "To send the current weight press /send. \n" +
        "To know previous values press /show_previous_values. \n" +
        "To get a graph of changes press /show_chart"
    )


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


@bot.message_handler(commands=['tesg'])
def send_welcome(message):
    bot.reply_to(message, "Enter your weight")


@bot.message_handler(func=lambda message: True)
def save_to_db(message):
    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS weight(
        id INTEGER,
        date TEXT,
        message TEXT 
    )""")

    connect.commit()

    id_user = message.chat.id
   
    date_message = datetime.datetime.fromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
    print(date_message)
    message_user = message.text
    
    cursor.execute("INSERT INTO weight VALUES(?, ?, ?);", [id_user, date_message,  message_user])
    connect.commit()
    

def echo_all(message):
	bot.reply_to_message("your weight is:", message.text)
    


print('STARTED...')

bot.polling()