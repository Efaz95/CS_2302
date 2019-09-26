import time
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width='500', height='500')
canvas.pack() 

rec = canvas.create_rectangle(10, 250, 60, 300, fill='blue', outline='red', width='8')

# Bonus section included
for x in range(30):
	y = x = 5
	time.sleep(0.025)
	canvas.move(rec, x, -y)
	canvas.update()

for x in range(30):
	y = x = 5
	time.sleep(0.025)
	canvas.move(rec, x, y)
	canvas.update()

for x in range(30):
	y = x = 5
	time.sleep(0.025)
	canvas.move(rec, -x, y)
	canvas.update()

for x in range(30):
	y = x = 5
	time.sleep(0.025)
	canvas.move(rec, -x, -y)
	canvas.update()


root.mainloop()