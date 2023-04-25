from math import *;

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self,p):
        return sqrt(pow((self.x - p.x),2) + pow((self.y - p.y),2))

    
    def tracerCercle(self,r,couleur,canvas,hover=''):
    	canvas.create_oval(self.x-r,self.y-r,self.x+r,self.y+r,fill=couleur,outline='',activefill=hover)

    
    def tracerHexagone(self,p1,p2,p3,p4,p5,canvas):
    	return canvas.create_polygon(self.x,self.y, p1.x, p1.y, p2.x, p2.y, p3.x,p3.y, p4.x,p4.y, p5.x,p5.y,fill= "white", outline='black')
