import scrapy
from scrapy import Request

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['192.168.1.52']
    start_urls = ['http://192.168.1.52:8093/basebusiness/SocialWorkActivit/list?status=4']

    def start_requests(self):
        #设置登录需要的各种参数
        login_url = "http://192.168.1.52:8093/login"
        data = {
            "username": "admin",
            "password": "S0pCMTIzNA==",
            "validateCode":"",
            "rememberMe": "false",
            "sign":"yfjh",
            "codeShow": "false",
        }

        # 使用FormRequest发送post请求
        yield scrapy.FormRequest(login_url,formdata=data, callback=self.success_login)


    def success_login(self,response,**kwargs):
        print("success_login",response.json())
        # 登录成功以后
        yield scrapy.FormRequest(self.start_urls[0],method="POST")


    def parse(self, response,**kwargs):
        print("self",response.json())
