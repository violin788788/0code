import threading
import time
import tkinter as tk
import mss, cv2, numpy as np
recording = False
def record():
    global recording
    fps = 30
    frame_time = 1 / fps
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        out = cv2.VideoWriter(
            "recording.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (monitor["width"], monitor["height"])
        )
        while recording:
            start = time.time()
            img = sct.grab(monitor)
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)
            out.write(frame)
            time.sleep(max(0, frame_time - (time.time() - start)))
        out.release()
        # When recording stops, show a message
        show_message("Recording Complete! File saved as 'recording.mp4'")
def start_recording():
    global recording
    recording = True
    threading.Thread(target=record, daemon=True).start()
def stop_recording():
    global recording
    recording = False
def show_message(message):
    # Create a new window with the message
    message_window = tk.Toplevel()
    message_window.title("Recording Status")
    message_window.geometry("250x100")
    label = tk.Label(message_window, text=message)
    label.pack(pady=20)
    # Button to close the message window
    button = tk.Button(message_window, text="Close", command=message_window.destroy)
    button.pack(pady=10)
root = tk.Tk()
root.title("Screen Recorder")
# Start and Stop buttons
tk.Button(root, text="Start", command=start_recording).pack(padx=20, pady=10)
tk.Button(root, text="Stop", command=stop_recording).pack(padx=20, pady=10)
root.mainloop()
