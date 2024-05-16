from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from bot import TelegramBot
from bot.config import Telegram

TARGET_USER = None  # Variable to store the target user ID

@TelegramBot.on_message(filters.command('target'))
async def set_target(_, msg: Message):
    global TARGET_USER
    replied_msg = msg.reply_to_message
    if replied_msg and replied_msg.from_user:
        target_id = replied_msg.from_user.id
        TARGET_USER = target_id
        await msg.reply(f"Target user set to {target_id}")
    else:
        await msg.reply("Please reply to a message from the target user to set the target.")

@TelegramBot.on_message(filters.command('enough'))
async def unset_target(_, msg: Message):
    global TARGET_USER
    TARGET_USER = None
    await msg.reply("Target user unset.")

@TelegramBot.on_message(filters.text)
async def send_reaction(_, msg: Message):
    global TARGET_USER
    if TARGET_USER is not None and msg.from_user and msg.from_user.id == TARGET_USER:
        try:
            await msg.react(choice(Telegram.EMOJIS))
        except (MessageIdInvalid, EmoticonInvalid, ChatAdminRequired, ReactionInvalid):
            pass
