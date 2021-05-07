import os
from pyrogram import Client

API_ID = os.environ.get("3609223", None)
API_HASH = os.environ.get("302bf5498005e091fd23c88d8e76740e", None)
TOKEN = os.environ.get("1831246366:AAHTE7bcvOasq_fWuI8EFgGiJ4cz0JYl4ek", None)

LYCIA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
