import threading
import time


def run():
    print('1111')
    time.sleep(2)
    print('222')

if __name__ == '__main__':
    # t1 = time.time()
    # for i in range(5):
    #     p1 = threading.Thread(target=run)
    #     p1.start()
    #     p1.join()
    # t2 = time.time()
    # print(t2-t1)
    t1 = time.time()
    p_list=[]
    for i in range(5):
        # 创建线程
        p1 = threading.Thread(target=run)
        # 开启线程
        p1.start()
        p_list.append(p1)
    # 线程等待
    for i in p_list:
        i.join()
    t2 = time.time()
    print(t2-t1)





