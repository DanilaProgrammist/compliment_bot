import requests
import telebot
from bs4 import BeautifulSoup
import time
import random
from random import choice

token = "your_token"
compliments_julia = []
bot = telebot.TeleBot(token)

url = 'https://datki.net/komplimenti/#copy/'
responce = requests.get(url)
value = BeautifulSoup(responce.text, 'lxml')
compliments = value.find_all('div', class_= 'entry-summary entry-content')

for compliment in compliments:
    print(compliment.text)
    compliments_julia.append(compliment.text)
    if len(compliments_julia) > 500:
        break
print("Сбор комприментов завершён")
print(compliments_julia)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    for i in range(3):
        bot.send_message("your_id", random.choice(compliments_julia))
        time.sleep(15)


@bot.message_handler(func=lambda message: True)
def send_notification(message):
    bot.send_message("your_id", "Комплименты доставлены")
bot.polling()

