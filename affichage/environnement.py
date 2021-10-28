#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:53:02 2021
@author: lucasaissaoui
"""

import numpy as np


class Environment: 
    def __init__(self, hauteur, largeur):
        self.env = np.zeros((hauteur, largeur))

    def draw(self):
        print(self.env)