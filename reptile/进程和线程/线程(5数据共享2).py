import threading
import time

name = '张三'

def run1():
    time.sleep(2)
    global name
    name = '里斯'
    age = 18
    print(f'我叫{name},今年{age}岁',threading.currentThread().name)


def run2():

    age = 18
    print(f'我叫{name},今年{age}岁',threading.currentThread().name)

if __name__ == '__main__':
    p1 = threading.Thread(target=run1, name='name1')
    p2 = threading.Thread(target=run2, name='name2')
    p1.start()
    p2.start()
    p1.join()
    p2.join()


    print('我在外部获取数据',name)
    print('结束')