import http.client
from xml.etree.ElementTree import fromstring, ElementTree


def getInfo():
    conn = http.client.HTTPConnection('71.115.207.180', 8880, 5)
    payload = ""
    headers = {
        'cache-control': "no-cache",
    }

    conn.request("GET", "/api/LiveData.xml", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    tree = ElementTree(fromstring(data))
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)


def main():
    getInfo()


if __name__ == '__main__':
    main()
