from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp
import logging
import random


@dp.message_handler(commands=['mem'])
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


@dp.message_handler(commands=["start"])
async def send_command(message: types.Message):
    await message.answer(f"Приветствую тебя {message.from_user.first_name}\n"
                         f"Это лучший бот когда-либо ты видел!\n"
                         f"Команды:\n"
                         f"/quiz - викторины\n"
                         f"/mem - мемы")


@dp.message_handler(commands=["quiz"])
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Дата смерти Елизавета || ?"
    answers = [
        "8 февраля 1725 г",
        "13 марта 1881 г",
        "5 марта 1953 г",
        "8 апреля 2013 г",
        "8 сентября 2022 г",
        "9 сентября 2021 г",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="8 сентября 2022 г",
        open_period=10,
    )


@dp.message_handler()
async def echo(message: types.Message):
    try:
        x = int(message.text)
        await bot.send_message(message.from_user.id, x * x)
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
