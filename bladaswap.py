import time
import ccxt
from termcolor import cprint
from web3 import Web3
import random
from decimal import Decimal

#проверяем РПЦ и проверяем баланс кошельков в SOL и его стоимость в USDC

def get_eth_usdc_price():
    exchange = ccxt.binance()  # Используем биржу Binance для получения курса
    market = exchange.load_markets()
    ticker = exchange.fetch_ticker('ETH/USDC')
    return ticker['last']  # Возвращает последнюю цену ETH/USDC

def check_balance(address, number, web3, eth_usdc_price):
    try:
        balance = web3.eth.get_balance(web3.toChecksumAddress(address))
        humanReadable = web3.fromWei(balance, 'ether')
        humanReadable_decimal = Decimal(str(humanReadable))  
        humanReadable = web3.fromWei(balance, 'ether')
        humanReadable_decimal = Decimal(str(humanReadable))# Преобразование в Decimal
        usd_balance = humanReadable_decimal * Decimal(eth_usdc_price)  
        umanReadable_decimal = Decimal(str(humanReadable))  
        humanReadable = web3.fromWei(balance, 'ether')
        cprint(f'{number}. {address} : {humanReadable} ETH / {usd_balance:.2f} USDC', 'white')
        return humanReadable_decimal

    except Exception as error:
        cprint(f'{number}. {address} = {error}', 'red')
        return Decimal(0)00

if __name__ == "__main__":
    
    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]

    # RPC = 'https://mainnet.optimism.io'
    # RPC = 'https://bsc-dataseed.binance.org'
    # RPC = 'https://polygon-rpc.com'
        # RPC = 'https://mainnet.optimism.io'
    # RPC = 'https://bsc-dataseed.binance.org'
    # RPC = 'https://polygon-rpc.com'
    # RPC = 'https://arb1.arbitrum.io/rpc'
    web3 = Web3(Web3.HTTPProvider(RPC))
    total_eth_balance = Decimal(0)
    eth_usdc_price = get_eth_usdc_price()  # Получаем текущий курс ETH/USDC

    cprint('\a\n/// start check balance...', 'white')
    number = 0
    for wallet in wallets_list:
        address = web3.toChecksumAddress(wallet)
        number = number + 1
        balance = check_balance(address, number, web3, eth_usdc_price)  # Проверяем баланс и получаем его в ETH
        total_eth_balance += balance
        
#sosathui dupa
    cprint(f'\a\n/// Проверка завершена. Итоговый баланс всех кошельков: {total_eth_balance} ETH', 'green')

