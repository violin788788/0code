import cv2,mss,numpy as np,time
from pynput import keyboard
import os
name=input("Save name (no extension): ")
print("press enter after you put name in")
print("click space to end recording")
stop=False
ix=iy=fx=fy=-1
drag=False
FPS=30
def on_press(key):
    global stop
    if key==keyboard.Key.space:stop=True
keyboard.Listener(on_press=on_press).start()
def mouse(event,x,y,flags,param):
    global ix,iy,fx,fy,drag
    if event==cv2.EVENT_LBUTTONDOWN:ix,iy=x,y;drag=True
    elif event==cv2.EVENT_MOUSEMOVE and drag:fx,fy=x,y
    elif event==cv2.EVENT_LBUTTONUP:fx,fy=x,y;drag=False
sct=mss.mss()
mon=sct.monitors[1]
cv2.namedWindow("Select Area",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Select Area",mouse)
frame=np.array(sct.grab(mon))
while fx==-1 or drag:
    show=frame.copy()
    if ix!=-1 and fx!=-1:cv2.rectangle(show,(ix,iy),(fx,fy),(255,0,0),2)
    cv2.imshow("Select Area",show)
    cv2.waitKey(1)
cv2.destroyAllWindows()
x=min(ix,fx);y=min(iy,fy);w=abs(fx-ix);h=abs(fy-iy)
region={"left":x,"top":y,"width":w,"height":h}
save_directory=os.path.join(os.path.expanduser("~"),"Downloads")
os.makedirs(save_directory,exist_ok=True)
out_file=os.path.join(save_directory,name+".mp4")
out=cv2.VideoWriter(out_file,cv2.VideoWriter_fourcc(*"mp4v"),FPS,(w,h))
frame_time=1/FPS
next_time=time.time()
while not stop:
    img=np.array(sct.grab(region))
    out.write(img[:,:,:3])
    next_time+=frame_time
    sleep=next_time-time.time()
    if sleep>0:time.sleep(sleep)
out.release()
os.startfile(save_directory)
