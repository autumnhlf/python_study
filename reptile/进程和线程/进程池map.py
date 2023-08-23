import time
from multiprocessing import Pool

def get_data(url):
  print(url)
  time.sleep(2)





if __name__ == '__main__':
   url = 'http://www.baidu.com?page='
   pool = Pool(10) # 传参 开启几个进程 默认开启核心数个cpu  cpu_count()
   url_list = []
   for i in range(20):
       new_url = url + str(i)
       url_list.append(new_url)

   pool.map(get_data,url_list)
   print('主进程结束')




