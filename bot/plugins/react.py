from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from bot import TelegramBot
from bot.config import Telegram

ALLOWED_USER_ID = 6369933143  # Replace with the ID of the user who should have access

@TelegramBot.on_message(filters.command('target'))
async def set_target(_, msg: Message):
    global TARGET_USER
    if msg.from_user and msg.from_user.id == ALLOWED_USER_ID:
        replied_msg = msg.reply_to_message
        if replied_msg and replied_msg.from_user:
            target_id = replied_msg.from_user.id
            TARGET_USER = target_id
            await msg.reply(f"Target user set to {target_id}")
        else:
            await msg.reply("Please reply to a message from the target user to set the target.")
    else:
        await msg.reply("You are not authorized to use this command.")

@TelegramBot.on_message(filters.command('enough'))
async def unset_target(_, msg: Message):
    global TARGET_USER
    if msg.from_user and msg.from_user.id == ALLOWED_USER_ID:
        TARGET_USER = None
        await msg.reply("Target user unset.")
    else:
        await msg.reply("You are not authorized to use this command.")
        
