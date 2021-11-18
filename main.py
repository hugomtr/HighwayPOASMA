import tkinter as tk
import SMA 

## MISE EN PLACE DE L'INTERFACE GRAPHIQUE
windowSize = 600

root = tk.Tk()
canvas = tk.Canvas(root, height=windowSize, width=windowSize, bg='white')
canvas.pack()

sma1 = SMA.SMA(1, "lab2.png", 2, canvas)

# Events pour les touches Entrer et les fleches
def keypressSpace(event): 
    autoRun()

def autoRun():
    sma1.moveToGoal()

    root.after(1, autoRun)

#Event qui intervient à chaque frappe au clavier
root.bind("<r>", keypressSpace)



root.mainloop()