
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib  



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Curly . Please tell me how may I help you ? ")
    
def takeCommand():
    #It takes microphone input from the user and returns string output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("User Said:{query}\n")
    
    except Exception as e:
        #print(e)
        
        print("Say that again please...")
        return "None" 
    return query

'''def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendemail('youremail@gmail.com',to,content)
    server.close()    
    '''
    
    
if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            #This is for opening youtube
            webbrowser.open("youtube.com")
        
        elif 'open w3schools' in query:
            #This is for opening w3schools 
            webbrowser.open("w3schools.com")
        
        elif 'open google' in query:
            #This is for opening google
            webbrowser.open("google.com")
            
        elif 'open amazon' in query:
            #This is for opening amazon
            webbrowser.open("amazon.in")
            
        elif 'open imdb' in query:
            
            #This is for opening imdb
            webbrowser.open("imdb.com")
            
        elif 'play music' in query:
            #This part of the code is still work in progress as we  need to debug it so that the songs can be played from the system.
            music_dir='C:\\Users\\dmin\\Downloads\\The Twilight Saga Breaking Dawn Pt. 2 OST 2012 320kbps navj'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            CodePath = "C:\\Users\\admin\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CodePath)
        
        '''elif 'email to Aryan' in query:
            try:
                speak("What should I say ?")
                content=takeCommand()
                to = "200020223030.aryan@gdgu.org" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Aryan. I was unable to send this email.")
                '''
            
            
    