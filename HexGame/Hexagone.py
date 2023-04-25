from tkinter import*

from Point import *

from Constante import *

from Sommet import *


class Hexagone:

    def __init__(self,p,sommet):
        
        points = [p]
        points.append(Point(points[0].x,points[0].y+40))
        points.append(Point(points[1].x+40*cos(120), points[1].y+40*sin(120)))
        points.append(Point(points[2].x+40*cos(120), points[2].y-40*sin(120)))
        points.append(Point(points[3].x, points[3].y-40))
        points.append(Point(points[4].x-40*cos(120), points[4].y-40*sin(120)))
        self.points = points;

        self.sommet = sommet
        self.centre = Point((points[0].x+points[3].x)/2,(points[0].y+points[3].y)/2)

    
    def tracer(self,canvas):
        self.trace = self.points[0].tracerHexagone(self.points[1],self.points[2],self.points[3],self.points[4],self.points[5],canvas)
        
        self.centre.tracerCercle(25,'',canvas,'#ddd')
            
                  
    def setSommet(self,sommet):
        self.sommet = sommet

    
    def estLibre(self):
        return self.sommet.couleur == LIBRE
