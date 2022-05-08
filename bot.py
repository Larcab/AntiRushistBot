from aiogram import *

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
rusizm = "пецоп", "Путин", "Putin", "Россия", "Россія"
@dp.message_handler()
async def echo_message(msg: types.Message):
    for word in rusizm:
        if word in msg.text:
            await msg.delete()
            print('Видалено:', '"' + msg.text + '"')
          

if __name__ == '__main__':
    executor.start_polling(dp)