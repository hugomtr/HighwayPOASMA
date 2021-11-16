import tkinter as tk
import agent as agt
import wall as wl

import environment as env

## MISE EN PLACE DE L'INTERFACE GRAPHIQUE
windowSize = 600

root = tk.Tk()
canvas = tk.Canvas(root, height=windowSize, width=windowSize, bg='white')
canvas.pack()

a1 = agt.Agent(130, 260, 350, 20, canvas)
a2 = agt.Agent(50, 170, 380, 380, canvas)
a3 = agt.Agent(350, 50, 30, 370, canvas)
a4 = agt.Agent(200, 310, 90, 90, canvas)

env1 = env.Environment("lab2.png", canvas)
env1.draw()

# Ensemble d'agent
agents = [a1, a2, a3, a4]

# Events pour les touches Entrer et les fleches
def keypressReturn(env):
    for a in agents:
        a.moveToGoal(env1)

def keypressLeft(event):
    for a in agents:
        a.left()

def keypressRight(event):
    for a in agents:
        a.right()

def keypressUp(event):
    for a in agents:
        a.up()

def keypressDown(event):
    for a in agents:
        a.down()

def keypressSpace(event): 
    autoRun()

def autoRun():
    for a in agents:
        a.moveToGoal(env1)

    root.after(15, autoRun)

#Event qui intervient à chaque frappe au clavier
root.bind("<Return>", keypressReturn)
root.bind("<Left>", keypressLeft)
root.bind("<Right>", keypressRight)
root.bind("<Up>", keypressUp)
root.bind("<Down>", keypressDown)
root.bind("<r>", keypressSpace)



root.mainloop()