import threading

name = '张三'

def run():
    global name
    name = '里斯'
    age = 18
    print(f'我叫{name},今年{age}岁')

if __name__ == '__main__':
    p1 = threading.Thread(target=run, name='name1')
    p1.start()
    p1.join()


    print('我在外部获取数据',name)
    print('结束')