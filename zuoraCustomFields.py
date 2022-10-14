import http.client
import json

conn = http.client.HTTPSConnection("rest.apisandbox.zuora.com")
payload = ''
headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'Authorization': 'Bearer bc3e07c105c74d2d8cc9cbf043f91e0a'
}
conn.request("GET", "/settings/custom-fields/zuora", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))