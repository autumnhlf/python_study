from concurrent.futures import ThreadPoolExecutor,as_completed
import time

def run(i):
    print(f'开始',i)
    time.sleep(2)
    print(f'结束',i)
    return i


# 开启线程池 并发2个线程
pool = ThreadPoolExecutor(5)


# 列表推导式
# tasks = [pool.submit(run,i) for i in range(5)]

# for val in as_completed(tasks):
#     #  获取值
#     print('获取值111222333:',val.result())

for val in pool.map(run,list(range(5))):
    print(val)














