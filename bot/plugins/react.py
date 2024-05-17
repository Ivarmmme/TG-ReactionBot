from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from bot import TelegramBot
from bot.config import Telegram

ALLOWED_USER_ID = 6369933143  # Replace with the ID of the user who should have access
TARGET_USER = None  # Variable to store the target user ID

TARGET_SET_GIF_URL = "https://graph.org/file/046bb529b1f065a4db29e.mp4"

@TelegramBot.on_message(filters.command('target'))
async def set_target(_, msg: Message):
    global TARGET_USER
    if msg.from_user and msg.from_user.id == ALLOWED_USER_ID:
        replied_msg = msg.reply_to_message
        if replied_msg and replied_msg.from_user:
            TARGET_USER = replied_msg.from_user.id
            await msg.reply(f"okay, started")
        else:
            await msg.reply("Please reply to a user.")
    else:
        await msg.reply_animation(animation=TARGET_SET_GIF_URL)
        
@TelegramBot.on_message(filters.command('enough'))
async def unset_target(_, msg: Message):
    global TARGET_USER
    if msg.from_user and msg.from_user.id == ALLOWED_USER_ID:
        TARGET_USER = None
        await msg.reply("Target user unset.")
    else:
        await msg.reply_animation(animation=TARGET_SET_GIF_URL)
        
@TelegramBot.on_message(filters.text)
async def send_reaction(_, msg: Message):
    global TARGET_USER
    if TARGET_USER is not None and msg.from_user and msg.from_user.id == TARGET_USER:
        try:
            await msg.react(choice(Telegram.EMOJIS))
        except (MessageIdInvalid, EmoticonInvalid, ChatAdminRequired, ReactionInvalid):
            pass
