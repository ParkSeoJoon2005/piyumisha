from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
Hello, I am Nίհα, an AI Powered ChatBot. If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Lycia", switch_inline_query_current_chat="lycia "), InlineKeyboardButton("Github", url = "https://t.me/EywaSC")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
