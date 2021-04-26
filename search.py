import os
from sys import platform
import requests
import mainmodule
from shodan import Shodan

mainmodule.banner()

while True:
	mainmodule.checkOS()

	mainmodule.key_shodan()

	mainmodule.list()


