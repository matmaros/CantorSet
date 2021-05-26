
import tkinter as tk

#setup
root = tk.Tk()
canvas = tk.Canvas(root,width=800,height=600,background='white')
canvas.grid(row=0,column=0) #use instead of pack() - places canvas into 'root'window

#L_system variables and logic
row = ['_'] #seed row
final_rows = [] #store final set rows for L system
iters = 6 #set number of iterations

for i in range(iters):

    final_rows.append(row)    
    new_row = []

    for j in range(len(row)): #<<< range(len(row)) - secret sauce ;)
        
        if row[j] == '_':
            new_row.extend('_ _')
        else:
            new_row.extend('   ')

    row = new_row         

#draw lines
length = 3**iters
for i, row in enumerate(final_rows):
    line_length = length/len(row)
    
    SP = [25,25+(25*i)] #reset SP for new row

    for seg in row:
        x1 = SP[0]
        y1 = SP[1]
        x2 = SP[0] + line_length
        y2 = SP[1]
        if seg == '_':
            canvas.create_line(x1,y1,x2,y2,fill='blue', width=5)
        else:
            canvas.create_line(x1,y1,x2,y2,fill='white', width=1)

        SP = [x2,y2] #reset SP to build off previous line in row

root.mainloop()



