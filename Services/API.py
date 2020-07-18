"""
File that aims to requests Data from an API
"""
import requests
import Services.Tools.JsonHandling as JSON
import Services.Conf.Settings as settings
#from Conf.settings import API_BASE as URL

def Get():
    """Get a data from the API. \n
        Returns a dict."""
    try:
        response = requests.get(settings.API_BASE)
        if response.status_code == 200:
            return JSON.ToDict(response.content)
        else:
            raise Exception("Problem to access API. Status code: {0}".format(response.status_code))

    except Exception as ex:
        print(ex)