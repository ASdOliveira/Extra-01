"""
Parse a json
1 - Parse a json to a dict
2 - Parse a json to a specific object
"""
import json

def ToDict(InputString):
    return json.loads(InputString)