import confi as cf

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor


import gensim

w2v_fpath = "all.norm-sz100-w10-cb0-it1-min100.w2v"
w2v = gensim.models.KeyedVectors.load_word2vec_format(w2v_fpath, binary=True, unicode_errors='ignore')
w2v.init_sims(replace=True)


bot = Bot(token=cf.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    name = State()
    address = State()
    djghjc = State()
  

@dp.message_handler(commands=['reg'])
async def user_register(message: types.Message):
    await message.answer("Введите своё имя")
    await UserState.name.set()

  
@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Отлично! Теперь введите ваш адрес.")
    await UserState.next() 

@dp.message_handler(state=UserState.address)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Введите желаемый запрос")
    await UserState.next() 



@dp.message_handler(state=UserState.djghjc)
async def get_djghjc(message: types.Message, state: FSMContext):
    await state.update_data(djghjc=message.text)
    data = await state.get_data()
    lst = []
    for word, score in w2v.most_similar(positive=[f"{data['djghjc']}"]):
        lst.append(str(word)+' '+str(score)+'\n')
    await message.answer(f"Имя: {data['username']}\n"
                            f"Адрес: {data['address']}\n"
                            f"Ответ на запрос: \n{''.join(lst)}")
    lst.clear()
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp)
