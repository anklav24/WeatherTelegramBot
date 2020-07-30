"""Простой телеграм бот отвечающий прогнозом погоды @WeatherTelegramBot"""

# Проверьте не блокируется ли API телеграмма на уровне провайдера
# Документация https://github.com/eternnoir/pyTelegramBotAPI
#              https://github.com/csparpa/pyowm

import pyowm  # Импортируем пакет с помощью которого мы узнаем погоду
# from pyowm.utils.config import get_default_config  # Импорт конфига owm
import telebot  # Импортируем пакет бота через ввод в CMD "pip install pytelegrambotapi"
import os  # Импортируем для использования переменных окружения
import time

# config_dict = get_default_config()
# config_dict['language'] = 'ru'  # Настраиваем язык для owm.
owmToken = os.getenv('YOUR_OWN_TOKEN')  # Регистрируемся на сайте погоды, получаем ключ API
owm = pyowm.OWM(owmToken, language='ru')
mgr = owm.weather_manager()
botToken = os.getenv('YOUR_TELEGRAM_BOT_TOKEN')  # Получаем токен через BotFather в телеграме в чате коммандами. /newbot имя моего APITelegramBot
bot = telebot.TeleBot(botToken)


# Когда боту пишут текстовое сообщение вызывается эта функция
@bot.message_handler(content_types=['text'])
def send_message(message):
    """Send the message to user with the weather"""
    # Отдельно реагируем на сообщения /start и /help
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    elif message.text == "/Start":
        bot.send_message(message.from_user.id,
                         "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    elif message.text == "/Help":
        bot.send_message(message.from_user.id,
                         "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
    else:
        # С помощью try заставляю пройти код, если функция observation не находит город
        # и выводит ошибку, то происходит переход к except
        try:
            # Имя города пользователь вводит в чат, после этого мы его передаем в функцию
            observation = mgr.weather_at_place(message.text)
            weather = observation.weather
            temp = weather.temperature("celsius")["temp"]  # Присваиваем переменной значение температуры из таблицы
            print(time.ctime(), "Message:", message.text, temp, "C", weather.detailed_status)

            # Формируем и выводим ответ
            answer = "В городе " + message.text + " сейчас " + weather.detailed_status + "." + "\n"
            answer += "Температура около: " + str(temp) + " С" + "\n\n"
            if temp < -10:
                answer += "Пи**ц как холодно, одевайся как танк!"
            elif temp < 10:
                answer += "Холодно, одевайся теплее."
            elif temp > 25:
                answer += "Жарень."
            else:
                answer += "На улице вроде норм!!!"
        except Exception:
            answer = "Не найден город, попробуйте ввести название снова.\n"
            print(time.ctime(), "Message:", message.text, 'Error')

        bot.send_message(message.chat.id, answer)  # Ответить сообщением


# Запускаем бота
bot.polling(none_stop=True)
