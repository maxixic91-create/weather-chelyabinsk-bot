# 🚀 Подробная инструкция по деплою на Render

## Шаг 1: Создание Telegram бота

1. Откройте Telegram
2. Найдите [@BotFather](https://t.me/botfather)
3. Отправьте команду: `/newbot`
4. Введите имя: `Челябинск Погода`
5. Введите username: `chelyabinsk_weather_bot`
6. **Сохраните полученный токен!** Он выглядит так: `123456789:AAxxxxxxxxxxxxxxxx`

## Шаг 2: Подготовка GitHub репозитория

### Вариант A: Создать новый репозиторий

1. Зайдите на [github.com](https://github.com)
2. Нажмите **"+"** → **"New repository"**
3. Название: `weather-chelvabinsk-bot`
4. Выберите **Public**
5. **НЕ** добавляйте README, .gitignore, лицензию
6. Нажмите **"Create repository"**

### Вариант B: Очистить существующий

1. Зайдите в ваш репозиторий
2. Нажмите **"Settings"** → вниз до **"Danger Zone"**
3. Нажмите **"Delete this repository"**
4. Создайте новый по инструкции выше

## Шаг 3: Загрузка кода

1. **Распакуйте** архив `weather-bot-complete.zip`
2. **Откройте** папку `weather-bot-complete`
3. **На GitHub** нажмите **"Add file"** → **"Upload files"**
4. **Перетащите** ВСЕ файлы из папки в окно браузера
5. **Должно отобразиться:** "Uploading 28 files"
6. **Напишите сообщение:** `Initial commit - complete weather bot`
7. **Нажмите** **"Commit changes"**

## Шаг 4: Деплой на Render

1. **Зайдите** на [render.com](https://render.com)
2. **Зарегистрируйтесь** через GitHub
3. **Нажмите** **"New +"** → **"Blueprint"**
4. **Подключите** GitHub репозиторий
5. **Выберите** `weather-chelvabinsk-bot`
6. **Добавьте** переменную окружения:
   - Key: `BOT_TOKEN`
   - Value: `ваш_токен_от_BotFather`
7. **Нажмите** **"Apply"**

## Шаг 5: Проверка

Через 2-3 минуты:

1. **На Render** статус изменится на **"Live"**
2. **Откройте Telegram**
3. **Найдите** бота: `@chelyabinsk_weather_bot`
4. **Отправьте** `/start`

## 🔄 Обновление бота

```bash
# Локально
git add .
git commit -m "Update bot"
git push

# Render автоматически перезапустит бота
```

## 📊 Мониторинг логов

1. **На Render** → ваш сервис → **"Logs"**
1. Вы увидите:

```
2024-01-15 12:00:00 - Starting bot...
2024-01-15 12:00:01 - Bot @chelyabinsk_weather_bot is ready!
2024-01-15 12:00:02 - Web server started on port 8080
```

## ⏰ Как предотвратить засыпание (24/7)

Бесплатный тариф Render **засыпает через 15 минут** без активности.

### Решение: UptimeRobot

1. **Зарегистрируйтесь** на [UptimeRobot](https://uptimerobot.com)
1. **Добавьте** мониторинг:

- Type: **HTTP(s)**
- URL: `https://chelyabinsk-weather-bot.onrender.com/health`
- Interval: **5 minutes**
1. **Сохраните**

Теперь бот будет просыпаться каждые 5 минут и работать 24/7!

## 🆘 Частые проблемы

### Ошибка: "BOT_TOKEN not set"

**Решение:** Добавьте переменную `BOT_TOKEN` в настройках Render

### Ошибка: "Module not found"

**Решение:** Проверьте структуру папок, должны быть `handlers/`, `keyboards/`, `services/`, `data/`

### Бот не отвечает

**Решение:**

1. Проверьте логи Render
1. Убедитесь, что токен правильный
1. Перезапустите сервис: Manual Deploy → Deploy latest commit

## ✅ Готово!

Ваш бот работает! Теперь вы можете:

- Получать прогноз погоды для любого района Челябинска
- Смотреть почасовой прогноз
- Получать рекомендации по погоде

**Ссылка на бота:** `t.me/chelyabinsk_weather_bot`

