PyechartsTests

## There are my all kinds of Pyecharts test programs ##

### Sample line charts look like this:

![折线示例图](C:\Users\OEMUSER\PycharmProjects\TestPyecharts\pictures\折线示例图.png)

### Bar-charts look like this: ###

![柱状信息堆叠图](C:\Users\OEMUSER\PycharmProjects\TestPyecharts\pictures\柱状信息堆叠图.png)

### Pie-charts look like this:

![饼图-环形图示例](C:\Users\OEMUSER\PycharmProjects\TestPyecharts\pictures\饼图-环形图示例.png)

### Map-charts look like this:  

![广东地图示例](C:\Users\OEMUSER\PycharmProjects\TestPyecharts\pictures\广东地图示例.png)

### Mixed-charts look like this:  

![Line - Bar示例](C:\Users\OEMUSER\PycharmProjects\TestPyecharts\pictures\Line - Bar示例.png)

## Requirements: ##

* python 3.7.3

* Pyecharts

  > pip install pyecharts==0.5.11
  >
  > pip install pyecharts_snapshot

## Comments:

```
is_stack = True             #堆叠
mark_point = ['average','max','min']    #标记值
mark_line = ['min','max']   #标记线
is_convert = True           #坐标轴翻转
is_symbol_show = True,      #是否显示标记图形
is_smooth = False,          #是否显示平滑曲线
is_step = False,            #是否是阶梯线
is_fill = False,**kwargs    #是否填充曲线区域面积
line_opacity = 0.2,         #线条不透明度
area_opacity = 0.4,
radius = [40,75],           #环形内外圆的半径
is_label_show = True,       #是否显示标签
label_text_color = None,    #标签颜色
legend_orient = 'vertical', #图例垂直
legend_pos = 'left'
maptype = '广东'             #地图类型，支持China，world，北京，天津，上海，湖南，湖北，……363个二线城市
is_roam = True              #是否开启鼠标缩放，漫游等，默认 True,
is_map_symobol_show         #是否显示地图标记，默认 True。
```