from Graphe import *


class Sommet:
    def __init__(self):
        self.couleur = LIBRE
        self.graphe = None
        self.listeVoisin = []
        
      
    def setGraphe(self, graphe):
        self.graphe = graphe
        self.couleur = graphe.couleur
        
      
    def ajoutVoisin(self, voisin):
        self.listeVoisin.append(voisin)
        
    
    def jouer(self,couleur):
        if self.graphe == None:
            Graphe(couleur,B_NO).ajoutSommet(self)
        elif self.graphe.couleur == LIBRE:
            self.graphe.couleur = couleur
            self.couleur = couleur
        for i in range(len(self.listeVoisin)):
            if self.listeVoisin[i].couleur == couleur and self.listeVoisin[i].graphe != self.graphe:
                self.listeVoisin[i].graphe.fusion(self.graphe)