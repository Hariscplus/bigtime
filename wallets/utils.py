from bitcoinlib.wallets import Wallet
from web3 import Web3
import requests

BLOCKCYPHER_API_TOKEN = 'your_blockcypher_api_token'

def generate_bitcoin_wallet():
    wallet = Wallet.create('TemporaryWallet')
    address = wallet.get_key().address
    private_key = wallet.get_key().private_hex
    wallet.delete()
    return address, private_key

def generate_ethereum_wallet():
    w3 = Web3()
    account = w3.eth.account.create()
    return account.address, account.key.hex()

def register_blockcypher_webhook(wallet_address, callback_url):
    url = f"https://api.blockcypher.com/v1/btc/main/hooks?token={BLOCKCYPHER_API_TOKEN}"
    data = {
        "event": "confirmed-tx",
        "address": wallet_address,
        "url": callback_url
    }
    response = requests.post(url, json=data)
    if response.status_code != 201:
        raise Exception(f"Failed to register webhook: {response.json()}")
    return response.json()