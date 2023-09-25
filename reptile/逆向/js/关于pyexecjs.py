import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen,encoding='UTF-8')
# 上面的代码是用于js中有中文时，调用报错或者乱码（必须要放在最开头的地方）

import execjs

# 最常用的一套方案
f = open("测试.js",mode="r",encoding="utf-8")
js_code = f.read()

# 先加载js代码
js = execjs.compile(js_code)
# r = js.call("fn",2,4)
# print(r)
r = js.call("fn2")
print(r)
