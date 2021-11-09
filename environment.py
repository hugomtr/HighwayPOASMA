#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:53:02 2021
@author: lucasaissaoui
"""

import numpy as np

class Environment: 
    def __init__(self, hauteur, largeur, canvas):
        self.env = np.zeros((hauteur, largeur))
        self.canvas = canvas
        
        # Tracer un mur
        self.env[210:220, 40:360] = 1
        

    def draw(self):
        for i in range(0, self.env.shape[0]): 
            for j in range(0, self.env.shape[1]):
                if self.env[i, j] == 1:
                    self.canvas.create_rectangle(i-0.5, j-0.5, i+0.5 , j+0.5, fill='black', outline='black')
        
    def free(self, x, y):
        return self.env[x][y] == 0