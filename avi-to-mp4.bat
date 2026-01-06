@echo off

set input_folder=A:\Users\-\0code

if not exist "%input_folder%\converted" mkdir "%input_folder%\converted"

for %%f in ("%input_folder%\*.avi") do (
    ffmpeg -i "%%f" -c:v libx264 -c:a aac -b:a 192k "%input_folder%\converted\%%~nf.mp4"
    move "%%f" "%input_folder%\converted"
)

echo Conversion complete.