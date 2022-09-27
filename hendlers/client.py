from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot
import random
from asyncio import sleep
from data_base.bot_db import sql_command_random
from parser import news

#игра с ботом
async def dice(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.full_name}!\nНачинаем игру!!!\n1-BOT\n2-Вы")
    await sleep(1)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)


    if bot_data > user_data:
        await bot.send_message(message.from_user.id, 'Вы проиграли!')
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, 'Вы победили!')
    else:
        await bot.send_message(message.from_user.id, 'Ничья!')
# закреп сообшении
async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Надо ответить на сообщение")

# фотки мемы
# @dp.message_handler(commands=['mem'])
async def bot_mem(message: types.Message):
    list = ["media/mem1.jpeg", "media/mem2.jpg", "media/mem3.jpg",
            "media/mem4.jpg", "media/mem5.jpg", "media/mem6.jpg",
            "media/mem7.jpg", "media/mem8.jpg", "media/mem9.jpg",
            "media/mem10.jpg", "media/mem11.jpg",
            "media/mem12.jpg", "media/mem13.jpg", "media/mem14.jpg",
            "media/mem15.jpg", "media/mem16.jpg", "media/mem17.jpg",
            "media/mem18.jpg", "media/mem19.jpg", "media/mem20.jpg", ]
    photo = open(random.choice(list), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

# Информация
# @dp.message_handler(commands=["start"])
async def send_command(message: types.Message):
    await message.answer(f"Приветствую тебя {message.from_user.first_name}\n"
                         f"Кандайсын эу?")

# Викторина
# @dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "В каком году Кыргызстан был независимым?"
    answers = [
        "1998",
        "1996",
        "1991",
        "1993",
        "1990",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation="31 августа 1991 году",
        open_period=10,
        reply_markup=markup
    )

async def help_command(message: types.Message):
    await message.answer(f"Разбирайся сам!")

async def show_random_menu(message: types.Message):
    await sql_command_random(message)

async def parser_news(message: types.Message):
    data = news.parser()
    for item in data:
        await bot.send_message(
            message.from_user.id,
            f"{item['time']}\n\n"
            f"{item['title']}\n"
            f"{item['desc']}\n\n"
            f"{item['link']}"
        )


# Вызов
def register_handlers_clien(dp: Dispatcher):
    dp.register_message_handler(bot_mem, commands=["mem"])
    dp.register_message_handler(send_command, commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="/!")
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(show_random_menu, commands=['get'])
    dp.register_message_handler(parser_news, commands=['news'])