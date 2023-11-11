from hashlib import sha256

lz = 5
name = '1337speak'
attempts = 1
prefix = '0' * lz

while True:
    if (hash_ := sha256(f'{name}{attempts}'.encode()).hexdigest()).startswith(prefix):
        print(f'Password: {name}{attempts}')
        print(f'Proof of Work: {hash_}\n')
    attempts += 1