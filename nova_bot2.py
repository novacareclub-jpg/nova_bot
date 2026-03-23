import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Получаем токен из переменной окружения
TOKEN = "8750176149:AAE0w5gbuLgMm0NcuOt1HOOJXj1XZ6ZNAw4"

# Ссылки
LINK_УСЛОВИЯ = "https://bedecked-city-56b.notion.site/NOVA-Terms-of-Participation-3269248859738001aeccc5db56fa767a"
LINK_ОПЛАТА = "https://whop.com/nova-woman-s-club/nova-ed/"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
Добро пожаловать в пространство NOVA 🤍
Здесь начинается твой новый путь — мягко, бережно и по-настоящему.
Ты в окружении женщин, которые выбирают рост, глубину и себя.

Выбери нужный раздел ниже, чтобы начать✨
"""
    keyboard = [
        [InlineKeyboardButton("Вступить", callback_data="join")],
        [InlineKeyboardButton("Поддержка", callback_data="support")],
        [InlineKeyboardButton("Правила", url=LINK_УСЛОВИЯ)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в NOVA Club!", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()
        if query.data == "join":
            keyboard = [
                [InlineKeyboardButton("Условия", url=LINK_УСЛОВИЯ)],
                [InlineKeyboardButton("Оплата", url=LINK_ОПЛАТА)]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text("Выберите:", reply_markup=reply_markup)
        elif query.data == "support":
            await query.edit_message_text("Чат с поддержкой пока не создан.")
    except Exception as e:
        print("Игнорируем старый callback:", e)

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Бот запущен!")
    app.run_polling()

python-telegram-bot==20.4

git init
git add .
git commit -m "Initial commit"

git branch -M main
git remote add origin https://github.com/<nova_bot>/nova_bot.git
git push -u origin main
