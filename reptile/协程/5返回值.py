import asyncio

async def run(url):
    print('接受',url)
    await asyncio.sleep(2)
    print('结束')
    return url

# 回调函数
def call_back(future):
    print(future)
    print('回调函数',future.result())

if __name__ == '__main__':
    con = run('www.baidu.com')
    # 创建task
    task = asyncio.ensure_future(con)
    # 添加回调操作 获取返回值
    task.add_done_callback(call_back)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)








