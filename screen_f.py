import subprocess
import time

def start_screen_recording(output_file="screen_recording.mp4"):
    command = [
        "ffmpeg", "-y", "-f", "gdigrab", "-framerate", "30", "-i", "desktop", 
        "-c:v", "libx264", "-preset", "fast", "-pix_fmt", "yuv420p", output_file
    ]
    subprocess.Popen(command)  # Start the screen recording process in the background

def stop_screen_recording():
    # Send the stop signal (CTRL+C) to stop the ffmpeg process
    subprocess.run(["taskkill", "/IM", "ffmpeg.exe", "/F"])

# Example: Start recording
start_screen_recording(output_file="screen_recording.mp4")

# Sleep for 10 seconds (change this to however long you want to record)
time.sleep(10)

# Stop the recording after 10 seconds
stop_screen_recording()
