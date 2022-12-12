import requests
import sys
from main import *

posty = {
    'id' : 100,
    'name' : 'Jay'
}

test = requests.post(url = 'http://127.0.0.1:8000/getInformation', json=posty)
print(test, test.json())

