from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from message import MESSAGES
from configure import BOT_TOKEN

storage = MemoryStorage()
chatbot = Bot(token=BOT_TOKEN)
dp = Dispatcher(chatbot, storage=storage)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'])


if __name__ == "__main__":
    executor.start_polling(dp)