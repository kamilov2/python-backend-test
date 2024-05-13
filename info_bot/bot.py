import telebot

token = '5139803451:AAF3a9qiOqpa2pmNETS_QuMQZKOmxuGZLF8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
#   print(message)
#   print(dir(message))
  print(message.from_user)  
  bot.send_message(message.chat.id,"Привет ✌️ ")

bot.infinity_polling()