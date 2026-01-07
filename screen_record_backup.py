import tkinter as tk, cv2, numpy as np, pyautogui, time, keyboard, os, subprocess
from tkinter import simpledialog
root=tk.Tk()
root.withdraw()
def select_region(image):
    w,h=pyautogui.size()
    img=cv2.resize(image,(w,h))
    cv2.namedWindow("Select Region",cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Select Region",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    r=cv2.selectROI("Select Region",img,fromCenter=False,showCrosshair=True)
    cv2.destroyAllWindows()
    return r
def select_filename():
    return simpledialog.askstring("File Name","Enter name for the capture file:")
name_capture=select_filename()
if not name_capture: print("No filename provided. Exiting."); exit()
print("Press space to stop recording. Drag selection for region after.")
w,h=pyautogui.size()
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
fps=30
temp_file='screen_record.mp4'
out=cv2.VideoWriter(temp_file,fourcc,fps,(w,h))
while True:
    frame=np.array(pyautogui.screenshot())
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    out.write(frame)
    if keyboard.is_pressed('space'): print("Recording stopped."); break
out.release()
cap=cv2.VideoCapture(temp_file)
ret,frame=cap.read()
if ret:
    x,y,w1,h1=select_region(frame)
    cropped_file=os.path.join(os.path.expanduser("~"),"Downloads",f"{name_capture}.mp4")
    out_cropped=cv2.VideoWriter(cropped_file,fourcc,fps,(w1,h1))
    while ret:
        ret,frame=cap.read()
        if not ret: break
        out_cropped.write(frame[y:y+h1,x:x+w1])
    out_cropped.release()
cap.release()
final=os.path.join(os.path.expanduser("~"),"Downloads",f"{name_capture}_final.mp4")
subprocess.call(f'ffmpeg -y -i "{cropped_file}" -c:v libx264 -pix_fmt yuv420p -movflags +faststart "{final}"',shell=True)
os.remove(temp_file)
os.startfile(os.path.dirname(final))
