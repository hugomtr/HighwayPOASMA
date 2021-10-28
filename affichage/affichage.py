import math
import tkinter as tk
import numpy as np

# Fonction qui dessin un cercle de centre (x, y) et de rayon r
def draw_circle(x, y, r):
    canvas.create_oval(x - r, y - r , x + r, y + r)