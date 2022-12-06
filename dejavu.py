import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=usd&from=eur&amount=3"


payload = {}
headers= {
  "apikey": "52NPDB88iMqL86HWTtJi4LvPYgwmL54H"
}

requests.request("GET", url, headers=headers, data = payload)

status_code = response.status
print(status_code)
result = response.txt
print(result)