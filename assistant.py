import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr 
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine=pyttsx3.init('sapi5')

client=wolframalpha.Client('XLET94-29L9AHU8AU')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)

def speak(audio):
    print('computer:'+audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH=int(datetime.datetime.now().hour)
    if currentH>=0 and currentH<12:
        speak('good morning')

    if currentH>=12 and currentH<18:
        speak('good afternoon')

    if currentH>=18 and currentH!=0:
        speak('good evening')

greetMe()

speak('Hello Sir,I am your digital assistant emi!')
speak('how may I help you?')


def myCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="en-in")
        print('user:'+query+'\n')

    except sr.UnknownValueError:
        speak('Sorry Sir!I didn\'t get that try typing the command!')
        query=str(input('command:'))

    return query


if __name__ == '__main__':

    while True:

        query=myCommand()
        query=query.lower()

        if 'open youtube' in query:
            speak('okay sir')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay sir')
            webbrowser.open('www.google.com')

        elif 'open stackoverflow' in query:
            speak('okay sir')
            webbrowser.open('www.stackoverflow.com')

        elif 'open instagram' in query:
            speak('okay sir')
            webbrowser.open('www.instagram.com')

        elif 'open facebook' in query:
            speak('okay sir')
            webbrowser.open('www.facebook.com')

        elif 'open twitter' in query:
            speak('okay sir')
            webbrowser.open('www.twitter.com')

        elif 'open whatsapp' in query:
            speak('okay sir')
            webbrowser.open('web.whatsapp.com')

        elif 'who am I' in query:
            speak('you are the one who created me')

        elif 'open gmail' in query:
            speak('okay sir')
            webbrowser.open('https://accounts.google.com//')

        elif 'open ms team' in query:
            speak('okay sir')
            webbrowser.open('https://teams.microsoft.com//')       #optional

        elif 'open python' in query:
            speak('okay sir')
            pythonPath='C:\\Users\\suhartho mandal\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib\\idle.pyw'
            os.startfile(pythonPath)                      #replace my path with your idle path

        elif 'open vs code' in query:
            speak('okay sir')
            vscodePath="your vs code path"
            os.startfile(vscodePath)

        elif 'open narrator' in query:
            speak('okay sir')
            narratorPath='your narrator path'
            os.startfile(narratorPath)

        elif 'open desktop' in query:
            speak('okay sir')
            desktopPath="your desktop path"
            os.startfile(desktopPath)

        elif 'open new folder2' in query:
            speak('okay sir')
            newfolder2Path='\\SANDY\\New folder (2)'
            os.startfile(newfolder2Path)           #optional

        elif 'open new folder3' in query:
            speak('okay sir')
            newfolder3Path='\\SANDY\\New folder (3)'
            os.startfile(newfolder3Path)                #optional

        elif 'open blueStacks' in query:
            speak('okay sir, this will take some time as per your PC performance')
            blueStacksPath='your bluestacks path'
            os.startfile(blueStacksPath)

        elif 'open new folder5' in query:
            speak('okay sir')
            newfolder5Path='\\SANDY\\New folder (5)'
            os.startfile(newfolder5Path)                #optional

        elif 'open taylor swift' in query:
            speak('okay sir')
            taylorswiftPath='\\SANDY\\taylor swift'
            os.startfile(taylorswiftPath)                       #optional

        elif 'open got' in query:
            speak('okay sir')
            gotPath='\\SANDY\\got'
            os.startfile(gotPath)                      #optional

        elif 'open cmd' in query:
            speak('okay sir')
            cmdPath='YOUR cmd path'
            os.startfile(cmdPath)

        elif "what\'s up emi"  in query or 'how are you' in query:
                stmsgs=['just doing my things!','I am fine sir,How are you','I am nice sir and full of energy','I am good,waiting for your next command','I am fine,always ready to serve']
                speak(random.choice(stmsgs))
        
        elif 'wait for my command' in query:
            speak('okay sir')

        elif 'express yourself' in query:
            speak('I am your digital AI assistant emi')

        elif 'which source is used to create you' in query:
            speak('I have been created by python programing')

        elif 'what can you do for me emi' in query:
            speak('I can do anything,i can search an data for you,can inform you many important things as per your cammand,can tell you the latest update of news headlines,you just have to command me')
            
        elif 'what you can not do for me' in query:
            speak('well...I am not a chatbot so I can not talk to you as a chatbot')

        elif 'send email' in query:
            speak('who is the recipient?')
            recipient=myCommand()

            if 'me' in recipient:
                try:
                    speak('what should I say?')
                    content=myCommand()

                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login("your username",'yourpassword')
                    server.sendmail("username","recipient_username",content)
                    server.close()
                    speak('email sent,sir!')

                except:
                    speak('sorry sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay sir')
            speak('bye sir, have a good day.')
            sys.exit
 
        elif 'shut down' in query:
             speak('okay sir')
             speak('hope I was useful for you')
             sys.exit()

        elif 'hello emi' in query:
            speak('hello sir')
            speak('how can I help you')

        elif 'bye' in query:
            speak('bye Sir,have a nice day.')
            sys.exit()

        elif 'play music' in query:
            speak('what should I play for you sir?')
            musicfolder ='\\SANDY\taylor swift'
            music=['music name','music name','music name','music name','music name']
            random_music=musicfolder+random.choice(music)+'.mp3'
            os.system(random_music)

            speak('okay,here is your music! Enjoy!')


        else:
            query=query
            speak('Searching...')
            try:
                try:
                    res=client.query(query)
                    results=next(res.results).text
                    speak('WOLFRAM-ALPHA says-')
                    speak('got it sir.')
                    speak(results)

                except:
                    results=wikipedia.summary(query,sentences=2)
                    speak('got it sir.')
                    speak('WIKIPEDIA says-')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('next command! Sir!')  
                 
    
    

    