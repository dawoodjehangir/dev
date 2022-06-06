from email import message
import json
import requests 

#endpoint = "https://www.httpbin.org/status/200"
#endpoint = "https://www.httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

#get_response = requests.get(endpoint) #http get request 


get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "HELLO HELLO"})

#print(get_response.headers)
#print(get_response.text)
print(get_response.json())




## Normal HTTP request => (returns) => HTML document (e.g. a webpage)
## used by browsers for humans as it is fancy/readable 

## REST API HTTP request => (returns) => usually JSON, maybe XML, readable/usable data format in an application. 
## Used for software/applications to communicate with each other over web/internet