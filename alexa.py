import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit
import wikipedia
import webbrowser
from time import sleep
import cv2
import winsound


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty("voices",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..................")
        r.pause_threshold =1
        audio= r.listen(source)

    try:
        print("Recognizing..................")
        text=r.recognize_google(audio,language="en-in")
        print(f" you said:{text}")
    
    except Exception as e:
        speak("Sorry could not understand what you said")
        return "None"
    return  text 


def wish():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak("Good morning sir!")
    elif h>=12 and h<16:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")

    speak("how can i help you")

if __name__ == "__main__":
    speak("welcome,to the chandan's  virtual assistant.")


    while True:
        text=takecommand().lower()
        if 'wake up' in text:
            wish()

        elif "hello alexa" in text:
            speak("hello ,sir ,how are you")

        elif "fine" in text:
            speak("that's great,sir")

        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak("the current time is",+ strTime)

        elif "date" in text:
            date = datetime.datetime.today()
            speak("Today is " + date)

        elif "open notepad" in text:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open cmd" in text:
            npath="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(npath)
        

        elif "sleep now" in text:
            speak("ok sir,")
            sleep(20)

        elif "thank you alexa" in text:
            speak("welcome,sir ")

        elif "who are you" in text:
            speak("I am your  Alexa.")
        
        elif "who built you" in text:
            speak("chandan")
        
        elif "are you single alexa" in text:
            speak("No, i am relationship with  my creator, chandu")
        
        elif "when will I  get married?" in text:
            speak(" someday soon")
        
        elif "how is the josh alexa" in text:
            speak("High,sir")

        elif "google map" in text:
                speak("ok,sir where are you looking for?")
                speak("from where to go ")
                from_where=takecommand().lower()
                sleep(2)
                speak("to where you want to go?")
                to_where=takecommand().lower()
                sleep(2)
                result= f"https://www.google.com/maps/dir/{from_where}/{to_where}"
                webbrowser.get().open(result)
    
        elif "which programming language is best in the  world" in text:
            speak(" PYTHON ")

        elif "youtube" in text:
            search=text.replace("youtube","")
            speak("play" +search)
            pywhatkit.playonyt(search)

        elif "search" in text:
            s=text.replace("search","")
            speak('search' + s)
            pywhatkit.search(s)

        elif "who is " in text:
            person=text.replace("who is ","")
            info=wikipedia.summary(person, sentences=2)
            speak(info)

        elif "temperature" in text:
            tem=text.replace("temperature","")
            result=pywhatkit.search(tem)


        elif "current price of gold" in text:
            search=text.replace("what is the current price of","")
            speak("current price of gold  is searching")
            url="https://www.moneycontrol.com/news/gold-rates-today/"
            webbrowser.get().open_new_tab(url)
        
        elif "current price of sliver " in text:
            search=text.replace("what is the current price of","")
            speak("current price of sliver is searching")
            url="https://www.goodreturns.in/silver-rates/"
            webbrowser.get().open_new_tab(url)


        elif "click photo" in text:
            speak("Smile,please..")
            cap=cv2.VideoCapture(0)

            result,image=cap.read()

            if result:
                cv2.imshow('image', image)
                cv2.imwrite('image.jpg', image)
                cv2.waitKey(10)
                speak("Done")
                cv2.destroyAllWindows()
            else:
                speak("sorry no face detected")

        elif "look at" in text :
            speak("ok sir, i am careful,if any movement in camera, i will notify you ,by alert alarm")
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                for c in contours:
                    if cv2.contourArea(c) < 5000:
                        continue
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('Granny Cam', frame1)
            
        

        elif "check cricket score" in text:
            cricket=text.replace( "check cricket score","") 
            url="https://www.cricbuzz.com/cricket-match/live-scores"
            webbrowser.get().open_new_tab(url)

        elif "open flipkart" in text:
            flip=text.replace("open flipkart", "")
            url="https://www.flipkart.com/"
            webbrowser.get().open_new(url)

        elif "open amazon" in text:
            amz=text.replace( "open amazon","")
            url="https://www.amazon.in/"
            webbrowser.get().open_new(url)

        elif "open myntra" in text:
            my=text.replace("open myntra","")
            url="https://www.myntra.com/"
            webbrowser.get().open_new(url)

        
        elif "stop alexa" in text:
            exit()
        
        else :
            pass
            


        
        
    



