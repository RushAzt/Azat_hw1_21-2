from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot

# викторина2
# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)
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
        reply_markup=markup
    )
# викторина3
    # @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_3)
    question = "Какого камня нету в реке ?"
    answers = [
        "Круглого",
        "Мокрого",
        "Сухого",
        "Красного",
        "Большого",
        "Не знаю(",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сухого камня нету в РЕКЕ!",
        open_period=10

    )

def register_hanflers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,lambda call: call.data == "button_call_2")