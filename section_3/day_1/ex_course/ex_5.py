import requests
from parsel import Selector

BASE_URL = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"

response = requests.get(BASE_URL)

selector = Selector(text=response.text)
images = selector.css("a.image img::attr(src)").getall()


for image in images:
    image_name = image.split("/")[-1::][0]
    print(image_name)
