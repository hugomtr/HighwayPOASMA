"""
@author: lucasaissaoui
"""

import math as mt
import position as ps

class Agent: 

    def __init__(self, x, y, xGoal, yGoal, canvas):
        # Position courante de l'agent 
        self.x = x
        self.y = y

        # Posoition but de l'agent 
        self.xGoal = xGoal
        self.yGoal = yGoal

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
        

    def moveToGoal(self, wl1):

        if not(self.x == self.xGoal and self.y == self.yGoal):
            # Dict de toutes le positions possibles 
            positions = {"up": ps.position(self.x, self.y-1, mt.sqrt(mt.pow(self.xGoal - self.x, 2) + mt.pow(self.yGoal - self.y - 1, 2))), 
                         "right": ps.position(self.x+1, self.y, mt.sqrt(mt.pow(self.xGoal - self.x + 1, 2) + mt.pow(self.yGoal - self.y, 2))), 
                         "down": ps.position(self.x, self.y+1, mt.sqrt(mt.pow(self.xGoal - self.x, 2) + mt.pow(self.yGoal - self.y + 1, 2))), 
                         "left": ps.position(self.x-1, self.y, mt.sqrt(mt.pow(self.xGoal - self.x - 1, 2) + mt.pow(self.yGoal - self.y, 2)))}
            
            # Dict des positions libre
            positionsFree = {}
            
            # On ajout les positions libres dict des positions libre (positionsFree)
            for p in positions : 
                if wl1.free(positions[p].getX(), positions[p].getY()):
                    positionsFree[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                    
                    
            # On recher la mailleure option parmis le positions libres
            action = ""
            h = 0
            
            for p in positionsFree: 
                if positionsFree[p].getH() > h: 
                    h = positionsFree[p].getH()
                    action = p
                    
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