import requests

class jokeHandler:
    def __init__(self, address, JSONStringExt):
        self.address = address
        self.JSONStringExt = JSONStringExt

    def getJoke(self):
        req = requests.get(self.address)
        jsonData = req.json()
        APIRespons = jsonData[self.JSONStringExt]
        
        return APIRespons