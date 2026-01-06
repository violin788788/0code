import cv2,os
import numpy as np
import pyautogui
import time
import keyboard
def select_region(image):
    screen_width, screen_height = pyautogui.size()  # Get screen resolution
    image_resized = cv2.resize(image, (screen_width, screen_height))  # Resize the image to fit the screen resolution
    # Create a full-screen window for ROI selection
    cv2.namedWindow("Select Region", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Select Region", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    r = cv2.selectROI("Select Region", image_resized, fromCenter=False, showCrosshair=True)  # Open ROI at top-left corner
    #r = cv2.setMouseCallback("Select Region", image_resized, fromCenter=False, showCrosshair=True)  # Open ROI at top-left corner
    cv2.destroyAllWindows()
    return r
print("")  
name_capture = input("Type name of capture file? = ")  
print("")  
print("Press space to stop recording")
print("") 
print("drag and drop what to keep on the screen that pops up after")
print("") 
print("hit space for it to go to the downloads folder")
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
    if keyboard.is_pressed('space'):  # Stop recording when Spacebar is pressed
        print("Recording stopped by user.")
        break
out.release()
cap = cv2.VideoCapture('screen_record.mp4')
folder_save = r"A:\Users\-\Downloads"
out_file = folder_save+"\\"+name_capture+".mp4"
ret, frame = cap.read()
if ret:
    region = select_region(frame)  # Let the user select the region without the window going off-screen
    x, y, w, h = region
    #out_cropped = cv2.VideoWriter('screen_record_cropped.mp4', fourcc, fps, (w, h))
    out_cropped = cv2.VideoWriter(out_file, fourcc, fps, (w, h))
    while ret:
        ret, frame = cap.read()
        if not ret:
            break
        cropped_frame = frame[y:y+h, x:x+w]
        out_cropped.write(cropped_frame)
    out_cropped.release()
cap.release()
cv2.destroyAllWindows()
os.startfile(r"A:\Users\-\Downloads")
