import requests
from app import app


def goget():
    pre = "http://"
    port = ":" + app.config['HOSTPORT']
    endpoint = "/api/LiveData.xml"

    url = pre + app.config['HOST'] + port + endpoint

    payload = ""
    headers = {
        'cache-control': "no-cache",
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    response.raw.decode_content = True
    return response.text
