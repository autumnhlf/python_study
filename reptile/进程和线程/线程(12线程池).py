from concurrent.futures import ThreadPoolExecutor,wait
import time

def run(i,a):
    print(f'开始{a}',i)
    time.sleep(2)
    print(f'结束{a}',i)


# 开启线程池 并发2个线程
pool = ThreadPoolExecutor(2)
# 如何放入线程池
# for i in range(5):
#     # 传参 正常放入
#     pool.submit(run,i,'zhangsan')

# 列表推导式 等同于上方
tasks = [pool.submit(run,i,11) for i in range(5)]
wait(tasks) #等待 子线程执行
print('over')
print(tasks)






