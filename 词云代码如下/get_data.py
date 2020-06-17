import requests
from lxml import etree
import json
import openpyxl
url="https://voice.baidu.com/act/newpneumonia/newpneumonia";
response=requests.get(url)
#print(response.text)
#生成html对象
html=etree.HTML(response.text)
#解析并赋值給result
result=html.xpath('//script[@type="application/json"]/text()')
#字符串类型
result=result[0]
#json.loads方法可以将字符串转换为python数据类型 dumps为加密 loads为解码
result=json.loads(result)
#获取国外疫情
print(result)
#创建工作簿
wb=openpyxl.Workbook()
#创建工作表
ws=wb.active
ws.title="国内疫情"
ws.append(['省份','累计确诊','死亡','治愈','现有确证','累计确诊数量','死亡增量','治愈增量','现有确诊增量'])
#print(type(result)) #dict字典类型 为了和国外和国内疫情进行区分通常用result_in表示国内疫情
result_in=result['component'][0]['caseList']
#添加国外的疫情情况
result_out=result['component'][0]['globalList']
print(result_out)
#遍历result
for each in result_in:
    #print(each)
    #print('*'*50+'\n')
    #为了让代码简洁要对代码进行一次赋值
    temp_list=[each['area'],each['confirmed'],each['died'],each['crued'],each['curConfirm'],each['confirmedRelative'],
               each['diedRelative'],each['curedRelative'],each['curConfirmRelative']]
    ws.append(temp_list)
    #为了让爬取的数据的空值变为0进行一次遍历
    for i in range(len(temp_list)):
        if temp_list[i]=='':
            temp_list[i]='0'
            ws.append(temp_list)
#遍历国外的列表
for each in result_out:
    #print(each)
    #print('*'*8+'\n')
    #创建国外工作表 亚洲字段
    sheet_title=each['area']
    #创建新的工作表
    ws_out=wb.create_sheet(sheet_title)
    ws_out.append(['国家','累计确诊','死亡','治愈','现有确诊','累计确诊增量'])
    for country in each['subList']:
        list_temp=[country['country'],country['confirmed'],country['died'],country['crued'],
                   country['curConfirm'],country['confirmedRelative']]
        for i in range(len(list_temp)):
            if list_temp[i]=='':
                list_temp[i]='0'
        ws_out.append(list_temp)

    wb.save('./data.xlsx')
"""
area-->省份/直辖市/特别行政区等
city-->城市
confirmed-->累计确证人数
died-->死亡人数
confirmedRelating-->累计确诊增量
curConfirmRelative-->现有确证的增量
diedRelative-->死亡的增量

"""


