import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    engine.setProperty('rate', 174)     # setting up new voice rate
    eel.DisplayMessage(text)
    # print(voices)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        
        # speak(query)
        
    except Exception as e:
        return ""
    
    return query.lower()

# text = takecommand()

# speak(text)

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in  query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "send message" in query or "whatsapp call" in query or "video call" in query:
            from engine.features import findContact, whatsapp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no !=0):

                if "send message" in query:
                    flag = 'message'
                    speak("What message to send")
                    query = takecommand()

                elif "whatsapp call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                
                whatsapp(contact_no, query, flag, name)
        elif "phone call" in query:
            from engine.features import findContact, phoneCall
            contact_no, name = findContact(query)
            phoneCall(contact_no, name)
        elif "type something" in query:
            speak("What do you want to type?")     
            query = takecommand()   
            from engine.features import typeText
            typeText(query)  
        elif "show contacts" in query:
            from engine.features import showContacts
            showContacts()
        elif "unlock my phone" in query:  
             from engine.features import unlockPhone
             unlockPhone()
        elif "lock my phone" in query:
            from engine.features import lockPhone
            lockPhone()
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")

    eel.ShowHood()