#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:01:03 2021

@author: lucasaissaoui
"""

import numpy as np 

mat = np.zeros((10, 7))

mat[3:5, 3:5] = 1

print(mat.shape[0])