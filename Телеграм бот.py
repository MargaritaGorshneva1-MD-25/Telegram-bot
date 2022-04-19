import(telegram)
bot=telebot.Telebot(5317785622:AAEBeSL514cNnvSW-Q_JZ1YPMfpBHbdBzWk)
@bot.messege_handler(commands=["start"])
def start(message, res=False):
    chat_id= message.chat.id
    bot.send_message(chat.id, text="Привет, {0.first_name}! Я тестовый бот.".format(message.from_user))

@bot.message_handler(content_types=["text"])
def ger_text_messages(message):
    chat_id=message.chat.id
    ms_text=message.text
    bot.send_message(chat_id, text="Да слышу я тебя. Твоё сообщение:" + ms_text)

bot.polling(none_stop=True, interval=0)