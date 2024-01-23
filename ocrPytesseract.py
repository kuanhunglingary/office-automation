#  Optical Character Recognition using python pytesseract module
from PIL import Image
import pytesseract

# Here we specified the path to our tessseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#This is the name of the image we have above 
img_name = 'D:/xxx/pic.jpg'

# Opening the image & storing it in an image object
img = Image.open(img_name)

# we will use this particular function to extract the text from the 
text = pytesseract.image_to_string(img, lang='chi_tra')

# We will display the result below