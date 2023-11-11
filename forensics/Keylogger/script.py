import requests
from hashlib import sha256

url = 'http://mandf.csaw.io:4999/keylogger/'

# Generate params
lz = 5
attempts = 1
prefix = '0' * lz
name= "1337speak"
while True:
    if (hash_ := sha256(f'{name}{attempts}'.encode()).hexdigest()).startswith(prefix):
        # Replace 'param1' and 'param2' with the actual parameter names you need
        params = {
            'password': f'{name}{attempts}',
            'resultant_hash': hash_
        }

        print(f'Attempt : {name}{attempts}')

        # Send the POST request
        response = requests.post(url, data=params)

        # Print the response
        # print(response.text)

        if "csaw" in response.text:
            print(f'flag found with : {name}{attempts}')
            print(response.text)
            break

    attempts += 1

