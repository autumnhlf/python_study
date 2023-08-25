import time
import threading

def run1():
    # 获取线程名字
    print("启动 %s 子线程"%(threading.current_thread().name))
    for i in range(5):
        print('11111')
        time.sleep(1)


def run2(name,word):
    print("启动 %s 子线程"%(threading.current_thread().name))
    for i in range(5):
        print("%s is a %s man"%(name,word))
        time.sleep(1)


if __name__ == '__main__':
    t1 = time.time()
    '''
    主进程中默认有一个线程，称为主线程（父线程）
    主线程一般作为调度而存在，不具备实现业务逻辑
    '''

    # 创建子线程
    # name参数可以设置线程名称，如果不设置按顺序设置为Thread-n
    p1 = threading.Thread(target=run1, name='name1')
    p2 = threading.Thread(target=run2,args=('张三','china') ,name='name2')

    # 启动
    p1.start()
    p2.start()
    # 阻塞等待
    p1.join()
    p2.join()

    t2 = time.time()

    print('耗时：%.2f'%(t2-t1))





















