#code Misha Lytov
#версия 1.2
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random
import schedule
import requests
from skript_1_7 import main, pars_url # это подключения скрипта для парсинга
import time
import datetime
import os.path
from pathlib import Path # добавили библиотеку

i = 0

def cat_fun(message):

	#print('\nпользователь захотел посмотреть фотку кота')
		#id_ = message.from_user.id
		#print('ID:',id_)
		#first_name_ = message.from_user.first_name
		#print('first_name:',first_name_)
		#last_name_ = message.from_user.last_name
		#print('last_name:',last_name_)
		#ser_name = message.from_user.username
		#print('last_name:',user_name)
	lines = []
	rand_i = 0
		#проверим есть ли файл, если его нету, то создаем
	proverka = os.path.exists('cat.txt')
	
	
	if proverka == True:
		rand_i = 0
	else:
		file = open('cat.txt','a')
		file.close
		main()
		time.sleep(2)

	size_cat_txt = int(Path('cat.txt').stat().st_size)#тут проверяем, что файл не пустой 
	if size_cat_txt <= 10:
		main()
		rand_i = 0
		#проверим есть ли файл, если его нету, то создаем
	

	size_cat_txt = int(Path('cat.txt').stat().st_size)#тут проверяем, что файл не пустой 
	if size_cat_txt <= 10:
		main()

		#with open('cat.txt') as file:
			#for line in file:
			#	rand_i += 1
		#	rand_i = 0
		#file.close 
		#if rand_i == 0:
		#	print('running parser_cat')
		#	main()
		#	with open('cat.txt') as file:
		#		for line in file:
		#			rand_i += 1
		#	file.close 
		#print(rand_i)

		#photo_cat = random.randint(1,rand_i)
		#print(photo_cat)
		#with open('cat.txt') as file:
		#	lines = file.readlines()
		#file.close
		#bot.send_photo(message.chat.id, photo = lines[photo_cat])

		#рандомная строка 
	with open('cat.txt') as file:
		for line in file:
			lines.append(line)
	random_cat_photo = random.choice(lines)
	bot.send_photo(message.chat.id, photo = random_cat_photo)
	global i
	i += 1
	if i >= 200 :
		bot.send_message(message.chat.id, 'коты козлы')
		print('running parser_cat')
		main()
		time.sleep(2)
		i = 0



def slovar(name_goroskob):

	if name_goroskob == 'Овен' or name_goroskob == 'овен':
		name_goroskob = 'aries'
	elif name_goroskob == 'Телец' or name_goroskob == 'телец':
		name_goroskob = 'taurus'
	elif name_goroskob == 'Близнецы' or name_goroskob == 'близнецы':
		name_goroskob = 'gemini'
	elif name_goroskob == 'Рак' or name_goroskob == 'рак':
		name_goroskob = 'cancer'
	elif name_goroskob == 'Дева' or name_goroskob == 'дева':
		name_goroskob = 'virgo'
	elif name_goroskob == 'Весы' or name_goroskob == 'весы':
		name_goroskob = 'libra'
	elif name_goroskob == 'Лев' or name_goroskob == 'лев':
		name_goroskob = 'leo'
	elif name_goroskob == 'Скорпион' or name_goroskob == 'скорпион':
		name_goroskob = 'scorpio'
	elif name_goroskob == 'стрелец' or name_goroskob == 'Стрелец':
		name_goroskob = 'sagittarius'
	elif name_goroskob == 'Козерог' or name_goroskob == 'козерог':
		name_goroskob = 'capricorn'
	elif name_goroskob == 'Водолей' or name_goroskob == 'водолей':
		name_goroskob = 'aquarius'
	elif name_goroskob == 'Рыбы' or name_goroskob == 'рыбы':
		name_goroskob = 'pisces'
	else:
		name_goroskob = ''
	





	return name_goroskob
def parser_goroskob(name_goroskob):
	#https://1001goroskop.ru/?znak=aries
	url = "https://1001goroskop.ru/?znak=" + slovar(name_goroskob)
	print(url)
	headers = {
			"Accept": "*/*",
			"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
	}
	req = requests.get(url, headers=headers)
	src = req.text
	with open("page.html", "w") as file:
		file.write(src)

	with open("page.html") as file:
		src = file.read()

	soup = BeautifulSoup(src, "lxml")
	text_page = soup.find(class_="eje_block").find("p")
	return text_page


