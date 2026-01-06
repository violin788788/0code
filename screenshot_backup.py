import mss
import numpy as np
import cv2
start_x, start_y = 0, 0
dragging = False
selected_region = None
def select_region(event, x, y, flags, param):
    global start_x, start_y, dragging, selected_region
    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            img = np.array(mss.mss().grab(mss.mss().monitors[1]))
            img = cv2.rectangle(img, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow("Select Area", img)
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        selected_region = (start_x, start_y, x - start_x, y - start_y)
        cv2.destroyAllWindows()
        if selected_region[2] > 0 and selected_region[3] > 0:
            take_screenshot(selected_region)
def take_screenshot(region):
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2BGR)
        cv2.imwrite("screenshot.png", screenshot_bgr)
        print("Screenshot saved as 'screenshot.png'")
def select_area_to_capture():
    cv2.imshow("Select Area", np.zeros((1, 1)))
    cv2.setMouseCallback("Select Area", select_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
select_area_to_capture()
