from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"A:\Program Files\Tesseract-OCR\tesseract.exe"
image = Image.open("fdr.png")
text = pytesseract.image_to_string(image)
print(text)
