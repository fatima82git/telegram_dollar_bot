import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "توکن_خودت_رو_اینجا_بذار"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\nبرای دیدن قیمت دلار /price بزن"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl"
        response = requests.get(url, timeout=10)
        data = response.json()
        dollar = data['data'][0][1]
        await update.message.reply_text(f"💵 قیمت دلار: {dollar} ریال")
    except:
        await update.message.reply_text("خطا در دریافت قیمت. دوباره تلاش کن.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.run_polling()
