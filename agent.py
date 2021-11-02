"""
@author: lucasaissaoui
"""

import numpy as np
import math as mt

import wall as wl
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

        if self.x == self.xGoal and self.y == self.yGoal:
            print("Goal")
        else:
            actions = {"up": 0, "right": 0, "down": 0, "left": 0}
            
            p0 = ps.position(self.x, self.y-1)
            p1 = ps.position(self.x+1, self.y)
            p2 = ps.position(self.x, self.y+1)
            p3 = ps.position(self.x-1, self.y)
            
            positions = {"up": p0, "right": p1, "down": p2, "left": p3}
            
            actions["up"] = mt.sqrt(mt.pow(self.xGoal - self.x, 2) + mt.pow(self.yGoal - self.y - 1, 2))
            actions["right"] = mt.sqrt(mt.pow(self.xGoal - self.x + 1, 2) + mt.pow(self.yGoal - self.y, 2))
            actions["down"] = mt.sqrt(mt.pow(self.xGoal - self.x, 2) + mt.pow(self.yGoal - self.y + 1, 2))
            actions["left"] = mt.sqrt(mt.pow(self.xGoal - self.x - 1, 2) + mt.pow(self.yGoal - self.y, 2))
            
            for p in positions : 
                if wl1.free(positions[p].getX(), positions[p].getY()) == False:
                    actions.pop(p)
                    
                    
            
            # Supprime les positions impossible
            
            #for a in actions :
             #   if 
            

            action = max(actions, key=actions.get)
            #print("Dirs : ", dirs)
            #print("Dir : ", dirToGo)

            if action == "up":
                self.up()
            elif action == "right":
                self.right()
            elif action == "down": 
                self.down()
            elif action == "left": 
                self.left()
            
            print(wl1.free(self.x, self.y))


    def drawAgent(self):
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill='blue', outline='blue' )

    def eraseAgent(self): 
        self.canvas.delete(self.agentDraw)