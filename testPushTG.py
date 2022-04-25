import telegram

chat_id = ''
token = ''

bot = telegram.Bot(token = token)

bot.send_message(chat_id = chat_id,text = 'test')