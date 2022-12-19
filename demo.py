import requests
import sys
from main import *
from termcolor import colored
test = requests.post(url = 'http://127.0.0.1:8000/scanner', json = {'contract_key' : 'smart-contracts/denial-of-service.sol', 'pragma' : '0.8.12'})
print(test, test.json())

final = requests.post(url = 'http://127.0.0.1:8000/vulnerable',  json={'contract_key' : 'smart-contracts/denial-of-service.sol', 'pragma' : '0.8.11'})
print(final, final.json())

print(colored('High Severity Vulnerabilities\n', 'red'))
for issue in final.json()['high_severity']:
    print("Type:", colored(issue['check'], 'red'))
    print(colored(issue['description'], 'red'))
``
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
