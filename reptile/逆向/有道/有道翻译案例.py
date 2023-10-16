from hashlib import md5
import time
import requests,base64
from Crypto.Cipher import AES
import hashlib

t = 'fsdsogkndfokasodnaso'
u = 'webfanyi'
e = str(int(time.time() * 1000))  # 时间戳
d = 'fanyideskweb'
s = f'client={d}&mysticTime={e}&product={u}&key={t}'

obj = md5()
obj.update(s.encode())
sign = obj.hexdigest()

url = 'https://dict.youdao.com/webtranslate'

real_data = {
    'i': 'apple',
    'from': 'auto',
    'to': '',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': e,
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg'
}

headers = {
'Referer':'https://fanyi.youdao.com/',
'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=248806123.00721085; OUTFOX_SEARCH_USER_ID="-1104611778@10.110.96.157"',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

resp = requests.post(url,data=real_data,headers=headers)
print(resp.text)

# ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl
# ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4



decodeKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
decodeIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"


# 在本案例中，先是对两个参数进行了参数加密
key = hashlib.md5(decodeKey.encode(encoding='utf-8')).digest()
iv = hashlib.md5(decodeIv.encode(encoding='utf-8')).digest()
# AES解密
# 先创建加密器（解密器）
# mode:要么是EBC,要么是CBC
#       对于我们而言，区别就是
#       EBC：不用给IV
#       CBC：需要给IV

aes_en = AES.new(key=key, mode=AES.MODE_CBC,IV=iv)
# 加密或者解密，需要的参数是字节
# 将已经加密的数据放进该方法
data_new = base64.urlsafe_b64decode(resp.text)
# 参数准备完毕后，进行解密
result = aes_en.decrypt(data_new).decode('utf8')
print(result)

