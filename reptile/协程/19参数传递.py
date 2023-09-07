import aiohttp
import asyncio



async def main():
    async with aiohttp.ClientSession() as session:
        params = {'name': '张三', 'age': 18}
        async with session.get('http://httpbin.org/get',params=params) as response:
            # 将对应内容返回
            print(response.url)#获取当前请求的url

asyncio.run(main())









