import asyncio



async def run():
    print('11111')
    await asyncio.sleep(2)
    print('22222')


if __name__ == '__main__':
    con = run()
    #创建task
    task = asyncio.ensure_future(con)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)





