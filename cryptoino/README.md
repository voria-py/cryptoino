# cryptoino module
A small python module to get 12,000 cryptocurrencies information from coingecko

## Tech Stack
**Main Stack:** Python

**Packages/Modules:** requests

## How to using?

Sure to have requests module

Clone or download this project.

Import `cryptoino` to your project and use `Coin()` class

or install using pip.

`pip install cryptoino`

## using example

`from cryptoino import Coin`
<br>

`doge = Coin(name="dogecoin" , target_currency="usd")`
<br>

`print("Current btc price:", doge.get_current_price(),"USD")`

## Compatibility
Successful test on:
- Python 3.7
- Python 3.8
- Python 3.10



