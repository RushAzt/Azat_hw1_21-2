from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboards.client_kb import cancel_markup

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" or message.from_user.id == ADMIN:
        await FSMAdmin.photo.set()
        await message.answer(f"Здравствуйте {message.from_user.first_name} "
                             f"скинь фотку еды...",
                             reply_markup=cancel_markup)
    else:
        await message.answer("Пиши в личку!")
        await message.answer("Вы не администратор!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Введите названия блюда!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Опиши блюда!")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Введи цену блюда...")




async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
    await bot.send_photo(message.from_user.id,
                         data['photo'],
                         caption=f"Блюдо: {data['name']}\n"
                                 f"Описание: {data['description']}\n"
                                 f"Цена: {data['price']}\n")
    await state.finish()
    await message.answer("Ваша меню готово!")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Регистрация отменена!")


def register_handlers_fsm_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)