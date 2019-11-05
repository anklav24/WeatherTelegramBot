# Простой телеграм бот отвечающий прогнозом погоды @WeatherTelegramBot
# Проверьте не блочится ли API телеграма на уровне провайдера
# Документация https://github.com/eternnoir/pyTelegramBotAPI
#              https://github.com/csparpa/pyowm
# Импортируем пакет с помощью которого мы узнаем погоду

import pyowm
# Импортируем пакет бота через ввод в CMD "pip install pytelegrambotapi"
import telebot

# Регистрируемся на сайте погоды, получаем ключ API
owmToken = input('Ваш API токен от Pyowm: ')
owm = pyowm.OWM(owmToken, language='ru')
# Получаем токен через BotFather в телеграме в чате коммандами. /newbot имя моего APITelegramBot
botToken = input('Ваш API токен от Телеграм бота: ')
bot = telebot.TeleBot(botToken)


# Когда боту пишут текстовое сообщение вызывается эта функция
@bot.message_handler(content_types=['text'])
def send_message(message):
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
            observation = owm.weather_at_place(message.text)
            w = observation.get_weather()
            # Присваиваем переменной значение температуры из таблицы
            temp = w.get_temperature('celsius')["temp"]

            # Формируем и выводим ответ
            answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "." + "\n"
            answer += "Температура около: " + str(temp) + " С" + "\n\n"
            if temp < -10:
                answer += "Пи**ц как холодно, одевайся как танк!"
            elif temp < 10:
                answer += "Холодно, одевайся теплее."
            elif temp > 25:
                answer += "Жарень."
            else:
                answer += "На улице вроде норм.!!!"
        except:
            answer = "Не найден город, попробуйте ввести название снова.\n"
            # Ответить сообщением
        bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True)
