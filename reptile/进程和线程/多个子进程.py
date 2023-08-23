from multiprocessing import Process


def get_data(url):
  print(url)





if __name__ == '__main__':
   url = 'http://www.baidu.com?page='
   for i in range(10):
       new_url = url + str(i)
       Process(target=get_data,args=(new_url,)).start()






