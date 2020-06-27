from bs4 import BeautifulSoup
import requests
import json

# Start the session
session = requests.Session()

# Create the payload

p = open('Credential.json',)
creds = json.load(p)
userName =creds['userName']
password =creds['password']
payload = {'userName':userName, 
          'password':password
         }
s = session.post("https://ntpc.envirologiciq.com/api/login", data=payload)

f = open('data.json',)
data = json.load(f)
# for x in creds:
for i in data['param']: 
    for key in i:
        # print(i[key])
        payloadData = i[key]
        s = session.post("https://ntpc.envirologiciq.com/api/metrics/widgets",json=payloadData)
        # print(s.text)
        x = json.loads(s.text)
        # json_object = json.dumps(x, indent = 4) 
        def write_json(data, filename='sample.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
    
        with open('sample.json') as json_file: 
            data = json.load(json_file)
            temp = data['sensor'] 
            temp.append(x) 
        write_json(data)

f.close() 
