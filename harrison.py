import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=usd&from=eur&amount=5"

payload = {}
headers= {
  "apikey": "52NPDB88iMqL86HWTtJi4LvPYgwmL54H"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)



