import telebot

bot = telebot.TeleBot('1183512137:AAHk1In1XOZxNGrPUYT0CYA44zKSsch1Kkk')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет, это реализация алгоритма Диффи-Хеллмана')
    bot.send_message(message.from_user.id, 'Запустить алгоритм? (Да/Нет)')


@bot.message_handler(content_types=['text'])
def first(message):
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Введите имя первого абонента')
        bot.register_next_step_handler(message, get_name1)
    elif message.text == 'Нет':
        bot.send_message(message.from_user.id, 'Если захотите запустить, введите Да')
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю, введите Да или Нет')


def get_name1(message):
    global abonent1
    abonent1 = message.text
    bot.send_message(message.from_user.id, 'Имя первого абонента: ' + abonent1)
    bot.send_message(message.from_user.id, 'Введите имя второго абонента')
    bot.register_next_step_handler(message, get_name2)


def get_name2(message):
    global abonent2
    abonent2 = message.text
    bot.send_message(message.from_user.id, 'Имя второго абонента: ' + abonent2)
    bot.send_message(message.from_user.id, 'Введите целое число N для функции\nF(x)= N^x mod M')
    bot.register_next_step_handler(message, get_N)


def get_N(message):
    global N
    N = message.text
    try:
        int(N)
        bot.send_message(message.from_user.id, 'Введи целое число M для функции\nF(x)= N^x mod M')
        bot.register_next_step_handler(message, get_M)
    except:
        loop_for_N(message)


def loop_for_N(message):
    bot.send_message(message.from_user.id, 'Необходимо ввести целое число(!)\nПовторите ввод')
    bot.register_next_step_handler(message, get_N)


def get_M(message):
    global M
    M = message.text
    try:
        int(M)
        bot.send_message(message.from_user.id, abonent1 + ' и ' + abonent2 +
                         ' договорились о том, что число N будет равно ' + N +
                         ', а число M равно ' + M)
        bot.send_message(message.from_user.id, 'Введите случайное целое число p для абонента ' + abonent1 +
                         '\nФормула: P= N^p mod M')
        bot.register_next_step_handler(message, get_p)
    except:
        loop_for_M(message)


def loop_for_M(message):
    bot.send_message(message.from_user.id, 'Необходимо ввести целое число(!)\nПовторите ввод')
    bot.register_next_step_handler(message, get_M)


def get_p(message):
    global p
    global P
    p = message.text
    try:
        int(p)
        P = pow(int(N), int(p)) % int(M)
        bot.send_message(message.from_user.id, 'Число P по формуле будет равно'+
                         '\nP= ' + N + '^' + p + ' mod ' + M + '= ' + str(P))
        bot.send_message(message.from_user.id, abonent1 + ' отправляет абоненту ' +
                         abonent2 + ' число P ')
        bot.send_message(message.from_user.id, ' Введите случайное целое число r для абонента ' + abonent2 +
                         '\nФормула: R= N^r mod M')
        bot.register_next_step_handler(message, get_r)
    except:
        loop_for_p(message)


def loop_for_p(message):
    bot.send_message(message.from_user.id, 'Необходимо ввести целое число(!)\nПовторите ввод')
    bot.register_next_step_handler(message, get_p)


def get_r(message):
    global r, R
    global K1, K2
    r = message.text
    try:
        int(r)
        R = pow(int(N), int(r)) % int(M)
        bot.send_message(message.from_user.id, 'Число R по формуле будет равно' +
                         '\nR= ' + N + '^' + r + ' mod ' + M + '= ' + str(R))
        bot.send_message(message.from_user.id, abonent2 + ' отправляет абоненту ' +
                         abonent1 + ' число R')

        K1 = pow(int(R), int(p)) % int(M)
        K2 = pow(int(P), int(r)) % int(M)
        bot.send_message(message.from_user.id, abonent1 + ' вычисляет K1 по формуле:' +
                         '\nK1= R^p mod M' +
                         '\nK1= ' + str(R) + '^' + p + ' mod ' + M + '= ' + str(K1))
        bot.send_message(message.from_user.id, abonent2 + ' вычисляет K2 по формуле:' +
                         '\nK1= P^r mod M' +
                         '\nK1= ' + str(P) + '^' + r + ' mod ' + M + '= ' + str(K2))
        bot.send_message(message.from_user.id, 'K= K1= K2= ' + str(K1) +
                                               '\nПолучившееся значение K есть секретный ключ, '
                                               'который абоненты смогут использовать для расшифровки сообщений')
        bot.send_message(message.from_user.id, 'Вы хотите снова запустить алгоритм? (Да/Нет)')
    except:
        loop_for_r(message)


def loop_for_r(message):
    bot.send_message(message.from_user.id, 'Необходимо ввести число(!)\nПовторите ввод')
    bot.register_next_step_handler(message, get_r)


if __name__ == '__main__':
    bot.polling(none_stop=True)

