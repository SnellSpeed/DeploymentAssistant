import http.client
import json
import os

#getting the file name with full path -->
abs_path = (os.path.dirname(__file__))
rel_path = "json database/zuoraWorkflowData.json"
fname = os.path.join(abs_path,rel_path)


#Read json Function-->
def readFile(fname):
    with open(fname,'r') as f:
        data = json.load(f)
    return data


#Write on json Function-->
def writeFile(data,fname):
    with open(fname,'w') as fs:
        json.dump(data,fs, indent=4)
    


#generate token for authentication-->
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



#connection to Zuora to fetch details-->
fullToken = "Bearer " + token
conn = http.client.HTTPSConnection("rest.apisandbox.zuora.com")
payload = ''
headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'Authorization': fullToken            #'Bearer bc3e07c105c74d2d8cc9cbf043f91e0a'
}
conn.request("GET", "/workflows", payload, headers)
res = conn.getresponse()
data = res.read()
temp = json.loads(data.decode("utf-8"))


#check if we have the write permission on the file if yes the write-->
if os.path.exists(fname):
    if os.access(fname, os.W_OK):
        writeFile(temp,fname)
    else:
        print("You dont have access to the file")

#print the recently created file to console-->
with open(fname,'r') as fs:
    temp = json.load(fs)
    print(json.dumps(temp,indent=4))
    
    