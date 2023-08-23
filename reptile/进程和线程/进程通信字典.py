from multiprocessing import Process,Manager


def run1(Dict):
   print('子进程放数据')
   Dict['name']='xiaoming'
   Dict['age']='19'






if __name__ == '__main__':
    # 创建队列对象
    Dict = Manager().dict()

    p1 = Process(target=run1,args=(Dict,)) # 创建子进程1
    p1.start()
    p1.join()
    print('主进程读数据',Dict)






