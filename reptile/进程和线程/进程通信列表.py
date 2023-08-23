from multiprocessing import Process,Manager


def run1(List):
   print('子进程放数据')
   List.append('111')
   List.append(222)






if __name__ == '__main__':
    # 创建队列对象
    List = Manager().list()

    p1 = Process(target=run1,args=(List,)) # 创建子进程1
    p1.start()
    p1.join()
    print('主进程读数据',List)






