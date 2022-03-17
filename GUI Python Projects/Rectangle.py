from tkinter import  *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_rectangle(  0,   0, 150, 150, fill="yellow")
canvas.create_rectangle(100,  50, 250, 100, fill="orange", width=5)
canvas.create_rectangle( 50, 100, 150, 200, fill="green", outline="red", width=3)
canvas.create_rectangle(125,  25, 175, 190, fill="purple", width=0)
root.mainloop()
