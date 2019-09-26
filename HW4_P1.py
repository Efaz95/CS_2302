import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400) 
canvas.pack() 


canvas.create_rectangle(140, 170, 250, 250, fill='blue', outline='blue')

canvas.create_rectangle(180, 140, 250, 200, fill='yellow', outline='yellow')

canvas.create_rectangle(140, 120, 150, 188, fill='green', outline='green')

points = [120, 120, 170, 120, 145, 85, 120, 120]
canvas.create_polygon(points, fill='red', outline='red')

canvas.create_oval(120,220,170,270, fill='black')
canvas.create_oval(220,220,270,270, fill='black')

canvas.create_arc(150, 55, 185, 90, start=0, extent=120, fill='grey')
canvas.create_arc(180, 35, 215, 70, start=0, extent=120, fill='grey')

root.mainloop()