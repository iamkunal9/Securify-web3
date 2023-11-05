from web3 import Web3

def getByteCode(address,chain):
    rpc = ""
    if chain.lower()=='eth':
        rpc="https://eth.meowrpc.com"
    elif chain.lower()=='bsc':
        rpc="https://bsc-dataseed1.binance.org/"
        
    w3 = Web3(Web3.HTTPProvider(rpc))
    address2 = Web3.to_checksum_address(address)
    ugly_bytecode = w3.eth.get_code(address2)
    bytecode = w3.to_hex(ugly_bytecode)
    return f"{bytecode}"