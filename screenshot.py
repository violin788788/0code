import tkinter as tk
from PIL import ImageGrab
import os

filename = input("Enter screenshot name (without extension): ")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.3)
root.configure(bg="black")

canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

start_x = start_y = rect = None

def on_mouse_down(event):
    global start_x, start_y, rect
    start_x, start_y = event.x, event.y
    rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red")

def on_mouse_drag(event):
    canvas.coords(rect, start_x, start_y, event.x, event.y)

def on_mouse_up(event):
    x1 = min(start_x, event.x)
    y1 = min(start_y, event.y)
    x2 = max(start_x, event.x)
    y2 = max(start_y, event.y)
    root.destroy()
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    save_directory = r"A:\Users\-\Downloads"
    

    save_file = os.path.join(save_directory, f"{filename}.png")
    img.save(save_file)


    #img.save(f"{filename}.png")

canvas.bind("<ButtonPress-1>", on_mouse_down)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_mouse_up)
root.mainloop()
os.startfile(r"A:\Users\-\Downloads")
