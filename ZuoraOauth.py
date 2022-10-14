import http.client
import json

conn = http.client.HTTPSConnection("rest.apisandbox.zuora.com")
payload = 'client_id=7309fc67-b2d1-403d-baaa-5ab720fb0680&client_secret=%2FrlpO27%3D6cRfcQLym34Wae%2FMP9kxCbQQP59UCqj8d&grant_type=client_credentials'
headers = {
  'Authorization': 'Basic cm9oYW4ucm95Y2hvd2RodXJ5QHN5bnRoZXNpcy1zeXN0ZW1zLmNvbTpSb2hhbkAxOTk3',
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/oauth/token", payload, headers)
res = conn.getresponse()
data = res.read()
temp = json.loads(data.decode("utf-8"))
token = temp["access_token"]
