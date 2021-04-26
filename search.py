import os
from sys import platform
import requests
import mainmodule
from shodan import Shodan

mainmodule.banner()
mainmodule.checkOS()

while True:
	mainmodule.key_shodan()

	mainmodule.list()


