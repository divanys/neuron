import confi as cf
# import forbot as fb
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor


import numpy as np
import sys

"""
Учимся обучать нейронные сети
код взят с канала
https://www.youtube.com/@KovalevskyiAcademy
"""


class PartyNN(object):

    def __init__(self, learning_rate=0.1):
        self.weights_0_1 = np.random.normal(0.0, 2 ** -0.5, (2, 3))
        self.weights_1_2 = np.random.normal(0.0, 1, (1, 2))
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        self.learning_rate = np.array([learning_rate])

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, inputs):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        return outputs_2

    def train(self, inputs, expected_predict):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        actual_predict = outputs_2[0]

        error_layer_2 = np.array([actual_predict - expected_predict])
        gradient_layer_2 = actual_predict * (1 - actual_predict)
        weights_delta_layer_2 = error_layer_2 * gradient_layer_2
        self.weights_1_2 -= (np.dot(weights_delta_layer_2, outputs_1.reshape(1, len(outputs_1)))) * self.learning_rate

        error_layer_1 = weights_delta_layer_2 * self.weights_1_2
        gradient_layer_1 = outputs_1 * (1 - outputs_1)
        weights_delta_layer_1 = error_layer_1 * gradient_layer_1
        self.weights_0_1 -= np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer_1).T * self.learning_rate


def MSE(y, Y):
    return np.mean((y - Y) ** 2)


epochs = 5000
learning_rate = 0.05

network = PartyNN(learning_rate=learning_rate)


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
    rez = []
    # print(data['djghjc'])
    for e in range(epochs):
        inputs_ = []
        correct_predictions = []
        for input_stat, correct_predict in eval(data['djghjc']):
            network.train(np.array(input_stat), correct_predict)
            inputs_.append(np.array(input_stat)), correct_predictions.append(np.array(correct_predict))

        train_loss = MSE(network.predict(np.array(inputs_).T), np.array(correct_predictions))
        rez1 = str(train_loss)[:5]
        rez.append(rez1)
    # print(rez)
    lst = []
    for input_stat, correct_predict in eval(data['djghjc']):
        lst.append("For input: {} the prediction is: {}, {}, expected: {}".format(
            str(input_stat),
            str(network.predict(np.array(input_stat)) > .5),
            str(network.predict(np.array(input_stat))),
            str(correct_predict == 1)))
    
    lst.append(rez[-1])
    await message.answer(f"Имя: {data['username']}\n"
                            f"Адрес: {data['address']}\n"
                            f"Ответ на запрос: \n{lst}")


if __name__ == "__main__":
    executor.start_polling(dp)
