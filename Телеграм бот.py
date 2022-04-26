import(telebot)
bot=telebot.Telebot(5317785622:AAEBeSL514cNnvSW-Q_JZ1YPMfpBHbdBzWk)
@bot.messege_handler(commands=["start"])
def start(message, res=False):
    chat_id= message.chat.id
    murkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.ReplyKeyboardButton("📨О игре Тайный Санта")
    btn2=types.ReplyKeyboardButton("❄О телеграм боте")
    btn3=typesReplyKeyboardButton("⚠Помощь")
    murkup.add(btn1,btn2,btn3)

    bot.send_message(chat_id, text="Привет, {0.first_name}! Я бот-помощник для игры в Тайного Санту!".format(message.from_user), reply_murkup=murkup)

    @bot.message_handler(content_types=["text"])
    def get_text_messages(message):
        chat_id = message.chat.id
        ms_text = message.text

        if ms_text == "О игре Тайный Санта" or ms_text == "📨О игре Тайный Санта":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Развлечения")
            btn2 = types.KeyboardButton("Управление")
            back = types.KeyboardButton("⚠Помощь")
            markup.add(btn1, btn2, btn3, back)
            bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)