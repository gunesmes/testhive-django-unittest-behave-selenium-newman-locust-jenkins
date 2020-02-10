from behave import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os


def before_scenario(context, scenario):
	options = Options()
	options.add_argument("--headless") 					# Runs Chrome in headless mode.
	options.add_argument('--no-sandbox') 				# Bypass OS security model3
	options.add_argument('--disable-infobars')
	options.add_argument('--disable-extensions')
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-dev-shm-usage')

	if os.environ['BROWSER'] == 'web':
		options.add_argument('start-maximized')
	elif os.environ['BROWSER'] == 'iphoneX':
		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
		options.add_argument('--window-size=1125,2436')
		options.add_argument(f'--user-agent={user_agent}')
	elif os.environ['BROWSER'] == 'iphone6':
		user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
		options.add_argument('--window-size=375,667')
		options.add_argument(f'--user-agent={user_agent}')
	elif os.environ['BROWSER'] == 'pixel2':
		user_agent = "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
		options.add_argument('--window-size=1080,1920')
		options.add_argument(f'--user-agent={user_agent}')

	context.browser = webdriver.Chrome(chrome_options=options)

	
def after_scenario(context, scenario):
	print("\n")
	context.browser.quit()
