from sys import platform
import sys
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


#the actual search function
def search(arg):
	country = str(input(f"""{gr}>Input the country you are interested in('*' for all countries): """))
	if country == "*":
		...
	else: 
		arg = arg +',country:' + country
	try:
        # Search Shodan
		results = api.search(arg)

        # Show the results
		print('Results found: {}'.format(results['total']))
		for result in results['matches']:
				print('IP: {}'.format(result['ip_str']))
				print(result['data'])
				print('')
		exit()
	except shodan.APIError:
		print(f"""{re}Api Error """)
		exit()

#cams
def goahead():
	print(f"""{re}!exploit with /system.ini?loginuse&loginpas ! """)
	search('realm="GoAhead", domain=":81"')

def rtsp():
	print(f"""{re}!exploit with rtsp://XXX.XXX.XXX.XXX + public comand(check result) ! """)
	search('port:554 has_screenshot:true')

def yawcams():
	search('"Server: yawcam" "Mime-Type: text/html"')

def android_web():
	search('"Server: IP Webcam Server" "200 OK"')

def dvrs():
	search('html:"DVR_H264 ActiveX"')

def webcamxp7():
	search('("webcam 7" OR "webcamXP") http.component:"mootools" -401')

#industrial 
def samsung_billboards():
	search('"Server: Prismview Player"')

def gas_spc():
	search('"in-tank inventory" port:10001')

def alpr():
	search('P372 "ANPR enabled"')

def traffic_lc():
	search('mikrotik streetlight')

def tesla_chargstatus():
	search('http.title:"Tesla PowerPack System" http.component:"d3" -ga3ca4f2')

#remote acces
def adb_phone():
	print(f"""{re}! use with PhoneSploit ! """)
	search('android debug bridge product:”Android Debug Bridge”')

def vnc():
	search('"authentication disabled" "RFB 003.008"')

#ftp
def asus_ftp():
	print(f"""{re}! exploit withftp://XXX.XXX.XXX.XXX ! """)
	search('asus 230 port:21') 
	
def ftp():
	search('"220" "230 Login successful." port:21')

#printers
def hprinters():
	search('"Serial Number:" "Built:" "Server: HP HTTP"')

def canon1():
	search('"Server: KS_HTTP" "200 OK"')
def canon2():
	search('"Server: CANON HTTP Server"')

def xerox():
	search('ssl:"Xerox Generic Root"')
#other
def hacked_site():
	search('http.title:"hacked by"')

def octoprint_control():
	search('title:"OctoPrint" -title:"Login" http.favicon.hash:1307375944')

def etheriuminers():
	search('"ETH - Total speed"')

def north_korea():
	search('net:175.45.176.0/22,210.52.109.0/24,77.94.35.0/24')

def chromecast():
	search('"Chromecast:" port:8008')




#list function 

def list():
	print(f"""
{cy}!Cameras!
{gr}1: GoAhead cams
2: RTSP webcams
3: Yawcams
4: Android IP Webcam Server  	
5: Security DVRs
6: webcamXP/webcam7

{cy}!Industrial Control Systems!
{gr}7: Samsung Electronic Billboards
8: Gas Station Pump Controllers
9: Automatic License Plate Readers
10: Traffic Light Controllers / Red Light Cameras
11: Tesla PowerPack Charging Status

{cy}!Remote Desktop and Phone!
{gr}12: ADB Phone
13: Unprotected VNC

{cy}!FTP!
{gr}14: ASUS FTP Servers with Anonymous Login
15: FTP Servers with Anonymous Login

{cy}!Printers & Copiers!
{gr}16: HP Printers
17: Canon Printers 1
18: Canon Printers 2
19: Xerox Copiers/Printers

{cy}!Other!
{gr}20: Hacked Site
21: OctoPrint 3D Printer Controllers
22: Etherium Miners
23: Literally Everything in North Korea 
24:Chromecasts / Smart TVs

    	""")
	numeth = int(input(">Input the number of the method you need:"))
	choose_list(numeth)

def choose_list(arg):
    switcher = {
        1: goahead ,
        2: rtsp,
        3: yawcams,
        4: android_web,
        5: dvrs,
        6: webcamxp7,
        7: samsung_billboards,
        8: gas_spc,
        9: alpr,
        10: traffic_lc,
        11: tesla_chargstatus,
        12: adb_phone,
        13: vnc,
        14: asus_ftp,
        15: ftp,
        16: hprinters,
        17: canon1,
        18: canon2,
        19: xerox,
        20: hacked_site,
        21: octoprint_control,
        22: etheriuminers,
        23: north_korea,
        24: chromecast
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
#voobshche ne imeyu predstavleniya chego ono tam ne furichit s camerami i ftp
#predpolozhitelno oshibka v vizove api ili ehche chego
#cheknu zavtra, a ne segodnya s telefona

    

	



	
