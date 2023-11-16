import requests

url = 'http://cd.tibetairlines.com.cn:9100/login'

data = {
    "grant_type":"password",
    "isLogin":"true",
    "password":"123",
    "username":"abc,C"
}

resp = requests.post(url,data=data)
resp.close()
print(resp.text)