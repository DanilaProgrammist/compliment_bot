import requests
import telebot
from bs4 import BeautifulSoup
import time
import random
from random import choice

token = "1998992268:AAHhj2apOozth2R46BU_WKaam3WFkkitsv8"
compliments_julia = []
bot = telebot.TeleBot(token)

url = 'https://heaclub.ru/100-luchshih-samyh-krasivyh-komplimentov-devushke-i-zhenshhine-o-ee-krasote-svoimi-slovami-v-proze-spisok-kak-krasivo-skazat-devushke-chto-ona-krasivaya-stishki-chetverostishya-pro-krasotu-devus/'
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
        bot.send_message(message.chat.id, random.choice(compliments_julia))
        time.sleep(5)


@bot.message_handler(func=lambda message: True)
def send_notification(message):
    bot.send_message("666667283", "Комплименты доставлены")
bot.polling()

