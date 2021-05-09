import requests
from parsel import Selector
response=requests.get('https://amazon.com/')
selector=Selector(response.text)
href_1=selector.xpath('//a/@href').getall()
image=selector.xpath('//img/@src').getall()
image_1=selector.xpath('//img/@alt').getall()
print(href_1)
print(image)
print(image_1)