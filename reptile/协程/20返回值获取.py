import json

import aiohttp
import asyncio

async def fetch(session,url):
    # 异步请求网址
    async with session.post(url,data='传递数据') as response:
        # 将对应的内容进行返回
        return await response.text()
        # return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        source= await fetch(session,'http://httpbin.org/post')
        print(json.loads(source))
        # print(source)

asyncio.run(main())









