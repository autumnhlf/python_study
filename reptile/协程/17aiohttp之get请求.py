import aiohttp
import asyncio

async def fetch(session,url):
    # 异步请求网址
    async with session.get(url) as response:
        # 将对应的内容进行返回
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        source= await fetch(session,'http://httpbin.org/headers')
        print(source)

asyncio.run(main())









