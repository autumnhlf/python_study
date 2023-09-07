import asyncio


# 异步任务
async def run(url):
    print('协程', url, '开始抓取')
    return url;


# 回调函数
def call_back(f):
    print('回调返回值', f.result())

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    url_list = ['douyin', 'baidu', 'guge']
    tasks = []  # 包含多个task任务
    for i in url_list:
        con = run(i)
        task = loop.create_task(con)
        task.add_done_callback(call_back)
        tasks.append(task)

    # 任务函数注册到消息循环上
    loop.run_until_complete(asyncio.wait(tasks))
    print('112233')