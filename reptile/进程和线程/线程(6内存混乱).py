import threading

i=0

def run1():
    global i
    for a in range(1000000):
        i+=a
        i-=a
    print('111',i)


def run2():
    global i
    for a in range(1000000):
        i += a
        i -= a
    print('222', i)


if __name__ == '__main__':
    p1 = threading.Thread(target=run1, name='name1')
    p2 = threading.Thread(target=run2, name='name2')

    p1.start()
    p2.start()
    p1.join()
    p2.join()


    print('i:',i)

