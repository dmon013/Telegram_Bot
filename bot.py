import telebot
import webbrowser

bot = telebot.TeleBot('6772074838:AAFViOGI04RghQZW5CbJZjwEDxV7ZpoIGLE')
API = 'a6cf66576f0fa27098bb644771d04bc8'


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['video'])
def cute_video(message):
    img = open('files/😊🦋.mp4', 'rb')
    bot.send_video(message.chat.id, img, None, '😊🦋', message.message_id)
    img.close()

@bot.message_handler(content_types=['video'])
def get_video(message):
    bot.reply_to(message, 'Хороший видеоролик!')

@bot.message_handler()
def into(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет', {})
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.infinity_polling()