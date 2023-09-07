import asyncio
import aiofiles


async def main():
    async with aiofiles.open('1同步代码.py',encoding='UTF-8')as f:
        return await f.readlines()



print(asyncio.run(main()))

