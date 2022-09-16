from aiogram.utils import executor
from config import dp
import logging
from hendlers import client, callback, extra, fsmAdminMenu
# вызов
client.register_handlers_clien(dp)
callback.register_hanflers_callback(dp)
fsmAdminMenu.register_handlers_fsm_admin(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
