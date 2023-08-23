import time
from multiprocessing import Process


def run1(num,name='张三'):
    for i in range(num):
        print(f'run1   {name}   ' + str(i))
        time.sleep(1)


def run2(num,name='李四'):
    for i in range(num):
        print(f'run2   {name}   ' + str(i))
        time.sleep(1)




if __name__ == '__main__':
    # 传递参数如果为一个值，需要给‘，’
    # 元组的效率高于列表
    Process(target=run1,args=(5,)).start() # 创建子进程1
    Process(target=run2,args=(6,)).start() # 创建子进程2






