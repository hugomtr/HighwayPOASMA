#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:01:03 2021

@author: lucasaissaoui
"""

import math as mt
import position as ps
import random

x = 1
y = 2
xGoal = 34
yGoal = 3

positions = {"up": ps.position(x, y-1, mt.sqrt(mt.pow(xGoal - x, 2) + mt.pow(yGoal - y - 1, 2))), 
             "right": ps.position(x+1, y, mt.sqrt(mt.pow(xGoal - x + 1, 2) + mt.pow(yGoal - y, 2))), 
             "down": ps.position(x, y+1, mt.sqrt(mt.pow(xGoal - x, 2) + mt.pow(yGoal - y + 1, 2))), 
             "left": ps.position(x-1, y, mt.sqrt(mt.pow(xGoal - x - 1, 2) + mt.pow(yGoal - y, 2)))}


tmp = list(positions.keys())

print(tmp)

print(random.choice(tmp))







# import matplotlib.pyplot as plt 

# from PIL import Image
# im = Image.open("lab.png")
# im.show()

# print(type(im))

# face = np.array(im)

# plt.imshow(face)
# plt.show()  

# # load and display an image with Matplotlib
# from matplotlib import image
# from matplotlib import pyplot
# # load image as pixel array
# image = image.imread("lab2.png")
# # summarize shape of the pixel array
# print(type(image))
# print(image.dtype)
# print(image.shape)
# # display the array of pixels as an image
# #pyplot.imshow(image)
# #pyplot.show()

# rgb_weights = [0.2989, 0.5870, 0.1140]

# env = np.dot(image[...,:3], rgb_weights)

# pyplot.imshow(env, cmap=pyplot.get_cmap("gray"))
# pyplot.show()

# print(env.shape)
# print(env)

# for i in range(0, env.shape[0]): 
#     for j in range(0,env.shape[1]):
#         if env[i, j] < 0.5:
#             env[i, j] = 1
#         else :
#             env[i, j] = 0


# print(env.shape)
# print(env)
