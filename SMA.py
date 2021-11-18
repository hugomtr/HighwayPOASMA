#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:45:23 2021

@author: oem
"""

import environment as env
import agent as agt

class SMA: 
    def __init__(self, nbAgents, file, goal, canvas):
        self.canvas = canvas
        
        self.env = env.Environment(file, canvas)
        self.env.draw()
        
        ## Réseau d'agent ##
        self.a1 = agt.Agent(130, 260, 350, 20, self.env.xShape(),  self.env.yShape(),  canvas)
        #self.a2 = agt.Agent(50, 170, 380, 380, self.env.xShape(),  self.env.yShape(), canvas)
        #self.a3 = agt.Agent(350, 50, 30, 370, self.env.xShape(),  self.env.yShape(), canvas)
        #self.a4 = agt.Agent(200, 310, 90, 90, self.env.xShape(),  self.env.yShape(), canvas)


        # Ensemble d'agents
        self.agents = [self.a1] #, self.a2, self.a3, self.a4]
        
    def moveToGoal(self):
        for a in self.agents:
            a.moveToGoal(self.env)