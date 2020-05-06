class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
class Shape:
    def __init__(self,line_list,point_list):
        self.l = line_list
        self.p = point_list
        
        
        
def plot_Shape(shape,point_list):
    from matplotlib import pyplot as plt
    from shapely.geometry.polygon import Polygon
    
    plist = [(p.x,p.y) for p in shape.p]

    poly = Polygon(plist)
    x,y = poly.exterior.xy
    for p in point_list: 
        plt.plot([p.x],[p.y],'*',3)
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
    