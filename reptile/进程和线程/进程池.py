import time
from multiprocessing import Pool,cpu_count

def get_data(url):
  print(url)
  time.sleep(10)





if __name__ == '__main__':
   url = 'http://www.baidu.com?page='
   pool = Pool(4) # 开启几个进程 默认开启核心数个cpu  cpu_count()
   for i in range(20):
       new_url = url + str(i)
       # 任务添加到进程池
       pool.apply_async(get_data,args=(new_url,))

   pool.close() #关闭池子
   pool.join() #阻塞等待
   print('主进程结束')

   # print(cpu_count())


