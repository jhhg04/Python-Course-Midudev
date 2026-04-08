# How to make API requests with Python
# with and without dependencies

# 1. Without dependencies (harder, no external libraries)
import urllib.request
import json

DEEPSEEK_API_KEY = "xxx"

api_posts = "https://jsonplaceholder.typicode.com/posts/"

try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  json_data = json.loads(data.decode('utf-8'))
  print(json_data) # [{'userId': 1, 'id': 1,..........
  response.close()
except urllib.error.URLError as e:
  print(f"Request error: {e}") # add error in except


# 2. With dependency (requests)
import requests

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
response_json = response.json()
print(response_json) # GET: [{'userId': 1, 'id': 1,...........

# 3. A POST request
print("\nPOST:")
try:
  response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1
    })
  print(response.status_code) # POST:{'title': 'foo', ......} # POST: 201
except requests.exceptions.RequestException as e:
  print(f"Request error: {e}") 

# 4. A PUT request
print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1,
    })

  print(response.status_code) # PUT: All object # PATCH: only what you need modify in Object
except requests.exceptions.RequestException as e:
  print(f"Request error: {e}")

# Using the OpenAI GPT-4o API
# Ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAI_KEY = "sk-XXXXXXXX" # use your key

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Write a short poem about programming")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

# Call the DEEPSEEK API

import json

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Write a short poem about programming")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])