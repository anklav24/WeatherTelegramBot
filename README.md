# WeatherTelegramBot

### Для чего предназначен проект:
Это телеграм бот который отвечает прогнозом погоды в ответ на название города.

### Инструкции по конфигурации и установке (Короткий путь):
- Регистрируемся на сайте погоды https://openweathermap.org/, получаем ключ API
- Получаем токен и создаем нового бота через **[@BotFather](https://t.me/BotFather)** в телеграме коммандой "/newbot"
- Скачиваем и запускаем файл WeatherTelegramBot.exe (Найти можно в разделе "releases")
- Вводим токены на соответствующие запросы от программы.
```
Ваш API токен от Pyowm: YOUR_TOKEN
```
```
Ваш API токен от Телеграм бота: YOUR_TOKEN
```
- Запустить программу на сервере/пк
- Найти бота в телеграмме.
- Наслаждаться результатом своих непосильных трудов.

### Инструкции по конфигурации и установке (Истинный путь):
- установить Python https://www.python.org/downloads/
- Установить pyowm (В командной строке от имени администратора вводим: "pip install pyowm" без кавычек)
- Установить pyTelegramBotAPI ("pip install pyTelegramBotAPI")
- Регистрируемся на сайте погоды https://openweathermap.org/, получаем ключ API
- Получаем токен и создаем нового бота через  **[@BotFather](https://t.me/BotFather)** в телеграме коммандой "/newbot"
- Регистрируемся на [Heroku.com](https://Heroku.com) и следуем мануалу, устанавливаем все что нужно.
- Добавляем файл Procfile (Без расширения, важно!)

Содержимое Procfile: `worker: python weather_telegram_bot.py`

- Добавляем файл requirements.txt с необходимыми зависимостями.

- Переходим в папку с проектом в командной строке или баше и логинимся.

`heroku login`

- Создаем новый контейнер на хероку

 `heroku create weather-telegram-bot-010 --buildpack heroku/python`

- Пушим билд 

`git push heroku master`

- Устанавливаем в переменные окружения наши ключи API 

heroku: `heroku config:set YOUR_API_KEY_NAME=YOUR_API_KEY`

ubuntu: to `~$ vi ~./bashrc` file add `export "YOUR_API_KEY_NAME=YOUR_API_KEY"`

windows: push win + break keys "System" -> "Advanced system settings" -> "Environment Variables..." -> "New..."

- Запускаем приложение если вдруг само не поехало

`heroku ps:scale worker=1`

- Если надо остановить бота

`heroku ps:scale worker=0`

- Проверяем логи

`heroku logs --tail`

- Найти бота в телеграмме.
- Наслаждаться результатом своих непосильных трудов.

### Примеры использования:
Возможность узнать погоду в текущий момент в любом городе через телеграм.
Короче говоря захотел и узнал. Изи.

Можете найти моего бота в телеграме:

 **[@WeatherPyowmTelegramBot](https://t.me/WeatherPyowmTelegramBot)**
 
### Используемая лицензия: 
Apache License Version 2.0, January 2004 

### Правила участия в проекте:
Рад любой помощи и доработкам.
