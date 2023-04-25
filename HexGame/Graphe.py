from Constante import *


class Graphe: 

    gagnant = ""

    
    def __init__(self,couleur,bord):
        self.sommets = []
        self.couleur = couleur
        self.bord = bord

    
    def ajoutSommet(self,sommet):
        sommet.setGraphe(self)
        self.sommets.append(sommet)
        
    
    def fusion(self,graphe):
        
        if graphe.couleur != self.couleur:
            return 0
            
        self.bord = self.bord | graphe.bord

        while(len(graphe.sommets) != 0):
            self.ajoutSommet(graphe.sommets.pop())

        
        if self.couleur == BLEU:
            if (self.bord & (B_HAUT_BLEU | B_BAS_BLEU)) == B_HAUT_BLEU + B_BAS_BLEU:
                Graphe.gagnant = "BLEU"
        elif self.couleur == ROUGE:
            if (self.bord & (B_GAUCHE_ROUGE | B_DROIT_ROUGE)) == B_GAUCHE_ROUGE + B_DROIT_ROUGE:
                Graphe.gagnant = "ROUGE"

