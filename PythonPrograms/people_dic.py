import json
import requests
import os

# people = [
#     {
#         "name": "Sabrina Green",
#         "username": "sgreen",
#         "phone": {
#             "office": "802-867-5309",
#             "cell": "802-867-5310"
#         },
#         "department": "IT Infrastructure",
#         "role": "Systems Administrator"
#     },
#     {
#         "name": "Eli Jones",
#         "username": "ejones",
#         "phone": {
#             "office": "684-348-1127"
#         },
#         "department": "IT Infrastructure",
#         "role": "IT Specialist"
#     },
# ]

with open('people.json', 'w') as people_json:
	# json.dump(people, people_json, indent=2)
	people = json.load(people_json)

print(people)
# people_json = json.dumps(people)
print(people_json)

# response = requests.get('https://google.com', stream=True)

# print(response.raw.read()[:100])
# print(response.text[:100])
# print(response.request.headers['Accept-Encoding'], 'gzip, defflate')
# print(response.headers['Content-Encoding'], 'gzip')
# response.ok
# status = response.status_code
ckeck = response.raise_for_status()

p = {"description": "white kitten", "name": "Snowball", "age_months": 6}

first_post = response = requests.post("https://example.com/path/to/api", data=p)

first_url = response.request.url
'https://example.com/path/to/api'
first_body = response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'

print(first_post)
print(first_url)
print(first_body)
print(status)
