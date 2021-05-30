# бібліотеки
import requests
import telebot
from telebot import types
from datetime import datetime

token = ("1665297243:AAFwxuPK0_oJPR7_TZ_3f-HGn0_bFRq9Adk") # адрес бота
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start']) # При введенні команди '/start' привітаємося з користувачем.
def handle_start_help(message):
    bot.send_message(message.chat.id, f" Привіт, я TradeBot"
                                      f"\nЯкщо ти не знаєш що далі, пиши /help!")

@bot.message_handler(commands=['help']) # При введенні команди '/help' виводимо список команд
def handle_start_help(message):
    bot.send_message(message.chat.id, f" Наразі все що я вмію:"
                                      f"\n/crypto_price - crypto price today"
                                      f"\n/gold_price - gold price today"
                                      f"\n/news - last news about finance fond"
                                                                                 )

@bot.message_handler(commands=['crypto_price']) # При введенні команди '/crypto_price'
def handle_crypto_price_key(message):
        key_add = types.InlineKeyboardMarkup() # Добавляю кнопки
        key1 = types.InlineKeyboardButton(text='LTC to USD', callback_data='key1')
        key_add.add(key1)
        key2 = types.InlineKeyboardButton(text='BTC to USD', callback_data='key2')
        key_add.add(key2)
        key3 = types.InlineKeyboardButton(text='DOGE to USD', callback_data='key3')
        key_add.add(key3)
        key4 = types.InlineKeyboardButton(text='ETH to USD', callback_data='key4')
        key_add.add(key4)
        bot.send_message(message.from_user.id, text='Choose a pair of cryptocurrencies ⤵', reply_markup=key_add)

@bot.callback_query_handler(func=lambda call: True) # нажаття кнопки
def callback_worker(call):
    if call.data == "key1":
        req = requests.get(url="https://yobit.net/api/2/ltc_usd/ticker") # crupto api
        response = req.json()
        high_price = response["ticker"]["high"]
        sell_price = response["ticker"]["sell"]
        buy_price = response["ticker"]["buy"]
        bot.send_message(call.message.chat.id, f"Час:{datetime.now().strftime('%d.%m.%Y %H:%M')}"
                                         f"\n\n\nПік:{high_price}"
                                         f"\n\nПродаж:{sell_price},"
                                         f"\n\nКупівля:{buy_price}"
                                                                     )
    if call.data == "key2":
        req = requests.get(url="https://yobit.net/api/2/btc_usd/ticker")
        response = req.json()
        high_price1 = response["ticker"]["high"]
        sell_price1 = response["ticker"]["sell"]
        buy_price1 = response["ticker"]["buy"]
        bot.send_message(call.message.chat.id, f"Час:{datetime.now().strftime('%d.%m.%Y %H:%M')}"
                                         f"\n\n\nПік:{high_price1}"
                                         f"\n\nПродаж:{sell_price1},"
                                         f"\n\nКупівля:{buy_price1}"
                                                                     )
    if call.data == "key3":
        req = requests.get(url="https://yobit.net/api/2/doge_usd/ticker")
        response = req.json()
        high_price1 = response["ticker"]["high"]
        sell_price1 = response["ticker"]["sell"]
        buy_price1 = response["ticker"]["buy"]
        bot.send_message(call.message.chat.id, f"Час:{datetime.now().strftime('%d.%m.%Y %H:%M')}"
                                         f"\n\n\nПік: {high_price1}"
                                         f"\n\nПродаж: {sell_price1},"
                                         f"\n\nКупівля: {buy_price1}"
                                                                     )
    if call.data == "key4":
        req = requests.get(url="https://yobit.net/api/2/eth_usd/ticker")
        response = req.json()
        high_price1 = response["ticker"]["high"]
        sell_price1 = response["ticker"]["sell"]
        buy_price1 = response["ticker"]["buy"]
        bot.send_message(call.message.chat.id, f"Час: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
                                         f"\n\n\nПік: {high_price1}"
                                         f"\n\nПродаж: {sell_price1},"
                                         f"\n\nКупівля: {buy_price1}"
                                                                     )
@bot.message_handler(commands=['gold_price'])# При введенні команди '/gold_price'
def handle_start_help(message):

    url = "https://gold-price1.p.rapidapi.com/get_price/USD"# api gold price

    headers = {
        'x-rapidapi-key': "a7544b7cd9msh560c79499597685p1cdb49jsn63c7b4d689e5",
        'x-rapidapi-host': "gold-price1.p.rapidapi.com"
    }

    req = requests.request("GET", url, headers=headers)
    response = req.json()
    gold_price = response["gold"]["price"]
    percentage = response["gold"]["percentage"]
    bot.send_message(message.chat.id, f"Час: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
                                           f"\n\nЦіна: {gold_price}"
                                           f"\nПроцент: {percentage}"
                                                                        )

@bot.message_handler(commands=['news'])# При введенні команди '/news'
def handle_start_help(message):
    url = "https://trending-financial-data.p.rapidapi.com/finance"

    querystring = {"limit":"10","skip":"0","langs":"en"}

    headers = {
    'x-rapidapi-key': "a7544b7cd9msh560c79499597685p1cdb49jsn63c7b4d689e5",
    'x-rapidapi-host': "trending-financial-data.p.rapidapi.com"
    }

    req = requests.request("GET", url, headers=headers, params=querystring)
    response = req.json()
    title_c = response[6]["title"]
    urls_c = response[6]["url"]
    bot.send_message(message.chat.id, f"{title_c}"
                                      f"\n{urls_c}"
                                                     )

bot.polling() # запуск бота