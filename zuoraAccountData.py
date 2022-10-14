import os
import json
import http.client

#getting the file name with full path -->
abs_path = (os.path.dirname(__file__))
rel_path = "json database/zuoraAccounts.json"
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
    
    
#connection with Zuora to fetch data -->
conn = http.client.HTTPSConnection("rest.apisandbox.zuora.com")
payload = ''
headers = {
  'Authorization': 'Basic cm9oYW4ucm95Y2hvd2RodXJ5QHN5bnRoZXNpcy1zeXN0ZW1zLmNvbTpSb2hhbkAxOTk3'
}
acn = input("Please provide the account Number you want to fetch: ")
str = "/v1/accounts/" + acn
conn.request("GET", str, payload, headers)
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