from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from bot import TelegramBot
from bot.config import Telegram

ALLOWED_USERS = [6824897749]  # List of user IDs

@TelegramBot.on_message(filters.text)
async def send_reaction(_, msg: Message):
    if msg.from_user and msg.from_user.id in ALLOWED_USERS:
        try:
            await msg.react(choice(Telegram.EMOJIS))
        except (MessageIdInvalid, EmoticonInvalid, ChatAdminRequired, ReactionInvalid):
            pass

