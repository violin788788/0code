from PIL import Image

# Open an image
image = Image.open("screenshot.png")

# Save as .ico format
image.save("screenshot.ico", format="ICO")
