import telebot
import json
import calc_racional

API_TOKEN='5889749775:AAEdC_z8Z8AND-8ByQT0NnuWIyTWPTQ1p8o'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    # Приглашение к игре
    bot.send_message(message.chat.id, "Введите математическое выражение: \nСписок команд и операций можно увидеть через команду /help")

@bot.message_handler(commands=['help'])
def start_message(message):
    # Приглашение к игре
    bot.send_message(message.chat.id, "Выражение для вычисления вводится строкой.\nВводить можно: \n- числа\n- мнимую единицу i или j (для комплексных выражений)\n- Доступны стандарные операции +, -, *, /\n- скобки ()")
    bot.send_message(message.chat.id, "Чтобы начать, нажмите /start")

@bot.message_handler()
def calc_message(message):
        try:
            if 'i' in message.text or 'j' in message.text:
                data = message.text
                data = data.replace('i', 'j')
                data = data.replace('+j', '+1j')
                data = data.replace('-j', '-1j')
                data = data.replace('/j', '/1j')
                data = data.replace('*j', '*1j')
                data = data.replace('(j', '(1j')
                if data[0] == 'j': data = '1' + data
                bot.send_message(message.chat.id, eval(data))
            else:
                bot.send_message(message.chat.id, calc_racional.calc(message.text.replace(' ', '')))
            bot.send_message(message.chat.id, "Введите математическое выражение для вычисления:")
        except:
            bot.send_message(message.chat.id, "Математическое выражение не распознано.\nНажмите /help для более подробной информации.")

print("Бот работает")
bot.polling()


