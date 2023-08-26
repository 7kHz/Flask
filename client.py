import requests
headers = {'Content-Type': 'application/json'}
response = requests.post('http://127.0.0.1:5000/ads/',
                          json={'header': 'salt_3',
                                'description': '1234',
                                'owner': 'max'})
print(response.status_code)
print(response.text)

# response = requests.delete('http://127.0.0.1:5000/ads/1')
# print(response.status_code)
# print(response.text)

response = requests.get('http://127.0.0.1:5000/ads/1')
print(response.status_code)
print(response.text)
