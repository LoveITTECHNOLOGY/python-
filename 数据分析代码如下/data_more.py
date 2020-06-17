#导入将python转换为字符串模块
import json
#导入地图文件
from group4.virus_analyse import map_draw
from group4.virus_analyse import data_gui

#打开之前的第一步数据爬取
with open('data.json','r') as file:
    data=file.read()
    #将字符串转换为python类型 list
    data=json.loads(data)
#实例化一个类
map=map_draw.Draw_map()
#实例化时间类
datas=data_gui.Get_data()
#赋值
datas.get_time()
update_time=datas.get_time()
#解析数据
datas.parse_data()
#中国地区疫情数据
def china_map():
    #省份
    area=[]
    confirmed=[]
    for each in data:
        print(each)
        print('*'*50+'\n')
        area.append(each['area'])
        #通过键来获取值
        confirmed.append(each['confirmed'])
        #地区 人数 时间
    map.to_map_china(area,confirmed,update_time)

#省份疫情数据
def province_map():
    for each in data:
        city=[]
        confirmeds=[]
        province=each['area']
        for  each_city in each['subList']:
            city.append(each_city['city'])
            confirmeds.append(each_city['confirmed'])

#调用输出中国疫情数据
china_map()