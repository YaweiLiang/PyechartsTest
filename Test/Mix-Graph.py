#代码1：bar + line 叠加
from pyecharts import Bar,Line,Overlap
attr = ['A','B','C','D','E','F']
v1 = [10,20,30,40,50,60]
v2 = [38,28,35,58,65,70]
bar = Bar('Line - Bar示例')
bar.add('bar',attr,v1,mark_point = ['average'],mark_line = ['min','max'])
line = Line()
line.add('line',attr,v2,
         is_smooth = True,
         is_fill = True,
         mark_point_symbol = 'arrow',
         mark_point_symbolsize = 40)

overlop = Overlap()
overlop.add(bar)
overlop.add(line)
overlop.render('./Mix-graph.html')
