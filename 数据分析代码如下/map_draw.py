from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
class Draw_map():
    def to_map_city(self):
        pass
    #将参数传入
    def to_map_china(self,area,variate,update_time):
        #对分段地图进行分段赋值 列表字典
        pieces=[
            {"max":99999999,'min':1001,'label':'>10000','color':'#8A0808'},
            {"max": 9999, 'min': 1000, 'label': '1000-9999', 'color': '#B40404'},
            {"max": 999, 'min': 100, 'label': '100-999', 'color': '#DF0101'},
            {"max": 99, 'min': 10, 'label': '1-9', 'color': '#F5A9A9'},
            {"max": 9, 'min': 1, 'label': '1-9', 'color': '#F5A9A9'},
            {"max": 0, 'min': 0, 'label': '0', 'color': '#FFFFFF'},




        ]


        c = (
            Map(init_opts=opts.InitOpts(width='1000px',height='800px'))
            #进行值得替换 zip是内置函数将对应的项对应起来
                .add("累计确诊人数", [list(z) for z in zip(area,variate)], "china")
                .set_global_opts(
                #设置地图标题 副标题截止字符串的形式
                title_opts=opts.TitleOpts(title="中国疫情地图分布",subtitle='截止%s,中国疫情分布情况!'%(update_time)
                                          ,pos_left='center',pos_top='30px'),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,pieces=pieces),
            )
                .render("中国疫情地图.html")
        )
