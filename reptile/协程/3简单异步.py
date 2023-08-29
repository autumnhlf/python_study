import asyncio
import time


async def run():
    print('11111')
    # asyncio.sleep() 用于协程对象的阻塞等待
    await asyncio.sleep(2)
    # time.sleep(2)

    print('22222')

if __name__ == '__main__':
    # con = run()
    # asyncio.run
    con = run()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(con)

