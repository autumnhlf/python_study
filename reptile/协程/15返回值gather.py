import asyncio

# 异步任务
async def run(url):
    print('协程',url,'开始抓取')
    return url;

async def main():
    url_list = ['douyin', 'baidu', 'guge']
    tasks = []  # 包含多个task任务
    for i in url_list:
        con = run(i)
        task = asyncio.create_task(con)
        tasks.append(task)
    done = await asyncio.gather(*tasks)
    for i in done:
        # print(i)
        print('获取返回值：', i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 任务函数注册到消息循环上
    loop.run_until_complete(main())


