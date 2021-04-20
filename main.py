import speech_recognition as sr # Importing speech recognition as 'sr' shorthand, rather than typing 'speechrecognition'
from time import ctime # Import to current time
import time # Import for time
import playsound # Import for the text to speech .mp3 sound (Cynthia)
import os
import random
from gtts import gTTS

import webbrowser

r = sr.Recognizer() # Importing the speech recogniser class
r.energy_threshold = 4000
# Source (Microphone) listening for audio and will return necessary responses based on what is said (Below) 
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            cynthia_speak(ask)
        audio = r.listen(source)
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
             cynthia_speak('Sorry I did not get that') # Error thrown is we do not give a correct command
    except sr.RequestError:
                cynthia_speak('Sorry, my speech service is down') # Error thrown if our voice command request fails
    return voice_data # Returns the correct answer to our command if everything works

def cynthia_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # gTTS (Google Text-to-Speech) saves the written command as .mp3 and uses the text to speak back
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
# Voice commands for us and responses from Cynthia below
def respond(voice_data):
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        cynthia_speak('Here is what I found for ' + search)
    if 'show me cases' in voice_data:
        url = 'https://vd-cases.netlify.app/'
        webbrowser.get().open(url)
        cynthia_speak('Here is the data for the cities in England with the highest covid cases')
    if 'show me deaths' in voice_data:
        url = 'https://vd-deaths.netlify.app/'
        webbrowser.get().open(url)
        cynthia_speak('Here are the death rates for the regions in England')
    if 'show me testing' in voice_data:
        url = 'https://vd-testing.netlify.app/'
        webbrowser.get().open(url)
        cynthia_speak('Here is the data for COVID testing in English cities')
    if 'show me vaccinations' in voice_data:
        url = 'https://vd-vaccinations.netlify.app/'
        webbrowser.get().open(url)
        cynthia_speak('Here is the data for the vaccination doses in the United Kingdom')
    if 'show me recoveries' in voice_data:
        url = 'https://vd-recoveries.netlify.app/'
        webbrowser.get().open(url)
        cynthia_speak('Here is the worldwide data for recoveries')
    if 'exit' in voice_data:
        exit()

# Makes Cynthia sleep/pause for one second to allow us to say something
time.sleep(1)
cynthia_speak('My name is Cynthia. What COVID data would you like to see today')
while 1:
    voice_data = record_audio()
    respond(voice_data)