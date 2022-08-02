'''
Cryptoino
Crypto info module
By: https://amirkho.ir
github: https://github.com/amirkho-py
instagram: https://instagram.com/amirkho.ir

'''


import requests


class Coin:
    '''
    1- set name to one of coin list item. to access list use get_coin_list() method.\n
    2- set target_currency to one of target_currency list item. to access list use get_target_currency method.
    '''


    @classmethod
    def get_coin_list(cls):
        '''
        to get list of supported coin names
        '''
        coin_list_request = requests.get("https://api.coingecko.com/api/v3/coins/list").json()
        coin_list_name = []
        for coin in range(12000):
            coin_list_name.append(coin_list_request[coin]['id'])
        return coin_list_name


    @classmethod
    def get_coin_symbol(cls):
        '''
        to get list of supported coin symbols
        '''
        coin_list_symbol_request = requests.get("https://api.coingecko.com/api/v3/coins").json()
        coin_list_symbol = []
        for x in range(12000):
            coin_list_symbol.append(coin_list_symbol_request[x]['symbol'])
        return coin_list_symbol


    @classmethod
    def get_target_currency(cls):
        '''
        to get list of supported target currency list
        '''
        target_currency_request = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin").json()
        target_currency_json = target_currency_request['market_data']['current_price']
        target_currency_dict = dict(target_currency_json)
        target_currency_list = list(target_currency_dict.keys())

        return target_currency_list





    def __init__(self,name,target_currency):
        self.name = name
        self.target_currency = target_currency
        self.coin_full_data = requests.get(f"https://api.coingecko.com/api/v3/coins/{self.name}").json()




    def get_current_price(self):
        '''
        this method is for get current price. get_current_price()
        '''

        return self.coin_full_data['market_data']['current_price'][self.target_currency]




    def get_price_change_percentage_24h(self):
        '''
        this method is for get price_change_percentage_24h. get_price_change_percentage_24h()
        '''
        
        change_24h = float(self.coin_full_data['market_data']['price_change_percentage_24h'])
        if change_24h >= 0:
            change_24h = '+'+str(change_24h)
        else:
            change_24h = '-'+str(change_24h)

        return change_24h
        


