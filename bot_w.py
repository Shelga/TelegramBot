import telebot
import sqlite3
import datetime
import os
from dotenv import load_dotenv

import matplotlib.pyplot as plt



## Settings for matplot grid
fig, ax = plt.subplots()

## Loading ENV parameters
load_dotenv()
token = os.getenv('TOKEN')

## Starting a Telegram bot
bot = telebot.TeleBot(token, parse_mode=None)

## Flags
sending_weeight = False


## Command /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "Welcome! I will help you track your weight changes. \n" +
        "To get help press /help. \n" + 
        "To send the current weight press /send. \n" +
        "To know previous values press /show_previous_values. \n" +
        "To get a graph of changes press /show_chart"
    )

## Command /help
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

## Command /send
@bot.message_handler(commands=['send'])
def send_welcome(message):
    global sending_weeight
    sending_weeight = True
    bot.reply_to(message, "Enter your weight")

## Command /show_previous_values
@bot.message_handler(commands=['show_previous_values'])
def send_previous_values(message):

    ## Connecting to the database
    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    previous_values = cursor.execute("SELECT message FROM weight_from ORDER BY id DESC LIMIT 1;")
    previous_values = cursor.fetchone()

    connect.commit()
    cursor.close()

    print("previous_values", previous_values[0])
    bot.send_message(message.chat.id, f"Your previous weight is: {previous_values[0]}")

## Command //show_previous_week
@bot.message_handler(commands=['show_previous_week'])
def send_previous_values(message):

    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    previous_values_p = cursor.execute("SELECT message FROM weight_from ORDER BY id DESC LIMIT 7;")
    previous_values_p = cursor.fetchall()
    connect.commit()

    previous_values_w = []
    for i in previous_values_p:
        previous_values_w.append(float(i[0]))
    previous_values_w.reverse()
    previous_values_w =  str(previous_values_w)[1:-1]
    

    bot.send_message(message.chat.id, f"Your previous 7 parameters : {previous_values_w}")


## Command //show_chart
@bot.message_handler(commands=['show_chart'])
def send_previous_values(message):

    ## Connecting to the database
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


    ## Creating a graph
    x = previous_days_w
    ax.clear()
    
    plt.subplot(111)
    ax.set(xlabel='time (days)', ylabel='weight (kg)',
       title='Weight change chart for 7 days')

    ax.grid(which='major',
        color = 'k',
        linewidth = 1,
        linestyle = ':')
    ax.minorticks_on()
  
    y = previous_values_w
  
    ax.plot(x, y, color = 'b', linewidth = 3, label='kg')

    ax.tick_params(axis = 'both',   
        which = 'major', 
        pad = 5,
        labelsize = 7,
        labelbottom = True, 
        labelleft = True,
        labelrotation = 45) 

    fig.savefig("test.png")

    file = open('test.png', 'rb')

    bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: True)
def save_to_db(message):
    print('HERE')
    global sending_weeight
    if sending_weeight:
        ## Connecting to the database
        connect = sqlite3.connect('message.db')
        cursor = connect.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS weight_from(
            user_id INTEGER,
            date TEXT,
            message TEXT 
        )""")

        connect.commit()


        ## User message data
        id_user = message.chat.id
        date_message = datetime.datetime.fromtimestamp(int(message.date)).strftime('%Y-%m-%d')
        message_user = message.text
        
        params = (id_user, date_message, message_user)

        ## From string to float
        if message_user.replace('.','',1).isdigit():
            cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
            connect.commit()
            cursor.close()

            bot.send_message(message.chat.id, f"Your weight is: {message_user}")
        else:
            bot.send_message(message.chat.id, "Yours input is string. Call the command /send again")
            print("User input is string. ")
        sending_weeight = False 

print('STARTED...')

bot.polling()