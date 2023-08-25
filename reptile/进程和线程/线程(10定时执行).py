import threading

def run():
    print('111')

# 定时执行 传入参数秒
p1 = threading.Timer(3,run)
p1.start()

print(threading.enumerate())










