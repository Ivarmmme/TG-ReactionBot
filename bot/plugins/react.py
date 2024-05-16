from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from bot import TelegramBot
from bot.config import Telegram

AUTHORIZED_USERS = [6369933143]  # List of authorized user IDs

TARGET_USER = None  # Variable to store the target user ID

@TelegramBot.on_message(filters.command('target') & filters.user(AUTHORIZED_USERS))
async def set_target(_, msg: Message):
    global TARGET_USER
    if len(msg.command) == 2:
        target_id = int(msg.command[1])
        TARGET_USER = target_id
        await msg.reply(f"Target user set to {target_id}")
    else:
        await msg.reply("Please specify a user ID.")

@TelegramBot.on_message(filters.command('enough') & filters.user(AUTHORIZED_USERS))
async def unset_target(_, msg: Message):
    global TARGET_USER
    TARGET_USER = None
    await msg.reply("Target user unset.")

@TelegramBot.on_message(filters.text & filters.user(AUTHORIZED_USERS))
async def send_reaction(_, msg: Message):
    global TARGET_USER
    if TARGET_USER is not None and msg.from_user and msg.from_user.id == TARGET_USER:
        try:
            await msg.react(choice(Telegram.EMOJIS))
        except (MessageIdInvalid, EmoticonInvalid, ChatAdminRequired, ReactionInvalid):
            pass
