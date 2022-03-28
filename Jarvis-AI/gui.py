import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from tkinter import *
import threading




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



def function():
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


class Example(Frame):
    def __init__(root, parent):
        Frame.__init__(root, parent)
        f1 = GradientFrame(root, borderwidth=1, relief="sunken")
        f1.pack(side="top", fill="both", expand=True)

class GradientFrame(Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(root, parent, color1="#202060", color2="#0d0d26", **kwargs):
        Canvas.__init__(root, parent, **kwargs)
        root._color1 = color1
        root._color2 = color2
        root.bind("<Configure>", root._draw_gradient)

    def _draw_gradient(root, event=None):
        '''Draw the gradient'''
        root.delete("gradient")
        width = root.winfo_width()
        height = root.winfo_height()
        limit = width
        (r1,g1,b1) = root.winfo_rgb(root._color1)
        (r2,g2,b2) = root.winfo_rgb(root._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            root.create_line(i,0,i,height, tags=("gradient",), fill=color)
        root.lower("gradient")

def start():
    t1 = threading.Thread(target=function, args=(10,))
    #t2 = threading.Thread(target=print_cube, args=(10,))



def createwidgets(root):

        takecommand = Button (root,text = 'Command', bg = 'green2',font = ('arial',13,'italic'),width = 10 , relief=GROOVE, bd = 5,activebackground = 'purple4')
        takecommand.place(x=325,y=400)

        Start = Button (root,text = 'Start', bg = 'green2',font = ('arial',13,'italic'),width = 10 , relief=GROOVE, bd = 5,activebackground = 'purple4',command=start)
        Start.place(x=400,y=500)

        stop = Button (root,text = 'Stop', bg = 'green2',font = ('arial',13,'italic'),width = 10 , relief=GROOVE, bd = 5,activebackground = 'purple4')
        stop.place(x=250,y=500)







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')    #to load the voice in program.

#print(voices[0].id)       1 for girl and 0 for boy.
engine.setProperty('voice',voices[1].id)   #to provide a properties of voice


root = Tk()
root.geometry('800x600')
root.title('FRIDAY..')
root.resizable(False,False)
root.configure(bg='lightskyblue')
Example(root).pack(fill="both", expand=True)
createwidgets(root)
count=0
text=""


##################################### slider
ss = "S   m   i   l   e"

sliderlabel=Label(root,text=ss, font = ('castellar',22,'bold'))
sliderlabel.place(x=120,y=10)
def introlabeltrick():
    global count,text
    if count>=len(ss):
        count=-1
        text=""
        sliderlabel.configure(text=text)
    else:
        text=text+ss[count]
        sliderlabel.configure(text=text)
    count+=1
    sliderlabel.after(200,introlabeltrick)

########################################



introlabeltrick()
root.mainloop()
