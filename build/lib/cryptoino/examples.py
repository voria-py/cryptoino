'''
some examples of using crypto_info
'''

from cryptoino import Coin

# Get list of all supported coins
# print(Coin.get_coin_list())

# Get list of suppurted terget currency
# print(Coin.get_target_currency())



# Get bitcoin info
bitcoin = Coin(name="bitcoin" , target_currency="usd")
print("Current btc price:" , bitcoin.get_current_price() , "USD") # Get current price
print("24h change:", bitcoin.get_price_change_percentage_24h() ,"%") # Get 24h change percentage


# Get dogecoin info
doge = Coin(name="dogecoin" , target_currency="usd")
print("Current btc price:", doge.get_current_price(),"USD") # Get current price
print("24h change:", doge.get_price_change_percentage_24h(),"%") # Get 24h change percentage