def goroskob(message):
	#раньше тут писалось время и основная информация про пользователя
	#now = datetime.datetime.now() 
	#print("Current date and time: ") 
	#print(now.strftime('%Y-%m-%d %H:%M:%S')) 
	#print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
	#print('\nпользователь захотел узнать свой гороскоп')
	#id_ = message.from_user.id
	#print('ID:',id_)
	#first_name_ = message.from_user.first_name
	#print('first_name:',first_name_)
	#last_name_ = message.from_user.last_name
	#print('last_name:',last_name_)
	#user_name = message.from_user.username
	#print('last_name:',user_name)


	name_goroskob = message.text
	if name_goroskob  == 'текила' or name_goroskob == 'Текила':
		#print('пользователь узнал про посхалку')
		#print('https://www.instagram.com/misha_fama/')
		bot.send_message(message.chat.id, 'https://www.instagram.com/misha_fama/\n пить текилу и не задавать вопросов ')
		bot.send_photo(message.chat.id, 'https://cdngallery.adonismale.com/monthly_2020_01/large.VueContropostoPoster.jpg.ca82f132ae8f95555dff0c96051b9ae0.jpg')#https://cdngallery.adonismale.com/monthly_2020_01/large.VueContropostoPoster.jpg.ca82f132ae8f95555dff0c96051b9ae0.jpg
		time.sleep(2)
	if name_goroskob == 'Бит' or name_goroskob == 'бит':
		print('посхалка обнаружена"степа"')
		bot.send_message(message.chat.id, 'https://vk.com/stpxbeatstore\nлучшие биты тут ')

 #Отсылаем юзеру сообщение в его чат
	if ((name_goroskob == 'весы') or (name_goroskob == "Весы")):
		text = 'от создателя \n весы как обычно прекрасны\n а теперь ваш гороскоп'
		bot.send_message(message.chat.id, text)
	elif ((name_goroskob == 'Лев') or (name_goroskob == 'лев')):
 		text = 'https://instagram.com/antivanil_?utm_medium=copy_link\n если не работает, то он виноват'

 		bot.send_message(message.chat.id, text)
	text = parser_goroskob(name_goroskob)
	if slovar(name_goroskob) == '':
		name_goroskob = 'ты видимо не правильно написал свой знак, но не грусти, ты долбаеб, но смотри общий гороскоб'
		bot.send_message(message.chat.id, name_goroskob)
	bot.send_message(message.chat.id, text)

# цитаты
#def quotes(message):
#
#	lines = []
#		#проверим есть ли файл, если его нету, то создаем
#	proverka = os.path.exists('quotes.txt')
#	
#	if proverka == True:
#		if int(Path('quotes.txt').stat().st_size) > 0:
#			with open('quotes.txt') as file:
#				for line in file:
#					lines.append(line)
#			random_quotes = random.choice(lines)
#			bot.send_message(message.chat.id, random_quotes.split('\n'))
#		else:
#			return 0
#			
#	else:
#		bot.send_message(message.chat.id, 'цитат нету')
#		return 0
		
		


bot = telebot.TeleBot('5296390006:AAGsFOm6Fl3DRxTM0uyCWLzeFdkGDgyBz8U')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("гороскоп")
	item2=types.KeyboardButton("котики")
	item3=types.KeyboardButton("цитаты(нету ещё)")
	item4=types.KeyboardButton("бубенцы звенят(разработка)")
	markup.add(item1)
	markup.add(item2)
	markup.add(item3)
	markup.add(item4)
	
	bot.send_message(m.chat.id, 'Создатели бота:\n Лытов Михаил\n Фомин Михаил\n при поддержке Аркадия Иванова',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
	goroskob_znak = {'nовен','телец','близнецы','рак','лев','дева','весы','скорпион','стрелец','козерог','водолей', 'рыбы'}
	if message.text.strip() == 'гороскоп':
		bot.send_photo(message.chat.id, photo = 'https://tvcenter.ru/wp-content/uploads/2021/07/1.png')#https://tvcenter.ru/wp-content/uploads/2021/07/1.png
		#text = 'чтобы узнать свой гороскоп на сегодня, то напиши свой знак задиака\nовен\nтелец\nблизнецы\nрак\nлев\nдева\nвесы\nскорпион\nстрелец\nкозерог\nводолей\nрыбы'
		#bot.send_message(message.chat.id, text)
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1=types.KeyboardButton("овен")
		item2=types.KeyboardButton("телец")
		item3=types.KeyboardButton("близнецы")
		item4=types.KeyboardButton("рак")
		item5=types.KeyboardButton("лев")
		item6=types.KeyboardButton("дева")
		item7=types.KeyboardButton("весы")
		item8=types.KeyboardButton("скорпион")
		item9=types.KeyboardButton("стрелец")
		item10=types.KeyboardButton("козерог")
		item11=types.KeyboardButton("водолей")
		item12=types.KeyboardButton("рыбы")
		markup.add(item1,item2)
		markup.add(item3,item4)
		markup.add(item5,item6)
		markup.add(item7,item8)
		markup.add(item9,item10)
		markup.add(item11,item12)

		bot.send_message(message.chat.id, 'чтобы узнать свой гороскоп на сегодня, то выбери свой знак задиака',  reply_markup=markup)
		#bot.register_next_step_handler(message,goroskob)
	elif message.text.strip() == 'котики':#КОТИКИ
		cat_fun(message)
	elif message.text.strip() in goroskob_znak:
		#bot.register_next_step_handler(message,goroskob)
		goroskob(message)
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1=types.KeyboardButton("гороскоп")
		item2=types.KeyboardButton("котики")
		item3=types.KeyboardButton("цитаты(нету ещё)")
		item4=types.KeyboardButton("бубенцы звенят(разработка)")
		markup.add(item1)
		markup.add(item2)
		markup.add(item3)
		markup.add(item4)
		bot.send_message(message.chat.id, 'что дальше?',  reply_markup=markup)
	#elif message.text.strip() == 'цитаты':
	#	quotes(message)		



#def send_photo_file_url(chat_id,text):
#	bot.send_photo(c.chat_id, photo=('1.jbg'))




#schedule.every(1).minutes.do(main)
#while True:


#	schedule.run_pending()

bot.polling(none_stop=True, interval=0)
