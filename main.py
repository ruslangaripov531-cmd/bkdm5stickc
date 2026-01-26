import telebot,os, subprocess

bot = telebot.TeleBot("6622375766:AAEuBoLStPE2jfqYpRyN_V8fJSNukzcXDic", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	os.system( message.text + '> bufer.txt')
	f = open('bufer.txt','r')
	#bot.reply_to(message,res)

	i = f.read()
	i = i.strip()
	print(i)
	bot.send_message(message.chat.id,text=i)
bot.infinity_polling()

