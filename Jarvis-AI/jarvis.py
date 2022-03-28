import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#import smtblib

'''def sendEmail(to,content):
    server = smtlib.SMTP("smtp.gmail.com",587)
    server.startls()
    server.login("skgwhatsapp1812@gmail.com","")
    server.sendmail("skgwhatsapp1812@gmail.com",to,content)
    server.close()'''



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')    #to load the voice in program.

#print(voices[0].id)       1 for girl and 0 for boy.
engine.setProperty('voice',voices[1].id)   #to provide a properties of voice


def WishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    speak("Hi I am smile, how can I help you")
                



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass



    


def takeCommand():   # it takes microphone's input and return string output.
    r = sr.Recognizer()  # function help us to recognize the audio.
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1 # for 1 sec pause after listning.
        audio = r.listen(source)   # coming from speak recognition module and listning voice form mic or microphone

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language="en-us")        
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say it again please....")
        return "None"

    
    return query   
    
def start():
    if __name__ == "__main__":
        WishMe()
        if 1:
            query = takeCommand().lower()                     # take command returns string which you have spoken.
            # logic for executing task based on query
            if 'wikipedia' in query:
                speak("searching Wikipedia....")
                querty = query.replace("wekipedia","")
                results = wikipedia.summary(query,sentences=4)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:         # if query is similar to string than open
                speak("ok sir, opening youtube")
                webbrowser.open("youtube.com")     # to open in webbrowser

            elif 'open google' in query:
                speak("ok sir, opening google")
                webbrowser.open("google.com")

            elif " open gfg" in query:
                speak(" ok sir, opening geeks for geeks")
                webbrowser.open("wwww.geeksforgeeks.com")

            elif "play music" in query:
                music_dir = "E:\\realme 3\\SONGS\\Videos"
                songs = os.listdir(music_dir)   # list down all the files from this directory (listdir function)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"sir, The time is {strTime}")


            elif "vs code" in query:
                codepath = "C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("Opening Visual Studio Code sir")
                os.startfile(codepath)   # function is used to access the path and open the code.

        

            elif "email to harry" in query:
                try:
                    speak("What should I Say?")
                    content = takeCommand()
                    to = "31anuragupta@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send Successfully")
                except Exception as e:
                    print(e)
                    speak("sorry bro")
            
            
start()


            
