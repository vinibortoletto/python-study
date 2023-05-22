import requests

# response = requests.get("https://betrybe.com/")
# print(response.status_code)
# print(response.headers["Content-Type"])
# print(response.text)

# response = requests.post("https://httpbin.org/post", data="some content")
# print(response.text)

# response = requests.get(
#     "https://httpbin.org/get", headers={"Accept": "application/json"}
# )
# print(response.text)

# response = requests.get("http://httpbin.org/get")
# print(response.json())

response = requests.get("http://httpbin.org/status/404")
response.raise_for_status()
