
#This code works for bookPages 
#pytesseract is an open source module used to detect 100 languages
import pytesseract
from PIL import Image
from gtts import gTTS 
import os 
pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files (x86)/Tesseract-OCR/tesseract"
img=Image.open('page2.jpg')
text=pytesseract.image_to_string(img)
print(text)
# The text that you want to convert to audio 
#we are using the google speech to text to convert the text into audio
mytext = text
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("welcome.mp3")