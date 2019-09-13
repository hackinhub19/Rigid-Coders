from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import pytesseract
from PIL import Image
from gtts import gTTS 
import os 
import cv2
from imutils.object_detection import non_max_suppression
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
       
        cam = cv2.VideoCapture(0)

        ret,frame=cam.read()
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img_name="IMG_{}.png".format(timestr)
        print("{} written!".format(img_name))
        cv2.imwrite(img_name, frame)
        cam.release()
        cv2.destroyAllWindows()
        pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files (x86)/Tesseract-OCR/tesseract"
        img=Image.open(img_name)
        text=pytesseract.image_to_string(img)
        print(text)
            #frame = imutils.resize(frame, width=1000)
        mytext = text
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("welcome.mp3") 
        os.system("welcome.mp3")
        print("Captured")
       
        

class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()