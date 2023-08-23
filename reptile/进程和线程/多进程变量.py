from multiprocessing import Process

num=1
def run1():
    global num
    num=2
    print('run1',num)




if __name__ == '__main__':
    # 进程之间是独立的，每个进程有自己的独立存储

    p1 = Process(target=run1) # 创建子进程1
    p1.start()
    print('over')
    print(num)

    # p1 = Process(target=run1) # 创建子进程1
    # p1.start()
    # p1.join()
    # print('over')
    # print(num)



