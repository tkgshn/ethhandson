# 1. Import Module
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# 2. Access Ganache local server
ganache_url = "http://127.0.0.1:7545" #Ganacheに書いてる
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 3. Account Address, private key
SENDER_ADDRESS = '0x2CF156E39f498c21AD315B54088Cf9c2c46B51C3'  # Input selected Address
TAEGET_ADDRESS = '0xF60fB76e6AD89364Af3ffE72C447882bFe390331'  # Input selected Address
PRIVATE_KEY = os.environ['private_key']  # Input selected Address's private key

# 4. Get nonce value
nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)

# 5. Transaction data
tx = {
    'nonce': nonce,
    'to': TAEGET_ADDRESS,
    'value': web3.to_wei(1, 'ether'),  # 送金量(1 ETH)
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}

# 6. Generate singed transaction data
signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

# 7. Ethereum Transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# 8. Check Transaction address
print("transaction id", web3.to_hex(tx_hash))
