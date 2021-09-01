import telebot 
from main import get_titles

bot = telebot.TeleBot('1997559511:AAGYXCFD9Y6DLK0L6l9Q5t_yXD5jC1LCgEQ')

@bot.message_handler(commands=['start', 'старт'])
def send_welcome(message):	
	bot.reply_to(message, 'Hello, im your firts bot')

#return your message
# @bot.message_handler(func=lambda m: True)
# def parrot(message):
# 	bot.reply_to(message, message.text)

@bot.message_handler(commands=['picture'])
def send_pick(message):
	chat_id = message.chat.id 
	bot.send_photo(chat_id=chat_id, photo=open('maxresdefault.jpg','rb'))



@bot.message_handler(commands=['series'])
def send_series(message):
	bot.reply_to(message, '\n'.join(get_titles()))
print(get_titles)
bot.polling()