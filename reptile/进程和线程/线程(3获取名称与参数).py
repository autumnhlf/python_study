import threading
import time

def run(a):
    print(f'1111   {a}',threading.currentThread().name)
    time.sleep(2)
    print('222')

if __name__ == '__main__':
    # 创建线程并起名称  加参数
    p1 = threading.Thread(target=run,args=(2,),name='name1')
    p2 = threading.Thread(target=run,args=(4,),name='name2')

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('主进程name：'+threading.currentThread().name)
'''
每个进程会有一个默认主线程
在每个进程内开启的线程为子线程
'''










