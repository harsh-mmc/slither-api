import requests
import sys
from main import *
from termcolor import colored

contract_name = sys.argv[1]
content = ''
with open(contract_name) as f:
    content = f.read()
print(content)
prag = str(re.findall('\d{1,2}\.\d{1}\.\d{1,2}', content)[0])
print(prag)

test = requests.get(url='http://127.0.0.1:8000')
datatest = test.json()
print(datatest)

testContract = Contract(sol_contract=content, pragma=prag)
print("Type of testContract object is", type(testContract))
#print(testContract.sol_contract, testContract.pragma)
r = requests.post(url = 'http://127.0.0.1:8000/scanner',  json={'sol_contract' : content, 'pragma' : prag})
#print(r.url)
print(r, r.json())

r2 = requests.post(url = 'http://127.0.0.1:8000/items', json={'sol_contract' : content, 'pragma' : prag})
#print(r2.url)
print(r2.json())

final = requests.post(url = 'http://127.0.0.1:8000/vulnerable',  json={'sol_contract' : content, 'pragma' : prag})
print(final, final.json())

print(colored('High Severity Vulnerabilities\n', 'red'))
for issue in final.json()['high_severity']:
    print("Type:", colored(issue['check'], 'red'))
    print(colored(issue['description'], 'red'))

print(colored('Meduim Severity Vulnerabilities\n', 'yellow'))
for issue in final.json()['medium_severity']:
    print("Type:", colored(issue['check'], 'yellow'))
    print(colored(issue['description'], 'yellow'))

print(colored('Low Severity Vulnerabilities\n', 'green'))
for issue in final.json()['low_severity']:
    print("Type:", colored(issue['check'], 'green'))
    print(colored(issue['description'], 'green'))

print(colored('Informational Vulnerabilities\n', 'green'))
for issue in final.json()['informational']:
    print("Type:", colored(issue['check'], 'green'))
    print(colored(issue['description'], 'green'))

"""out = requests.post(url = 'http://127.0.0.1:8000/output', json=final.json())
print(out, out.url)
print(out.text)"""
