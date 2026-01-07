import tkinter as tk
from tkinter import simpledialog
import cv2, os
import numpy as np
import pyautogui
import time
import keyboard
root = tk.Tk()
root.withdraw()
def select_region(image):
    screen_width, screen_height = pyautogui.size()
    image_resized = cv2.resize(image, (screen_width, screen_height))
    cv2.namedWindow("Select Region", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Select Region", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    r = cv2.selectROI("Select Region", image_resized, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    return r
def select_filename():
    return simpledialog.askstring("File Name", "Enter name for the capture file:")
name_capture = select_filename()
if not name_capture:
    print("No filename provided. Exiting.")
    exit()
print("Press space to stop recording.")
print("Drag and drop the selection for the region to keep on the screen that pops up after.")
print("Hit space for it to go to the Downloads folder.")
screen_width, screen_height = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
out = cv2.VideoWriter('screen_record.mp4', fourcc, fps, (screen_width, screen_height))
start_time = time.time()
while True:
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
    if keyboard.is_pressed('space'):
        print("Recording stopped by user.")
        break
out.release()
cap = cv2.VideoCapture('screen_record.mp4')
ret, frame = cap.read()
if ret:
    region = select_region(frame)
    x, y, w, h = region
    out_cropped = cv2.VideoWriter(os.path.join("A:\\Users\\-\\Downloads", f"{name_capture}.mp4"), fourcc, fps, (w, h))
    while ret:
        ret, frame = cap.read()
        if not ret:
            break
        cropped_frame = frame[y:y+h, x:x+w]
        out_cropped.write(cropped_frame)
    out_cropped.release()
cap.release()

final=f"A:\\Users\\-\\Downloads\\{name}.mp4"
subprocess.call(f'ffmpeg -y -i "{crop}" -c:v libx264 -pix_fmt yuv420p -movflags +faststart "{final}"',shell=True)

cv2.destroyAllWindows()
os.delete('screen_record.mp4')
os.startfile(os.path.dirname(final))

#os.startfile(os.path.dirname(os.path.join("A:\\Users\\-\\Downloads", f"{name_capture}.mp4")))
   