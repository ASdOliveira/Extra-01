"""
File that will load the configurations at conf.json
"""
import json
import os

f = open(str(os.path.dirname(os.path.abspath(__file__))) + "\conf.json" )

data = json.load(f)

TELEGRAM_TOKEN = data['TELEGRAM_TOKEN']
API_BASE = data['API_BASE']
TELEGRAM_BOT_NAME = data['TELEGRAM_BOT_NAME']    
TELEGRAM_CHAT_ID = data['TELEGRAM_CHAT_ID']
