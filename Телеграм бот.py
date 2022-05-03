import telebot
from telebot import types
# from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('5317785622:AAEBeSL514cNnvSW-Q_JZ1YPMfpBHbdBzWk')  # Создаем экземпляр бота

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📨О игре Тайный Санта")
    btn2 = types.KeyboardButton("Чат-рулетка")
    btn3 = types.KeyboardButton("⚠Помощь")
    btn4 = types.KeyboardButton("Заполнить анкету")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Заполнить анкету" or ms_text == "Анкета" or ms_text == "Новая Анкета":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать заполнение")
        btn2 = types.KeyboardButton("Исправить анкету")
        btn3 = types.KeyboardButton("Посмотреть анкету")
        back = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы готовитесь к становлению Таным Сантой", reply_markup=markup)

    elif ms_text == "Начать заполнение":
        bot.send_message(chat_id, text="Как вас зовут?")
        user_name = input()
        bot.send_message(chat_id, text="Сколько вам лет?")
        user_age = input()
        bot.send_message(chat_id, text="Чем вы увлекаетесь?")
        user_hobbi = input()
        bot.send_message(chat_id, text="Есть ли у вас аллергии? Если есть-на что?")
        user_allergic = input()
        bot.send_message(chat_id, text="На какой адрес Тайному Санте отправить подарок?")
        user_adress = input()
        bot.send_message(chat_id, text="Имя/Ник:" + user_name + "Возраст:" + user_age + "Интересы:" + user_hobbi + "Аллергии:" + user_allergic + "Адрес:" + user_adress)

    elif ms_text == "Исправить анкету" or ms_text == "Исправить Анкету":
        bot.send_message(chat_id, text="В разработке")

    elif ms_text == "Посмотреть анкету" or ms_text == "Посмотреть Анкету":
        bot.send_message(chat_id, text="В разработке")

    elif ms_text == "Помощь" or ms_text == "⚠Помощь":
        bot.send_message(chat_id, "Случилась беда? Секунду!")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="За помощью просим сюда", url="https://yandex.ru/video/preview/18294331597446296112")
        key1.add(btn1)

    else:
        bot.send_message(chat_id, text="А енто зачем? Я не поняль " + ms_text)


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()
