from bs4 import BeautifulSoup # library
import requests

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'
headers = {
  'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
} # user agent to evoid catcha
response = requests.get(url, headers=headers)

if response.status_code == 200:
  print('The request was successful')

  soup = BeautifulSoup(response.text, 'html.parser') # indent the html

  # print(soup.prettify())
  title_tag = soup.title
  if title_tag:
    print(f"The website title is: {title_tag.text}") # title tag

  # find price using bs
  # price_span = soup.find('span', class_='rc-prices-fullprice')
  # if price_span:
  #   print(f"The product price is: {price_span.text}") # search price

  # find all prices
  # prices_span = soup.find_all(class_='rc-prices-fullprice')
  # for price in prices_span:
  #   print(f"The product price is: {price.text}") # search all prices

  # find each product and get the name and price
  products = soup.find_all(class_='rc-productselection-item')
  for product in products:
    name = product.find(class_="list-title").text
    price = product.find(class_="rc-prices-fullprice").attrs
    print(f"The product with the following features:\n {name}\nPrice: {price}\n\n") # all products with name