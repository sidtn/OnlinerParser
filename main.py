from get_data import get_data
import telebot
from config import api_key_tel


def tel_bot():
    bot = telebot.TeleBot(api_key_tel)

    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        bot.reply_to(message, "Введите наименование видеокарты, например '6800 XT': ")


    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        if len(get_data(message.text)) == 0:
            bot.reply_to(message, "Видеокарты не существует или нет в наличии.")
        else:
            try:
                iter = 0
                for key, value in get_data(message.text):
                    iter += 1
                    bot.send_message(message.chat.id, f'Цена: {key} BYN \n{value}')
                    if iter == 3:
                        break
            except:
                bot.reply_to(message, "Видеокарты не существует или нет в наличии.")


    bot.polling()


def main():
    tel_bot()

if __name__ == '__main__':
    main()