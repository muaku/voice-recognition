import requests
import json

APIKEY = "2e53434450454a54516a6261357443663750384a312e67325057744d516144323439416c6f636c77455041"
url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY={}".format(APIKEY)
payload = {
    "utt": "寿司を食べますか",
    "context": "",
    "nickname": "フクロウ",
    "nickname_y": "フクロウ",
    "sex": "女",
    "bloodtype": "B",
    "birthdateY": "1997",
    "birthdateM": "5",
    "birthdateD": "30",
    "age": "16",
    "constellations": "双子座",
    "place": "東京",
    "mode": "dialog",
}
req = requests.post(url, data=json.dumps(payload))
print (req.json())