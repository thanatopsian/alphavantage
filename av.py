import requests
import os


class AVClient:

    def __init__(self):
        self.url = "https://www.alphavantage.co/query"
        self.key = os.getenv("AV_KEY")
    
    def params(self, function: str, **kwags):
        params = {"apikey": self.key, "function": function}
        for k, v in kwags:
            params[k] = v

        return params

    def top_gain_loss(self) -> dict:
        params = self.params(function="TOP_GAINERS_LOSERS")
        req = requests.get(url=self.url, params=params)

        return req.json()
