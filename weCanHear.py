
from gtts import gTTS
import os
readtext="Hello weCanHear, It is a great platform where you can listen the speech which is present in text, Thankyou for hearing."
language = 'en'
inst = gTTS(text=readtext, lang=language, slow=False)
inst.save("myfile.mp3")
os.system("myfile.mp3")
