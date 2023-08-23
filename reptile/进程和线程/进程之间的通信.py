from multiprocessing import Process,Queue

def run1(que):
    print('子进程放数据')
    que.put(1)
    que.put(2)
    que.put(3)



if __name__ == '__main__':
    # p1 = Process(target=run1)  # 创建子进程1
#     创建队列对象
    que = Queue()
    p1 = Process(target=run1,args=(que,))
    p1.start()
    p1.join()
    print('主进程读数据',que.get())
    print('主进程读数据',que.get())
    # print('主进程读数据',que.get(timeout=3))
    # 如果队列中没有数据了，会阻塞等待
    # 如果在timeout时间内还没有数据跑出异常
    # print('主进程读数据', que.get(timeout=3))











