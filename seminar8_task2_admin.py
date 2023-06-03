import telebot


token = ''
bot = telebot.TeleBot(token)
data = open('text.txt', encoding='utf-8')
q = data.readlines()
data.close()
for question in q:
    current_question = question[0].split(':')
    q = q[0].split(':')
    answer = input(f'Вопрос: {current_question[1]}\nОтвет:')

    bot.send_message(current_question[0], answer)