import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <= 12:
        speak("Good Morning Sir!")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoonc Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am Dizzi, please tell me how may I help you")




def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Listning.....")
       r.pause_threshold = 1
       audio = r.listen(source)
       

   try:
        print("Recognizing..")
        query1 = r.recognize_google(audio, language='en-in')
        print('User said ', query1)

   except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
   return query1

def sendEmail(to, content ):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("YourMail@mail.com","Password")
    server.sendmail("YourMail@mail.com", to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    
        # logic for executing task
        
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        

        elif 'play music' in query:
            music_dir = 'music'
            songs = os.listdir(music_dir)
            print("\n",songs)
            os.startfile(os.path.join(music_dir, songs[7]))
        elif 'the time' in query: 
            strtTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"sir, The Time is {strtTime}")    

        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"    
            os.startfile(codepath)    

        elif 'open spotify' in query:
            codepath = "C:\\Users\\ACER\\AppData\\Roaming\\Spotify\\Spotify.exe" 
            os.startfile(codepath)        
        elif 'open atom' in query:
            codepath = "C:\\Users\\ACER\\AppData\\Local\\atom\\atom.exe"    
            os.startfile(codepath)   
        elif 'open chrome' in query:
            codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"     
            os.startfile(codepath)
        elif 'open firefox' in query:
            codepath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
            os.startfile(codepath)        
        elif 'open unity' in query:
            codepath = "C:\\Program Files\\Unity\\Editor\\Unity.exe"
            os.startfile(codepath)            
        elif 'open sublime' in query:
            codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codepath)            
        elif 'open android studios'  in query:
            codepath = "C:\\Program Files\\Android\Android Studio\\bin\\studio64.exe"
            os.startfile(codepath)

        elif 'wish happy birthday' in query:
            speak("Happy Birthday to You,  Happy Birthday to You,  Happy Birthday Dear (FRIEND), Happy Birthday to You");
            speak("From good friends and true, From old friends and new, May good luck go with you, And happiness too")
        elif 'email to saurabh' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "timesofsrb@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I'm not able to sent email")    