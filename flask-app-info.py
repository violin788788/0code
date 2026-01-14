# A very simple Flask Hello World app for you to get started with...
#from flask import Flask

from flask import Flask, render_template, request, send_file
from pydub import AudioSegment
import os,webbrowser,subprocess,sys
#from flask import Flask, render_template
app = Flask(__name__)
os.makedirs('uploads', exist_ok=True)
UPLOAD_FOLDER = 'uploads'
@app.route('/', methods=['GET', 'POST'])
#@app.route('/')
def run():
    if request.method == 'POST':
        # Get uploaded file and form inputs
        file = request.files['audio']
        start_time = int(request.form['start_time'])
        end_time = int(request.form['end_time'])
        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        # Load audio and clip it
        audio = AudioSegment.from_file(file_path)
        clipped_audio = audio[start_time*1000:end_time*1000]  # Clip in milliseconds
        # Save clipped audio
        clipped_path = 'clipped_audio.wav'
        clipped_audio.export(clipped_path, format='wav')
        # Send the clipped audio file as a response
        return send_file(clipped_path, as_attachment=True)
    files = os.listdir(UPLOAD_FOLDER)
    # Default rendering of the form
    return render_template('info.html', files=files)
"""
python anywhere does not get this last bit of code
will not work in python anywhere with this
"""

# Path to your Chrome executable
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust this path if needed
# URL you want to open
url = "http://127.0.0.1:5000/"
# Run Chrome with incognito mode and the URL
subprocess.Popen([chrome_path, '--incognito', url])
#subprocess.Popen([chrome_path, "http://127.0.0.1:5000"])
if __name__ == '__main__':
    app.run(debug=True)



"""
python anywhere does not get this last bit of code
will not work in python anywhere with this
"""
    