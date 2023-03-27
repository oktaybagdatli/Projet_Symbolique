from dataclasses import dataclass

        
@dataclass
class Chiffre():
    color:str
    valeur:int
    
    
@dataclass
class Tige():
    chiffres:list[Chiffre]
    capacite:int = 3
    
    def ajouterChiffre(self,chiffre):
        if self.capacite != 0:
            self.chiffres.append(chiffre)
            self.capacite-=1
    

        
        
        
        
    
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
        chiffre = tige.pop()
        tigeDest.ajouterChiffre(chiffre)
            

#initialisation 
tige1 = Tige(
    [Chiffre('j',3),Chiffre('j', 2),Chiffre('j', 1)])
tige2 = Tige([Chiffre('b',3),Chiffre('b', 2),Chiffre('b', 1)])
tige3 = Tige()
#float('inf') pour definir infini
def ProfondeurBornee(s):



    
    
    
    
    
    