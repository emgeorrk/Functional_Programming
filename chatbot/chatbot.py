import requests
import telebot

bot = telebot.TeleBot('')
telebot.logger.setLevel(telebot.logging.DEBUG)

@bot.message_handler(commands=['weather'])
def weather(message: telebot.types.Message):
    arguments = message.text.removeprefix('/weather')
    if len(arguments) <= 1:
        bot.send_message(message.chat.id, 'Usage: /weather [City]')
    arguments = arguments.removeprefix(' ')

    print(len(arguments))

    data = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': str(arguments), 'type': 'like', 'units': 'metric', 'APPID': '368e827be4b38db51ff960ca88b5c396'}).json()

    bot.send_message(message.chat.id, f'City: {data["list"][0]["name"]}\nConditions: {data["list"][0]["weather"][0]["description"]}\nTemp: {data["list"][0]["main"]["temp"]}°C\nTemp_min: {data["list"][0]["main"]["temp_min"]}°C\nTemp_max: {data["list"][0]["main"]["temp_max"]}°C')


@bot.message_handler(commands=['rates'])
def rates(message: telebot.types.Message):
    data = requests.get(
        'https://iss.moex.com/iss/statistics/engines/currency/markets/selt/rates.json?iss.meta=off').json()
    usdrub, eurrub = data['cbrf']['data'][0][3], data['cbrf']['data'][0][6]
    bot.send_message(message.chat.id, f'USD/RUB: {usd}\nEUR/RUB: {eur}')


@bot.message_handler(commands=['exchange'])
def exchange(message: telebot.types.Message):
    arguments = message.text.removeprefix('/exchange ').split()
    if len(arguments) != 2:
        bot.send_message(message.chat.id, 'Usage: /exchange [Target currency] [RUB\'s Amount]')
        return

    data = requests.get(
        'https://iss.moex.com/iss/statistics/engines/currency/markets/selt/rates.json?iss.meta=off').json()
    usdrub, eurrub = data['cbrf']['data'][0][3], data['cbrf']['data'][0][6]

    if arguments[0] == 'USD':
        target = usdrub
    else:
        target = eurrub
    bot.send_message(message.chat.id, f'{arguments[1]} RUB = {round(float(arguments[1])/float(target), 2)} {arguments[0]}')


@bot.message_handler(commands=['time'])
def time(message: telebot.types.Message):
    city = message.text.removeprefix('/time')
    if len(city) <= 1:
        bot.send_message(message.chat.id, 'Usage: /time [City]')
        return
    city = city.removeprefix(' ')

    data = requests.get(f'https://api.api-ninjas.com/v1/worldtime?city={city}&X-Api-Key=FVOpjPXwOWQ6MNz2OBN7XQ==pX31NDr7LZXXVITq').json()
    bot.send_message(message.chat.id, f'Time in {city}: {data["datetime"]}')


@bot.message_handler(commands=['start', 'help'])
def info(message: telebot.types.Message):
    bot.send_message(message.chat.id, '/weather [City] - Current weather\n/rates - Current exchange rate\n/exchange [Target currency] [RUB\'s Amount] - Exchange RUB to USD or EUR\n/time [City] - Current time in specific city')


if __name__ == '__main__':
    bot.infinity_polling()
