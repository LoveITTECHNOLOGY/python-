#导入爬虫模块
import requests
#导入地图xml模块
from lxml import etree
#正则表达式
import re
#导入json模块将字符串转换为字典类型
import json
#定义一个函数
class Get_data():
    #获取数据
    def get_data(self):
        #开始获取对应网站的url
      response=requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia')
      with open('html.txt','w') as file:
        file.write(response.text)
    #提取更新时间
    def get_time(self):
        with open('html.txt','r') as file:
            #赋值给text
            text=file.read()
        #引入正则表达式
        time=re.findall('"mapLastUpdatedTime":"(.*?)"',text)[0]
        #设置一个返回值
        return time
    #解析数据
    def parse_data(self):
        #调用文件的赋值方法
        with open('html.txt','r') as file:
            #赋值
            text=file.read()
        html=etree.HTML(text)
        #解析数据
        result=html.xpath('//script[@type="application/json"]/text()')
        #是字符串不可用字典分析 但是如何将字符串类型转换为字典了要用到json模块
        result=result[0]
        #进行数据解码从而进行字典分析将内容重新赋值给result
        result=json.loads(result)
        #之前的数据在component键 第一键数据分析爬取到全国各省各市 第一层分析
        result=result['component'][0]['caseList']
        #加密将python类型转换为字符串
        result=json.dumps(result)
        #写入json文件 数据第一步提取
        with open('data.json','w') as file:
            file.write(result)
            print('数据已写入.....')

