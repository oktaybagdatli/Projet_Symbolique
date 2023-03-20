from dataclasses import dataclass

        
@dataclass
class Chiffre():
    color:str
    valeur:int
    def __post_init__(self,color,valeur):
        self.color =color
        self.valeur = valeur
        
        
    
@dataclass
class Tige():
    chiffres:list[Chiffre]
    capacite:int = 3
    
    def ajouterChiffre(self,chiffre):
        if self.capacite != 0:
            self.chiffres.append(chiffre)
            
    def getChiffres(self):
        return self.chiffres
    

        
        
        
        
    
@dataclass 
class Etat():
    tiges:list[Tige]
    
    
    
    def __post_init__(self,tiges):
        for tige in tiges:
            self.tiges.append(tige)
            
            
            
    def getTige(self,numeroTige):
        return self.tiges[numeroTige-1]
    
    
    def enleverRemettreChiffre(self,numDepart,numDestination):
        tigeDep = self.getTige(numDepart)
        tigeDest = self.getTige(numDestination)
        chiffre = tigeDep.getChiffres().pop()
        tigeDest.ajouterChiffre(chiffre)
        
            
    
    
    
    
    
    