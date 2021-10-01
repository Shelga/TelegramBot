from sqlite3.dbapi2 import IntegrityError
import telebot
import sqlite3
import datetime


bot = telebot.TeleBot("1999350759:AAFIWJB-no9lxy876tzmEtIZTmycGYwDlUA", parse_mode=None)



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






@bot.message_handler(commands=['send'])
def send_welcome(message):
    bot.reply_to(message, "Enter your weight")


@bot.message_handler(func=lambda message: True)
def save_to_db(message):
    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS weight_from(
        user_id INTEGER,
        date TEXT,
        message TEXT 
    )""")

    connect.commit()

    id_user = message.chat.id
    date_message = datetime.datetime.fromtimestamp(int(message.date)).strftime('%Y-%m-%d %H:%M:%S')
    message_user = message.text
    params = (id_user, date_message, message_user)

    if message_user.strip().isdigit():
        cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
        connect.commit()

        previous_values = cursor.execute("SELECT * FROM weight_from ORDER BY id DESC LIMIT 1;")
        previous_values = cursor.fetchone()
        print("send",previous_values[3])
        print("User input is Number")
    else:
        bot.reply_to(message, "Yours input is string")
        print("User input is string")

    
    
    # cursor.execute("INSERT INTO weight_from VALUES (NULL, ?, ?, ?)", params)
    # connect.commit()

    # previous_values = cursor.execute("SELECT * FROM weight_from ORDER BY id DESC LIMIT 1;")
    # previous_values = cursor.fetchone()
    # print("send",previous_values[3])


# def send_message(message):
    # bot.send_message(message.chat.id, f"Your weight is: {message_user}")
    # print("here")
    

@bot.message_handler(commands=['show_previous_values'])
def send_previous_values(message):

    print("hello")

    connect = sqlite3.connect('message.db')
    cursor = connect.cursor()

    previous_values = cursor.execute("SELECT message FROM weight_from ORDER BY id DESC LIMIT 1;")
    previous_values = cursor.fetchone()
    print("show", previous_values)
    connect.commit()

    print("previous_values", previous_values)

    bot.send_message(message.chat.id, f"Your previous weight is: {previous_values}")
 

print('STARTED...')

bot.polling()