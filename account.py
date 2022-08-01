import os

from dotenv import load_dotenv
import bitget.mix.account_api as accounts

load_dotenv(".env")

class Account(object):
    def __init__(self):
        self.api = self.get_account_api()
        self.symbol = "BTCUSDT_UMCBL"

    def get_balance(self):
        return self.api.account(self.symbol, "USDT")["data"]["available"]

    def get_account_api(self):
        api_key = os.getenv("API_KEY")
        secret_key = os.getenv("SECRET_KEY")
        passphrase= os.getenv("PASSPHRASE")

        return accounts.AccountApi(api_key, secret_key, passphrase, use_server_time=False, first=False)