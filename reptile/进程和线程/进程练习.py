import time
from multiprocessing import Queue,Process

def product(q):
    print('生产子进程。。。。')
    for data in ['good','nice','cool','handsome']:
        time.sleep(2)
        print('生产出：%s'%data)
#         将生产的数据写入队列
        q.put(data)
    print('结束子进程。。。。')

def customer(q):
    print('启动消费子进程。。。')
    while 1:
        print('等待生产者生产数据')
#         获取生产者生产的数据，如果队列中没有数据会阻塞，等待队列中有数据在获取
        value = q.get()
        print('消费者消费了%s数据'%(value))
    print('结束消费子进程。。。。')


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=product,args=(q,))  # 创建子进程1
    p2 = Process(target=customer,args=(q,))  # 创建子进程1

    p1.start()
    p2.start()
    p1.join()
    # p2 子进程里面是死循环，无法等待它的结束
    # p2.join()
    p2.terminate()
    print('主进程结束')















