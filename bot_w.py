from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv



load_dotenv()

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token, parse_mode=None)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "Welcome! I will help you track your weight changes. \n" +
        "To get help press /help. \n" + 
        "To send the current weight press /send. \n" +
        "To know previous values press /show_previous_values. \n" +
        "To get a graph of changes press /show_chart"
    )


@bot.message_handler(commands=['help'])  
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(  
        telebot.types.InlineKeyboardButton(  
            'Message the developer', url='telegram.me/olikLelik8'  
  )  
    )  
    bot.send_message(  
        message.chat.id,  
        '1) To send the current weight, press /send. \n' +
        '2) Next you will receive a confirmation message about the entered weight \n' +
        '3) By selecting the command /show_previous_values you request the previous value.\n' +
        '4) To see the changes over the last 10 days, call the command /show_chart.\n' +
        '5) You can also write to the creator of the bot using the link:',  
        reply_markup=keyboard  
    )


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

    if message_user.isdigit():
        cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
        connect.commit()
        bot.send_message(message.chat.id, f"Your weight is: {message_user}")
    else:
        bot.send_message(message.chat.id, "Yours input is string. Call the command /send again")
        print("User input is string. ")




    


print('STARTED...')

bot.polling()