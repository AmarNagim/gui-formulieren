import tkinter as tk

size = 30

window = tk.Tk()

canvas = tk.Canvas(window)
canvas.pack()

color = 'black'

for y in range(8):

    for x in range(8):
        x1 = x*size
        y1 = y*size
        x2 = x1 + size
        y2 = y1 + size
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'

    if color == 'white':
        color = 'black'
    else:    
        color = 'white'
        
window.mainloop() 