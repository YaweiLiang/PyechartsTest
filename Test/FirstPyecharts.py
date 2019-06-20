import pyecharts
from pyecharts import Bar
bar = Bar("我的第一个图表", "这里是副标题")
x_aris_name=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]    #注解==label
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
bar = Bar('柱状信息堆叠图')
bar.add('商家A',x_aris_name,v1,is_stack = True,mark_point = ['average'])  #is_stack = True才表示堆叠在一起
bar.add('商家B',x_aris_name,v2,is_stack = True,mark_line = ['min','max'],is_convert = True)
bar.render('./FirstPyecharts.html')                          #文件存储路径（默认保存当前文件路径）


