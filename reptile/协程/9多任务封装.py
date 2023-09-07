import asyncio

# 异步任务
async def run(url):
    print('协程',url,'开始抓取')
    return url;


# 回调函数
def call_back(f):
    print('回调返回值',f.result())

async def main():
    url_list = ['douyin', 'baidu', 'guge']
    tasks = []  # 包含多个task任务
    for i in url_list:
        con = run(i)
        # 创建task
        task = asyncio.ensure_future(con)
        # 添加回调操作 获取返回值
        task.add_done_callback(call_back)
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    # 任务函数注册到消息循环上
    loop.run_until_complete(main())
    print('112233')








