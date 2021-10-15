# Fonction qui dessin un cercle de centre (x, y) et de rayon r
def draw_circle(x, y, r):
    canvas.create_oval(x - r, y - r , x + r, y + r)
   
   
# Fonction qui dessin un tableau tab sous forme de cercle (Revoir la robustesse de la fonction)
def array_roller(tab, x, y, r):
    step = (2 * math.pi) / len(tab)
    i = 0
   
    for e in range(0, len(tab)):
        if tab[e] == 1 :
            draw_circle(x + r * math.cos(i), y + r * math.sin(i), 2)
            tab[e] += 1
           
        i += step
       
# Event keypress intevent lors d'une touche clavier
def keypress(event):
    global dep
    tab[dep] = 1
    dep = dep + 1
    array_roller(tab, x, y, r)

## MISE EN PLACE DE L'INTERFACE GRAPHIQUE
root = tk.Tk()
canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()


## DEFINITION DES VARIABLES
tab = np.zeros((350))
dep = 0        
x = 400
y = 400
r = 200


#Tracer la "route"
draw_circle(x, y, r - 5)
draw_circle(x, y, r + 5)

#Event qui intervient à chaque frappe au clavier
root.bind("<Key>", keypress)
root.mainloop()

### Lucas Aissaoui ###




