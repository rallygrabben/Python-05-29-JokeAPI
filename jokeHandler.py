import requests
import datetime

class jokeHandler:
    def __init__(self, address, JSONStringExt):
        self.address = address
        self.JSONStringExt = JSONStringExt
        
        # now = datetime.datetime.now()

        # print(f'[{now}]: Constructor Runtime')

    def getJoke(self):
        req = requests.get(self.address)
        jsonData = req.json()
        APIRespons = jsonData[self.JSONStringExt]
        
        # now = datetime.datetime.now()

        # print(f'[{now}]: getJoke runtime')

        return APIRespons