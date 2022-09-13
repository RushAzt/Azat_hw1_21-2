from aiogram import types, Dispatcher
from config import bot, ADMIN
import random

async def game(message: types.Message):
    if message.text.startswith('game') or message.from_user.id in ADMIN:
        emojies = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
        rand_game = random.choice(emojies)
        await bot.send_dice(message.chat.id, emoji=rand_game)
    else:
        try:
            x = int(message.text)
            await bot.send_message(message.from_user.id, x * x)
        except:
            await bot.send_message(message.from_user.id, message.text)

# # @dp.message_handler()
# async def echo(message: types.Message):
#     try:
#         x = int(message.text)
#         await bot.send_message(message.from_user.id, x * x)
#     except:
#         await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game)
    # dp.register_message_handler(echo)