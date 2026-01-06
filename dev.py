from tkinter import Tk, simpledialog

root = Tk()
root.withdraw()  # hide main window
filename = simpledialog.askstring("Screenshot Name", "Enter screenshot name (without extension):")
root.destroy()
