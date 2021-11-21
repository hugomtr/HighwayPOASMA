"""
@author: lucasaissaoui
"""

import math as mt
import position as ps
import numpy as np
import random 

class Agent: 
    
    def __init__(self, x, y, xGoal, yGoal, xMemory, yMemory, canvas):
        # Position courante de l'agent 
        self.x = x
        self.y = y

        # Posoition but de l'agent 
        self.xGoal = xGoal
        self.yGoal = yGoal
        
        # Initialisation de la mémmoire
        self.xMemory = xMemory
        self.yMemory = yMemory
        # Les positions non-exploré valent 0, deje exploré 1 et interdite 2
        self.memory = np.zeros((self.xMemory, self.yMemory))
        #Pledge
        
        self.Pledge = False

        # Constante d'affichage
        self.aRadius = 2#0.5
        self.sRadius = 4

        self.canvas = canvas
        self.goalDraw =  self.canvas.create_oval(self.xGoal - self.sRadius, self.yGoal - self.sRadius , self.xGoal + self.sRadius, self.yGoal + self.sRadius, outline='green')
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill='blue', outline='blue')


    def up(self):
        self.eraseAgent()
        self.y = self.y - 1
        self.drawAgent()

    def down(self): 
        self.eraseAgent()
        self.y = self.y + 1
        self.drawAgent()

    def left(self): 
        self.eraseAgent()
        self.x = self.x - 1
        self.drawAgent()

    def right(self): 
        self.eraseAgent()
        self.x = self.x + 1
        self.drawAgent()
        
    def positionNonExplore(self, x, y): 
        return self.memory[x, y] == 0
    
    def positionExplore(self, x, y): 
        return self.memory[x, y] == 1
    
    def memoriserPosition(self): 
        self.memory[self.x][self.y] = 1
        
    def supprimerPosition(self, x, y): 
        self.memory[x][y] = 2
    
    def rightTo(self, pos): 
        if pos == "up":
            return "right"
        elif pos == "right":
            return "down"
        elif pos == "down": 
            return "left"
        elif pos == "left": 
            return "up"

    def moveToGoal(self, env):
        if not(self.x == self.xGoal and self.y == self.yGoal):
            #Memoriser une position 
            self.memoriserPosition()
            
            self.step = 1
            
            
            # Dict de toutes le positions possibles 
            positions = {"up": ps.position(self.x, self.y-self.step, mt.sqrt(mt.pow(self.xGoal - self.x, 2) + mt.pow(self.yGoal - self.y - self.step, 2))), 
                         "right": ps.position(self.x+self.step, self.y, mt.sqrt(mt.pow(self.xGoal - self.x + self.step, 2) + mt.pow(self.yGoal - self.y, 2))), 
                         "down": ps.position(self.x, self.y+1, mt.sqrt(mt.pow(self.xGoal - self.x, 2) + mt.pow(self.yGoal - self.y + self.step, 2))), 
                         "left": ps.position(self.x-self.step, self.y, mt.sqrt(mt.pow(self.xGoal - self.x - self.step, 2) + mt.pow(self.yGoal - self.y, 2)))}
            
            # Dict des positions possible
            positionsPossible = {}
            
            # Dict des positions Impossible
            positionsImpossible = {}
            
            # Dcit des positions non-explore
            positionsNonExplore = {}
            
            # On ajout les positions libres dict des positions libre (positionsPossible)
            for p in positions : 
                if env.free(positions[p].getX(), positions[p].getY()):
                    positionsPossible[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                else : 
                    positionsImpossible[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                    
            # On ajout les positions pas encore exploré
            for p in positionsPossible : 
                if self.positionNonExplore(positions[p].getX(), positions[p].getY()): 
                    positionsNonExplore[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                    
            # On recher la mailleure option parmis le positions libres
            action = ""
            h = 0
            
            # TEST Choisir dans les positions non-explore
            
            #Meilleure heristique des positions libre
            # for p in positionsPossible: 
            #     if positionsPossible[p].getH() > h: 
            #         h = positionsPossible[p].getH()
            #         action = p
            
            # Suivre le mur (ne fonctionne pas, il faut l'implementer d'une autre manière)
            #action = list(positionsPossible.keys())[0]
            
            if bool(positionsNonExplore): 
            # Meilleure heuristique des positions non-explore
                for p in positionsNonExplore: 
                    if positionsNonExplore[p].getH() > h: 
                        h = positionsNonExplore[p].getH()
                        action = p
                        #self.Pledge = False
            else : # Algo de Pledge
                if bool(positionsImpossible): 
                    action = self.rightTo(list(positionsImpossible.keys())[-1]) 
                    
                    while action in positionsImpossible:
                        action = self.rightTo(action)
                    
                else : 
                    action = str(random.choice(list(positionsPossible.keys())))
            
                # Aller vers la position qui me rapproche le plus 
                # if not bool(positionsImpossible) and self.Pledge == False: 
                #     action = "up"
                #     self.Pledge = True
                # elif not bool(positionsImpossible) and self.Pledge == True: 
                #     if bool(positionsImpossible): 
                #         actionIMP = next(iter(positionsImpossible))
                    
                #     action = self.rightTo(actionIMP)
                #     actionR = self.rightTo(action)
                #     actionRR = self.rightTo(actionR)
                            
                #     # Si mon action est possible je la réalise
                #     if env.free(positions[action].getX(), positions[action].getY()): 
                #         action = action 
                #     elif env.free(positions[actionR].getX(), positions[actionR].getY()):
                #         action = actionR
                #     elif env.free(positions[actionRR].getX(), positions[actionRR].getY()): 
                #         action = actionRR
                    
                
                
                
                
                
                        # Trop long et trop gourmand
            # else : # Choisir une action au hasard
            #       action = str(random.choice(list(positionsPossible.keys())))
            
                        # Peut encore bloquer
            # else: # Choisir la position qui nous éloigne le plus 
            #     print("eloigner")
            #     h = 99999999
            #     for p in positionsPossible: 
            #         if positionsPossible[p].getH() < h: 
            #             h = positionsPossible[p].getH()
            #             action = p
                   
            
            # Hasard parmis non-exploré
            #action = random.choice(positionsNonExplore.keys())
            
            
            # On execut l'actions qui a été selectionné
            if action == "up":
                self.up()
            elif action == "right":
                self.right()
            elif action == "down": 
                self.down()
            elif action == "left": 
                self.left()


    def drawAgent(self):
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill='blue', outline='blue' )

    def eraseAgent(self): 
        self.canvas.delete(self.agentDraw)