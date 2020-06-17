import openpyxl
from wordcloud import WordCloud


#读取数据
wb=openpyxl.load_workbook('data.xlsx')
#获取工作表
ws=wb['国内疫情']
#创建字典 为了和外国疫情区分frequency_in表示国内疫情
frequency_in={}
for row in ws.values:
    if row[0]=='省份':
        pass
    else:
        #通过字典将身份那一列去除
        frequency_in[row[0]]= float(row[1])
#将词云wordcloud进行实例化
wordcloud=WordCloud(font_path="C:Windows/Fonts/simhei.ttf",
                    background_color="white",
                    width=2000,height=1800)
#根据确证人数生成词云
wordcloud.generate_from_frequencies(frequency_in)
#保存词云
wordcloud.to_file('china.png')
#表示国外疫情
frequency_out={}
sheet_name=wb.sheetnames
for each in sheet_name:
    if '洲' in each:
        ws=wb[each]
        for row in ws.values:
            if row[0]=='国家':
                pass
            else:
                #转换为浮点型
                frequency_out[row[0]]=float(row[1])
#根据确证外国人数生成词云
wordcloud.generate_from_frequencies(frequency_out)
#保存词云
wordcloud.to_file('worldwide.png')