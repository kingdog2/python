"""from gtts import gTTS
import os
tts = gTTS(text='warning warning warning warning warning warning warning', lang='en')
tts.save("nitoce.mp3")
"""
from playsound import playsound
playsound('nitoce.mp3', block=True)