import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

MENU = [
    ["🎮 O‘yinlar", "🏆 Turnirlar"],
    ["👤 Profilim", "💳 To‘lov"],
    ["ℹ️ Yordam"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 SCHOOL TOURNAMENT ga xush kelibsiz!\n\n"
        "Turnirni tanlang va qatnashing!",
        reply_markup=ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    )

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👤 Ism: {user.first_name}\n"
        f"🆔 Telegram ID: {user.id}"
    )

async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 O‘YINLAR:\n\n"
        "🔫 Standoff 2 — 1v1\n"
        "🥇 G‘olib: 20 Gold\n\n"
        "🎯 PUBG Mobile — TDM 1v1\n"
        "🥇 G‘olib: 20 UC"
    )

async def tournaments(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 TURNIRLAR\n\n"
        "Hozircha faol turnirlar mavjud emas."
    )

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Oylik obuna: 5 000 so‘m\n"
        "Obuna muddati: 30 kun.\n"
        "To‘lovni admin tekshiradi va tasdiqlaydi."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Yordam\n"
        "Savollar bo‘yicha turnir adminiga murojaat qiling."
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎮 O‘yinlar":
        await games(update, context)
    elif text == "🏆 Turnirlar":
        await tournaments(update, context)
    elif text == "👤 Profilim":
        await profile(update, context)
    elif text == "💳 To‘lov":
        await payment(update, context)
    elif text == "ℹ️ Yordam":
        await help_command(update, context)

def main():
    if not TOKEN:
        print("XATO: BOT_TOKEN sozlanmagan!")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("games", games))
    app.add_handler(CommandHandler("tournaments", tournaments))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("SCHOOL TOURNAMENT BOT ISHLADI!")
    app.run_polling()

if __name__ == "__main__":
    main()