import asyncio
import time


async def run(url):
    print(f'开始请求{url}的数据')
    await asyncio.sleep(2)
    print(f'结束请求{url}的数据')
    data = url + '的抓取数据'
    return data

# 回调函数
def call_back(future):
    print(future)
    print('回调函数',future.result())


if __name__ == '__main__':
    t1 = time.time();
    loop = asyncio.get_event_loop()
    url_list = ['douyin','baidu','guge']
    tasks = [] #包含多个task任务
    for i in url_list:
        con = run(i)
        # 创建task
        task = asyncio.ensure_future(con)
        # 添加回调操作 获取返回值
        task.add_done_callback(call_back)

        tasks.append(task)

    # 任务函数注册到消息循环上
    loop.run_until_complete(asyncio.wait(tasks))
    t2 = time.time();
    print('时间',t2-t1)


