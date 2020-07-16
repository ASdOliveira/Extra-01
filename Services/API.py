"""
File that aims to requests Data from an API
"""
import requests
#import Tools.JsonHandling as jeison

URL = "http://api.open-notify.org/iss-now.json"

try:
    response = requests.get(URL)
    if response.status_code == 200:
    #    print(jeison(response.content))
    else:
        raise Exception("Problem to access API. Status code: {0}".format(response.status_code))

except Exception as ex:
    print(ex)
