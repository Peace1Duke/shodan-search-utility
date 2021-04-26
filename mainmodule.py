from sys import platform
from shodan import Shodan
import shodan
import os

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	print (f"""
{re}   ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄       ███▄    █    {cy} ▄████▄   ▄▄▄       ███▄ ▄███▓   
{re} ▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄     ██ ▀█   █    {cy}▒██▀ ▀█  ▒████▄    ▓██▒▀█▀ ██▒   
{re} ░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒   {cy}▒▓█    ▄ ▒██  ▀█▄  ▓██    ▓██░   
{re}   ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒   {cy}▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██    ▒██    
{re} ▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒▒██░   ▓██░   {cy}▒ ▓███▀ ░ ▓█   ▓██▒▒██▒   ░██▒   
{re} ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒    {cy}░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ░  ░   
{re} ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░   {cy}  ░  ▒     ▒   ▒▒ ░░  ░      ░   
{re} ░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒      ░   ░ ░    {cy}░          ░   ▒   ░      ░      
{re}       ░   ░  ░  ░    ░ ░     ░          ░  ░         ░    {cy}░ ░            ░  ░       ░      
{cy}  by Peace Duke	    {re}░                              ░                                
{gr}  ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██                                         
{gr}▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒                                        
{gr}░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░                                        
{gr}  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██                                         
{gr}▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓                                        
{gr}▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒                                        
{gr}░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░                                        
{gr}░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░                                        
{gr}  ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░                                 
{gr}                              ░                                     
	""")

#custom error
class Error(Exception):
    pass

class NotLinux(Error):
    pass

def checkOS():
	try:
		if platform == "linux" or platform == "linux":
			...
		else: 
			raise NotLinux
	except NotLinux:
		print("This script is for Linux only!")
		print()

#auxiliary functions
def exit():
	answ = str(input(f"""{cy}>Do you want to exit?(y/different key): """))
	if answ.lower() in ['y', 'yes']:
		sys.exit()
	else: 
		...


#the actual search function
def search(arg):
	country = str(input(f"""{gr}>Input the country you are interested in(just Enter for all countries): """))
	if country == "  ":
		...
	else: 
		arg = arg +',country:' + country
	try:
        # Search Shodan
		results = api.search(arg)

        # Show the results
		for result in results['matches']:
				print('IP: {}'.format(result['ip_str']))
				print(result['data'])
				print('')
		exit()
	except shodan.APIError:
		print('Api Error ')
		exit()


def cam():
	print(f"""{re}!exploit with /system.ini?loginuse&loginpas! """)
	search('realm="GoAhead", domain=":81"') 
	

def asus_ftp():
	print(f"""{re}! exploit withftp://XXX.XXX.XXX.XXX! """)
	search('asus 230 port:"21"') 
	

def hacked_site():
	search('http.title:"hacked by"')

#list function 

def list():
	print(f"""
{gr}1: cam,
2: asus_ftp,
3: hacked_site
    	""")
	numeth = int(input(">Input the number of the method you need:"))
	choose_list(numeth)

def choose_list(arg):
    switcher = {
        1: cam,
        2: asus_ftp,
        3: hacked_site
    }
    non_existent_arg = switcher.get(arg, lambda:"Invalid number!")
    print (non_existent_arg())




#functions for initialization
def shodan_init():
	with open('config.txt') as f:
		key = f.read()
		f.close()
	global api 
	api = Shodan(key)


    
def key_shodan():
	if os.path.isfile('config.txt') == False or os.stat("config.txt").st_size == 0:
		key = str(input(f"""{gr}>Input your api key: """))
		f = open("config.txt", "w+")
		f.write(key)
		shodan_init()
	else: 
		answ = str(input(f"""{cy}>Do you want to use a different api key?(y/different key): """))
		if answ.lower() in ['y', 'yes']:
			key = str(input(f"""{gr}>Input your api key: """))
			f = open("config.txt", "w+")
			f.seek(0)
			f.write(key)
			shodan_init()
		else: 
			shodan_init()



    

	



	
