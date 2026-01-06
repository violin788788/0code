import tkinter as tk
import subprocess

# Global variables to store coordinates
start_x, start_y = 0, 0
dragging = False
region = None

# Mouse callback function to handle dragging
def on_mouse_drag(event):
    global start_x, start_y, dragging, region
    if dragging:
        # Update region and redraw the rectangle
        region = (start_x, start_y, event.x - start_x, event.y - start_y)
        canvas.delete("all")
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2)

# Mouse button press function to start the drag
def on_mouse_press(event):
    global start_x, start_y, dragging
    dragging = True
    start_x, start_y = event.x, event.y

# Mouse button release function to stop dragging and capture the screenshot
def on_mouse_release(event):
    global dragging, region
    dragging = False
    if region[2] > 0 and region[3] > 0:
        # After the user selects a region, capture it with ffmpeg
        capture_region(region)
        root.quit()  # Close the tkinter window after selecting the region

# Function to capture the selected region using ffmpeg
def capture_region(region):
    x, y, width, height = region
    command = ["ffmpeg", "-y", "-f", "gdigrab", "-framerate", "1", "-i", f"desktop={x},{y},{width},{height}", "-vframes", "1", "screenshot.png"]
    subprocess.run(command)
    print("Screenshot saved as 'screenshot.png'")

# Tkinter window setup
root = tk.Tk()
root.title("Drag and Select Region")
root.geometry("600x400")
root.resizable(False, False)

# Create a canvas to capture the drag and drop
canvas = tk.Canvas(root, width=600, height=400, bg="lightgray")
canvas.pack()

# Bind mouse events for dragging
canvas.bind("<ButtonPress-1>", on_mouse_press)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_mouse_release)

# Start tkinter event loop
root.mainloop()
