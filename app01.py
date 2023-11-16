# 1. Import module
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# 2. Set web3 module
infura_url = os.environ['infura_url']
web3 = Web3(Web3.HTTPProvider(infura_url))

# 3. Print Connection check
print(web3.is_connected())

# 4. Get Block Number
print(web3.eth.block_number)

# 5. Print account balances
account = "0xF60fB76e6AD89364Af3ffE72C447882bFe390331"
balance = web3.eth.get_balance(account)
print(web3.from_wei(balance, "ether"))
