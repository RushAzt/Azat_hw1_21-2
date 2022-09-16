from aiogram import types, Dispatcher
from config import bot, ADMIN
import random

async def game(message: types.Message):
    if message.text.startswith('game') or message.from_user.id in ADMIN:
        emojies = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
        rand_game = random.choice(emojies)
        await bot.send_dice(message.chat.id, emoji=rand_game)
    else:
        if message.text.isdigit():
            await bot.send_message(message.chat.id, int(message.text)**2)
        else:
            await bot.send_message(message.chat.id, message.text)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game)