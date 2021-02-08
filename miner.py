from hashlib import sha256
# MAX_NONCE variable is number of times the loop runs to find the correct blockchain #
MAX_NONCE = 10000000
# SHA256 function is to encode the blockchain to read it in the terminal #
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
# mine function is to search for blockchain #
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value of: {nonce}")
            return new_hash
   # raising an exception so the loop doesnt run infinite number of times #
    raise BaseException(f"Cant find correct after trying {MAX_NONCE} times")

if __name__ == '__main__':
    transactions = '''
    nick -> walt -> 20,
    jenna -> ernie -> 45
    '''
    # dificulty variable is umber of zeros in blockchain #
    dificulty = 6
    # setting a timer to see how long it takes to find blockchains #
    import time
    start = time.time()
    print("Start mining!")
    new_hash = mine(5, transactions,'0000000ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad', dificulty )
    total_time = str((time.time() - start))
    print(f'Done mining! Mining took: {total_time} seconds!')
    print(new_hash)