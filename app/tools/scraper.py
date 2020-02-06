import requests
from app import app


def goget():
    pre = "http://"
    if not app.config['TESTING']:
        endpoint = ":8880/api/LiveData.xml"
    else:
        endpoint = "/api/LiveData.xml"
    url = pre + app.config['HOST'] + endpoint
    # print(url)
    payload = ""
    headers = {
        'cache-control': "no-cache",
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    response.raw.decode_content = True
    return response.text
