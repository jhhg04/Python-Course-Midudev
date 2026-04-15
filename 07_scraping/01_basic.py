# pip3 install requests -> install the dependency to make HTTP requests

import requests # to make request
import re # to make regex

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'

response = requests.get(url) # use get method

if response.status_code == 200:
  print('The request was successful')

  html = response.text
  print(html)

  # regular expression to find the price
  price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>' # regex
  match = re.search(price_pattern, html)

  if match:
    print(f"The product price is: {match.group(1)}") # print price

  # get the title if the pattern is found
  title_pattern = r'<title>(.*?)</title>' # regex use for google
  match = re.search(title_pattern, html)

  if match:
    print(f"The website title is: {match.group(1)}")