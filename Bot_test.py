# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5374259299:AAEQ1T0N4NYXLJ6OdoqbwupVl15DXooX8nw')


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('Website')
#     start = types.KeyboardButton('Start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Check to website', reply_markup=markup)

# # @bot.message_handler(content_types=['text'])
# # def ger_user_text(message):
# #     if message.text == 'Hello' or 'hi, HI, Hi, hello':
# #         bot.send_message(message.chat.id, "and hello to you!", parse_mode='html')
# #     elif message.text == 'id':
# #         bot.send_message(message.chat.id, f"Your id: {message.from_user.id}", parse_mode='html')
# #     elif message.text == 'photo':
# #         photo = open('icon.png', 'rb')
# #         bot.send_photo(message.chat.id, photo)
# #     else:
# #         bot.send_message(message.chat.id, "I don't understand you!", parse_mode='html')

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Oh, it\'s cool photo')


# @bot.message_handler(commands=['Website'])
# def website(message):
#     markap= types.InlineKeyboardMarkup()
#     markap.add(types.InlineKeyboardButton('Visit to Website', url='https://google.com'))
#     bot.send_message(message.chat.id, 'Check to Website', reply_markup=markap)



# bot.polling(none_stop=True)