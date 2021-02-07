from hashlib import sha256
MAX_NONCE = 10000000

def SHA256(text):
    return sha256("abc".encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'* prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Cant find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions ='''
    nick -> walt -> 20,
    ernie -> jenna -> 45
    '''
    dificulty=1
    import time
    start = time.time()
    print("Start mining!")
    new_hash = mine(5,transactions,'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad',dificulty)
    total_time = str((time.time() - start))
    print(f"Done mining. Mining took: {total_time} seconds")

    print(new_hash)