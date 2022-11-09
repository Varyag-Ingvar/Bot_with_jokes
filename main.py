from telebot.async_telebot import AsyncTeleBot, types
import asyncio
import random
from files import anekdot_list


TOKEN = ''
bot = AsyncTeleBot(TOKEN)


def get_random_anekdot():
    random_anekdot = random.choice(anekdot_list)
    audio_file = f"anekdot/{random_anekdot}"
    audio = open(audio_file, 'rb')
    return audio


@bot.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Хочу анекдот!')
    btn2 = types.KeyboardButton('id')
    btn3 = types.KeyboardButton('Научи меня пилить тг-боты!')
    btn4 = types.KeyboardButton('Не, ну не бот, а дерьмо!')
    markup.add(btn1, btn2, btn3, btn4)
    msg = '<b>ПО КНОПКАМ НИЖЕ ТЫ ПОЛУЧИШЬ:</b>' \
          '\n- каждый раз новый анекдот :)' \
          '\n- узнаешь свой id в телеге' \
          '\n- научишься пилить такие же боты сам'
    await bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)


@bot.message_handler()
async def get_user_text(message):
    greeting_list = ['И тебе саламчик от братвы, кореш!', 'И тебе не хворать!', 'Здрасьте, милсдарь!', 'Хеллоу, ёпта!']
    random_greeting = random.choice(greeting_list)
    if message.text.lower() == "привет":
        await bot.send_message(message.chat.id, random_greeting, parse_mode='html')
    elif message.text.lower() == "id":
        await bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text.lower() == "не, ну не бот, а дерьмо!":
        photo = open('kakashka.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo)
        audio = open('haha_chertila.mp3', 'rb')
        await bot.send_audio(message.chat.id, audio)
    elif message.text.lower() == "научи меня пилить тг-боты!":
        await bot.send_message(message.chat.id, "Лови ссылочку - https://www.youtube.com/watch?v=HodO2eBEz_8", parse_mode='html')
    elif message.text.lower() == "хочу анекдот!":
        audio = get_random_anekdot()
        await bot.send_audio(message.chat.id, audio)
    else:
        await bot.send_message(message.chat.id, "Шоооо? Не врубаюсь, о чем ты, бро(", parse_mode='html')


async def run():
    await bot.polling(none_stop=True)

asyncio.run(run())

