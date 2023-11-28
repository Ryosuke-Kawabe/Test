import tkinter as tk

def animation():
    canvas.move(head, 10, 0)
    canvas.move(body, 10, 0)
    canvas.move(left_arm, 10, 0)
    canvas.move(right_arm, 10, 0)
    canvas.move(left_leg, 10, 0)
    canvas.move(right_leg, 10, 0)
    
    root.after(50, animation)

root = tk.Tk()
root.title("Image")

canvas = tk.Canvas(root, width=700, height=400)
canvas.pack()

head = canvas.create_oval(80, 50, 120, 90, outline="black", width=2)

body = canvas.create_line(100, 90, 100, 150, fill="black", width=2)

left_arm = canvas.create_line(100, 110, 60, 90, fill="black", width=2)
right_arm = canvas.create_line(100, 110, 140, 90, fill="black", width=2)

left_leg = canvas.create_line(100, 150, 60, 190, fill="black", width=2)
right_leg = canvas.create_line(100, 150, 140, 190, fill="black", width=2)


animation()

root.mainloop()
