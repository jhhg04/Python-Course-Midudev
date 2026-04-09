# 1. Introduction to Classes in Python
# Classes are templates used to create objects. An object is an instance of a class.
# They allow us to group data (attributes or properties) and functions (methods) in one place.

OPENAI_KEY = ""
DEEPSEEK_API_KEY = ""

# Basic example of a class
class Car:
  # class attributes (shared across all instances)
  type = "four-wheel vehicle"
  wheels = 4

  # special method that constructs the object
  # this method is automatically called when you create an instance
  def __init__(self, brand, model, color):
    # instance attributes
    self.brand = brand
    self.model = model
    self.color = color

  def start(self):
    print(f"The car {self.brand} {self.model} has started! 🚗")


my_car = Car("Toyota", "Corolla", "red")
my_car.start()

print(my_car.brand)

pheralb_car = Car("Ford", "Fiesta", "blue")
pheralb_car.start()

print(pheralb_car.brand)

# Encapsulation: hiding the internal details of a class
# and exposing only the public interface

# Create a class to call AI APIs like OpenAI, DeepSeek, or others

import requests

class AIAPI:
  def __init__(self, api_key, url, model):
    self.api_key = api_key
    self.url = url
    self.model = model

  def call(self, prompt):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.api_key}"
    }
    data = {
      "model": self.model,
      "messages": [{"role": "user", "content": prompt}]
    }

    try:
      response = requests.post(self.url, json=data, headers=headers)
      res_json = response.json()
      print(res_json["choices"][0]["message"]["content"])
    except requests.exceptions.RequestException as e:
      print(f"Request error: {e}")
      return None

print("\nOPEN_AI:")
openai_api = AIAPI(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Write a short poem about programming")

print("\nDEEPSEEK:")
deepseek_api = AIAPI(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

deepseek_api.call("Write a short poem about programming")