import requests
from app import app


def goget():
    url = app.config['HOST']
    payload = ""
    headers = {
        'cache-control': "no-cache",
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    return response.text
