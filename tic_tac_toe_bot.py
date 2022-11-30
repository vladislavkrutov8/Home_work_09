import telebot
import json
import tic_tac_toe

API_TOKEN='5889749775:AAEdC_z8Z8AND-8ByQT0NnuWIyTWPTQ1p8o'

bot = telebot.TeleBot(API_TOKEN)
game_status = False
wait_row = False
wait_column = False
cur_row = 0
cur_column = 0
player = 0
sign = ['X', 'O']
n = 3


@bot.message_handler(commands=['start'])

def start_message(message):
  
    # Приглашение к игре
    bot.send_message(message.chat.id, f'Привет <b>{message.from_user.first_name}</b>!', parse_mode='html')
    bot.send_message(message.chat.id, "Добро пожаловать в игру Крестики-Нолики, для ознакомления с правилами выбери команду /help")

@bot.message_handler(commands=['help'])
def start_message(message):
    # Приглашение к игре
    bot.send_message(message.chat.id, "Правила очень просты. Перед тобой поле 3x3 клетки.\nКаждому игроку по очереди необходимо занимать одну из клеток фигурой X или 0 \nПобеждает тот, кто первый занимает 3 клетки по горизонтали \nвертикали или диагонали \nУдачи!")
    bot.send_message(message.chat.id, "Чтобы начать, нажмите /game")

@bot.message_handler(commands=['game'])
def start_message(message):
    global game_status
    global wait_row
    global field
    field = tic_tac_toe.field_init(n)
    bot.send_message(message.chat.id, tic_tac_toe.field_string(field))
    bot.send_message(message.chat.id, f"\nХодит {player+1}-й игрок\nНапишите номер строчки, где поставить {sign[player]}?")
    game_status = True
    wait_row = True

@bot.message_handler()
def game_message(message):
    global cur_row
    global cur_column
    global wait_row
    global wait_column
    global player
    global field
    global game_status

    # Если идет игра переходим к проверкам
    if game_status == True:
        # Если ожидалась на вход строка хода
        try:
            if wait_row == True:
                cur_row = int(message.text)
                bot.send_message(message.chat.id, "А в каком номере столбца?")
                wait_row = False
                wait_column = True
            # Если ожидался на вход столбец хода
            elif wait_column == True:
                cur_column = int(message.text)
                wait_row = True
                wait_column = False
                if field[cur_row - 1][cur_column - 1] == '--':
                    field[cur_row - 1][cur_column - 1] = sign[player]
                    bot.send_message(message.chat.id, tic_tac_toe.field_string(field))
                    # Проверка, вдруг кто-то уже виграл
                    if tic_tac_toe.check_win(field) != 0:
                        bot.send_message(message.chat.id, f"Игра окончена!\nВыиграл {player+1}-й игрок\nЧтобы сыграть еще раз, нажмите /start")
                        game_status = False

                    # Если игра продолжается, идет смена хода
                    if game_status == True:
                        # Переход хода и сброс координат хода
                        player = 1 - player
                        cur_row = 0
                        cur_column = 0
                        bot.send_message(message.chat.id, f"\nХодит {player+1}-й игрок\nНапишите номер строчки, где поставить {sign[player]}?")
                else:
                    bot.send_message(message.chat.id, tic_tac_toe.field_string(field))
                    bot.send_message(message.chat.id,
                                     f"В это поле уже походили ранее, попробуйте еще раз\nНапишите номер строчки, где поставить {sign[player]}?")
                    wait_row = True
                    wait_column = False
        except:
            bot.send_message(message.chat.id, tic_tac_toe.field_string(field))
            bot.send_message(message.chat.id, f"Неверные координаты, попробуйте еще раз\nНапишите номер строчки, где поставить {sign[player]}?")
            wait_row = True
            wait_column = False
    # Если игра не начиналась, подсказать команду начала
    else:
        # bot.send_message(message.chat.id, "Для начала игры нажмите /start")
        bot.send_message(message.chat.id, "Что то пошло не так")
    
print("Бот работает")
bot.polling()