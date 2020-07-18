"""
File that should run the aplication, and connect other services.
"""

import Services.API as api 
import Services.Bot as bot
from datetime import datetime

def Main():
    """Function That starts the service"""
    
    print("Starting...")
    data = api.Get()
    stringData = "Posicao ISS: "
    stringData = stringData + "latitude:" + str(data['iss_position']['latitude'])
    stringData = stringData + " longitude:" + str(data['iss_position']['longitude'])
    stringData = stringData + " hora:" + str(datetime.fromtimestamp(data['timestamp']))
    print (stringData)
    status = bot.SendMessage(stringData)

    print(status)