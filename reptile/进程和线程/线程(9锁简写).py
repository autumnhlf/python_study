import threading

# 创建一把锁
import time

lock = threading.Lock()
i=0

def run1():
    global i
    # 上锁
    with lock:
        for a in range(1000000):
            i += a
            i -= a

    print('111',i)


def run2():
    global i
    # 上锁
    with lock:
        for a in range(1000000):
            i += a
            i -= a

    print('222', i)


if __name__ == '__main__':
    t1 = time.time()

    p1 = threading.Thread(target=run1, name='name1')
    p2 = threading.Thread(target=run2, name='name2')

    p1.start()
    p2.start()
    p1.join()
    p2.join()


    print('i:',i)
    print('over')

    t2 = time.time()
    print('时间:',t2-t1)