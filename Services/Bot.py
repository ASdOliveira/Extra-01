"""
this file will send the message to telagram
"""
import requests
import Services.Conf.Settings as settings

def SendMessage(bot_message):
    """Send the message('bot_message') to telegram
        The settings of telegram are in Conf folder"""
        
    bot_token = settings.TELEGRAM_TOKEN
    bot_chatID = settings.TELEGRAM_CHAT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.post(send_text)
    #response = response.json()

    #return response['ok']
    return response.json()

## https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e