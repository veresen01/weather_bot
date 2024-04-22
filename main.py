import telebot
import requests
import json

bot = telebot.TeleBot('6790569555:AAGUWp7rXm5BsYn2r5W6NPOzUuIUB8Uo3J8')
API='83939960c3308f4b1e3a014f621c1041'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, в каком городе ты живешь?')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code==200:
        data=json.loads(res.text)
        temp=data['main']['temp']
        bot.reply_to(message, f'Сейчас погода: {temp} градусов')
        image='sun.png' if temp>5.0 else 'tucha.png'
        file=open('./'+image,'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город не найден')

bot.polling(none_stop=True)
