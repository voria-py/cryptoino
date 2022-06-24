# Crypto info module
A python module to get 12,000 cryptocurrencies information from coingecko
## Tech Stack
**Main Stack:** Python

**Packages/Modules:** request

## How to using?

Sure to have request module

Clone or download this project.

Import `crypto_info` to your project and use `Coin()` class


## using example

`from crypto_info import Coin`
<br>

`doge = Coin(name="dogecoin" , target_currency="usd")`
<br>

`print("Current btc price:", doge.get_current_price(),"USD")`


