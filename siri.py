import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
from plyer import notification
def nfm(mess):
    notification.notify(title='siri',message=mess,app_icon=None,timeout = 10)
    
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

print("youtube")
#while True:
#    x=input("search ... ")
#    #pywhatkit.playonyt(x)
#    pywhatkit.search(x)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take():
    try:
        with sr.Microphone() as source:
            nfm("listening")
            print("listening..")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'hi siri' in command:
                command=command.replace('hi siri','')
                
    except:
        command='what is your name'
        run()
        
        
    return command
def run():
    command=take()
    print(command)
    if 'who is your boss' in command:
        talk('deepanshu kaushik is my boss')
    elif 'what is your name' in command:
        talk('siri a voice assistant')
    elif 'play' in command:
        if 'hey' in command:
            command=command.replace('hey siri','')
        song=command.replace('play','')
        print(song)
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        if 'hey siri' in command:
            command=command.replace('hey siri','')
        song=command.replace('search','')
        print(song)
        talk("searching "+song)
        pywhatkit.search(song)
    elif 'time' in command:
        val=str(list(time.localtime())[3])+" "+str(list(time.localtime())[4])
        print(str(list(time.localtime())[3])+":"+str(list(time.localtime())[4]))
        talk('time is '+val)
    else:
        exit()

#pywhatkit.sendwhatmsg("+919700097029","automati send message",22,41)
       
while True:
    run()
    time.sleep(6)
