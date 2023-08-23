import time
from multiprocessing import Process


def run1():
    for i in range(5):
        print('run1   ' + str(i))
        time.sleep(1)


def run2():
    for i in range(5):
        print('run2   ' + str(i))
        time.sleep(100)




if __name__ == '__main__':
    a = time.time()
    p1 = Process(target=run1) # 创建子进程1
    p2 = Process(target=run2) # 创建子进程2
    p1.start() # 开启子进程1
    p2.start() # 开启子进程1
    p1.join()  # 阻塞等待子进程1执行完
    p2.join()  # 阻塞等待子进程2执行完
    print('333')
    print(time.time() - a)






