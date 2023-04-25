from tkinter import*

from Hexagone import *

from Sommet import *


class Grille:

    
    def __init__(self,p,n,sommets):
        self.taille = n
        self.hexagones = []

        
        for i in range(self.taille):
            self.hexagones.append([])

        self.hexagones[0].append(Hexagone(p,sommets[0][0]))

        for i in range(self.taille):
            for j in range(1,self.taille):
                self.hexagones[i].append(Hexagone(self.hexagones[i][j-1].points[4],sommets[i][j]))
            if (i < self.taille-1):
                self.hexagones[i+1].append(Hexagone(self.hexagones[i][0].points[2],sommets[i+1][0]))                          

    
    def tracer(self,canvas):
        
        H = self.hexagones

        for i in range(self.taille):
            for j in range(0,len(H[i])):
                H[i][j].tracer(canvas)

        for i in range(self.taille):

            canvas.create_line(H[0][i].points[0].x, H[0][i].points[0].y, H[0][i].points[5].x, H[0][i].points[5].y, width=5, fill="#aee1f6")
            canvas.create_line(H[0][i].points[4].x, H[0][i].points[4].y, H[0][i].points[5].x, H[0][i].points[5].y, width=5, fill="#aee1f6")

            canvas.create_line(H[-1][i].points[2].x, H[-1][i].points[2].y, H[-1][i].points[3].x, H[-1][i].points[3].y, width=5, fill="#aee1f6")
            canvas.create_line(H[-1][i].points[1].x, H[-1][i].points[1].y, H[-1][i].points[2].x, H[-1][i].points[2].y, width=5, fill="#aee1f6")

            canvas.create_line(H[i][0].points[0].x, H[i][0].points[0].y, H[i][0].points[1].x, H[i][0].points[1].y, width=5, fill="#b97273")
            canvas.create_line(H[i][0].points[1].x, H[i][0].points[1].y, H[i][0].points[2].x, H[i][0].points[2].y, width=5, fill="#b97273")

            canvas.create_line(H[i][-1].points[5].x, H[i][-1].points[5].y, H[i][-1].points[4].x, H[i][-1].points[4].y, width=5, fill="#b97273")
            canvas.create_line(H[i][-1].points[4].x, H[i][-1].points[4].y, H[i][-1].points[3].x, H[i][-1].points[3].y, width=5, fill="#b97273")

        canvas.create_line((H[0][-1].points[4].x + H[0][-1].points[5].x)/2, (H[0][-1].points[4].y + H[0][-1].points[5].y)/2, H[0][-1].points[4].x,H[0][-1].points[4].y, width=5, fill="#b97273")
        canvas.create_line((H[-1][0].points[1].x + H[-1][0].points[2].x)/2, (H[-1][0].points[1].y + H[-1][0].points[2].y)/2, H[-1][0].points[2].x, H[-1][0].points[2].y, width=5, fill="#aee1f6")

    
    def trouver(self,p):
        for i in range(self.taille):
            for j in range(self.taille):
                if (self.hexagones[i][j].centre.distance(p) <= 25):
                    return self.hexagones[i][j]
        return False

    
    def placer(self,couleur,hexagone,canvas):
        if couleur == ROUGE:
            hexagone.centre.tracerCercle(25,COULEUR_ROUGE,canvas)
        elif couleur == BLEU:
            hexagone.centre.tracerCercle(25,COULEUR_BLEU,canvas)