import speech_recognition as sr 
from google_trans_new import google_translator
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()
#Listening part - voice input (step 1 )
with sr.Microphone() as source:
    print("Clearing the background noises...")
    r.adjust_for_ambient_noise(source,duration=1)
    #print("Speak Now!!")
    audio = r.listen(source,timeout=1)
    print("Done Recording")
    try:
        print("Recognizing...")
        speech_text = r.recognize_google(audio,language='en')
        print(speech_text)
    except sr.UnknownValueError:
        print("Could not understand. Please speak clearly")
    except sr.RequestError:
        print("Could not find the requested result from Google. Please try again")
    except Exception as ex:
        print(ex)

    #Translation part (step 2)
    def translate():
        langinput = input("Type the language code in which you want to translate: ")
        translator= google_translator()
        translated_text = translator.translate(str(speech_text), lang_tgt= str(langinput))
        print(translated_text.text)
    # Voice output (step 3)
        engine.say(str(translated_text))
        engine.runAndWait()
    translate()
      

