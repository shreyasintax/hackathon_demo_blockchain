from web3 import Web3
from ocr import extractDetails;

name, birth_date = extractDetails()

# Connect to the local blockchain (Ganache)
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


# Verify connection
if not web3.is_connected():
    raise Exception("Failed to connect to the blockchain")

# Set the default account (use the first account provided by Ganache)
web3.eth.default_account = web3.eth.accounts[0]

# Contract address and ABI (replace with your actual values)
contract_address = "0xeaAA15701b60730A5D82c6Ce49424B979f8aF835"  # Replace with your contract address
contract_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_name", "type": "string"},
            {"name": "_birthDate", "type": "string"},
        ],
        "name": "storeKYC",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "_user", "type": "address"}],
        "name": "getKYC",
        "outputs": [
            {"name": "", "type": "string"},
            {"name": "", "type": "string"},
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

# Instantiate the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def store_kyc(name, birth_date):
    tx_hash = contract.functions.storeKYC(name, birth_date).transact()
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"KYC data for {name} stored successfully!")

def get_kyc(user_address):
    kyc_data = contract.functions.getKYC(user_address).call()
    print(f"KYC Data: Name: {kyc_data[0]}, Birth Date: {kyc_data[1]}")



# Store KYC data (example)
store_kyc(name, birth_date)

# Retrieve KYC data for the first account
get_kyc(web3.eth.accounts[0])
