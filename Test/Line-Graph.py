from pyecharts import Line
attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
line = Line('折线示例图')
line.add('商家A',attr,v1,
    mark_point = ['average','max','min'],
    is_fill = True,
    mark_point_textcolor = '#40ff27',
    line_opacity = 0.2)     #数字越小颜色越浅
line.add('商家B',attr,v2,
         mark_point = ['average','max','min'],
         is_smooth = True,
         is_fill = True,
         mark_point_symbol = 'arrow',
         mark_point_symbolsize = 40)
line.render('./Line-graph.html')

