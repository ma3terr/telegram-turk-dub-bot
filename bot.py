import asyncio
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# توکن از Railway / Environment Variable
TOKEN = os.getenv("8448007441:AAF8KOqaMoQVQcl_cvEptt0T8DqmWyHxyeg")

async def send_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # فعلاً یک فیلم ثابت
    # بعداً می‌تونیم چندتا فیلم کنیم
    video = "FILE_ID_اینجا"

    msg = await context.bot.send_video(
        chat_id=chat_id,
        video=video,
        caption="🎬 Türkçe Dublaj\nاین پیام ۲۰ ثانیه بعد حذف می‌شود"
    )

    # صبر ۲۰ ثانیه
    await asyncio.sleep(20)

    # حذف پیام ربات
    await context.bot.delete_message(
        chat_id=chat_id,
        message_id=msg.message_id
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, send_movie))
    app.run_polling()

if __name__ == "__main__":
    main()
