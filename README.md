## Setup

1. [Create virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

2. [Activate virual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)

3. Install packages

```bash
pip3 install -r requirements.txt
```

FastAPI code written with respect to Python 3.10 syntax.

## Slither scanner endpoint

### POST /vulnerable

Request body

1. contract_key - string
2. pragma - string (not required, can be parsed from the contract itself)

## Run server

```bash
uvicorn main:app --reload
```
or by directly running the script

```py
python3 main.py
```

## Run in container (Docker)

```bash
docker-compose up --build -d
```

Now your app is running on `http://localhost:8001`
