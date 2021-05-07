from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
Hello, I am [Nίհα](https://telegra.ph/file/ff2e456161e8ef77fe7e3.jpg), an AI Powered ChatBot. If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("🦋 CЯΣΛƬӨЯ 🦋", url = "https://t.me/AidanNia"), InlineKeyboardButton("🦋 SUPPӨЯƬ 🦋", url = "https://t.me/EywasSC")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
