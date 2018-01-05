import requests

index_00 = requests.get("https://www.baidu.com",params={"word":"Hello"})
print(index_00.status_code)
print(index_00.encoding)
print(index_00.text)
