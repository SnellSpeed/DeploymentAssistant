import http.client
import json
import os

#getting the file name with full path -->
abs_path = (os.path.dirname(__file__))
rel_path = "json database/zuoraSettings.json"
fname = os.path.join(abs_path,rel_path)

#Read json Function-->
def readFile(fname):
    with open(fname,'r') as f:
        data = json.load(f)
    return data


#Write on json Function-->
def writeFile(data,fname):
    with open(fname,'w') as fs:
        json.dump(data,fs, indent=2)
    

#Zuora connection for fetching data-->
conn = http.client.HTTPSConnection("rest.apisandbox.zuora.com")
payload = ''
headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'Authorization': 'Bearer 6da9506194324548b47009123d43fe45'
}
conn.request("GET", "/settings/listing", payload, headers)
res = conn.getresponse()
data = res.read()
temp = json.loads(data)


#Check if the path has the permission to write-->
if os.path.exists(fname):
    if os.access(fname, os.W_OK):
        writeFile(temp,fname)
    else:
        print("You dont have access to the file")

#print the recently created file to console-->
with open(fname,'r') as fs:
    temp = json.load(fs)
    print(json.dumps(temp,indent=2))
    
    