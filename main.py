import requests
import telebot
from telebot import  types #для кнопок
from bs4 import BeautifulSoup

responce1 = requests.get('https://minfin.com.ua/ua/currency/usd/')
soup1 = BeautifulSoup(responce1.content,"html.parser")
kyrs_usd = soup1.find('div' ,{"class":"sc-1x32wa2-9 bKmKjX"})
print(kyrs_usd)

responce2 = requests.get("https://minfin.com.ua/ua/currency/eur/")
soup2 = BeautifulSoup(responce2.content,"html.parser")
kyrs_eur = soup2.find('div' ,{"class":"sc-1x32wa2-9 bKmKjX"})
print(kyrs_eur)

responce3 = requests.get("https://minfin.com.ua/ua/currency/pln/")
soup3 = BeautifulSoup(responce3.content, "html.parser")
kyrs_pln = soup3.find('div', {"class":"sc-1x32wa2-9 bKmKjX"})
print(kyrs_pln)


bot = telebot.TeleBot("5946796978:AAHXcMpBuBVB6e5ZHWxtns0q3-Vhcaq4ylo")
@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_USD = types.KeyboardButton("USD💵 в UAH")
    item_EUR = types.KeyboardButton("EUR💶 в UAH")
    item_PLN = types.KeyboardButton("PLN в UAH")
    markup.add(item_USD)
    markup.add(item_EUR)
    markup.add((item_PLN))
    bot.send_message(m.chat.id, "Виберіть курс із списку", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'USD💵 в UAH':
        answer = kyrs_usd
    elif message.text.strip() == 'EUR💶 в UAH':
        answer = kyrs_eur
    elif message.text.strip() == 'PLN в UAH':
        answer = kyrs_pln
    bot.send_message(message.chat.id, answer)
bot.polling()