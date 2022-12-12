import requests
import sys
from main import *

contract_name = sys.argv[1]
content = ''
with open(contract_name) as f:
    content = f.read()

test = requests.get(url='http://127.0.0.1:8000')
datatest = test.json()
print(datatest)

testContract = Contract(sol_contract=content, pragma='0.8.13')
print("Type of testContract object is", type(testContract))
print(testContract.sol_contract, testContract.pragma)
r = requests.post(url = 'http://127.0.0.1:8000/scanner',  json={'sol_contract' : content, 'pragma' : '0.8.13'})
#print(r.url)
print(r, r.json())

r2 = requests.post(url = 'http://127.0.0.1:8000/items', json={'sol_contract' : content, 'pragma' : '0.8.13'})
#print(r2.url)
print(r2.json())

