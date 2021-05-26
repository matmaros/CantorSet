
import tkinter as tk

#setup
root = tk.Tk()
canvas = tk.Canvas(root,width=800,height=600,background='white')
canvas.grid(row=0,column=0) 

def cantor_set(x,y,L,yStep=25):
    if L >= 3:
        canvas.create_line(x,y,x+L,y,fill='blue', width=5) 
        y += yStep
        cantor_set(x,y,L/3)
        cantor_set(x+2/3*L,y,L/3)

cantor_set(0,10,800)

root.mainloop()