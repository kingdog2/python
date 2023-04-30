import requests

token = 'Ma56x6P1BdWGGSX7DMHiRFgYTJC3pAxNsAJxi4m0Dx3'

message = 'people'

headers = { "Authorization": "Bearer " + token }
data = { 'message': message }
image = open('test1.jpg', 'rb')    
files = { 'imageFile': image }   
requests.post("https://notify-api.line.me/api/notify",headers = headers, data = data, files=files)