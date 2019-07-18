import speech_recognition as sr

r = sr.Recognizer()  # Works as a recognizer to recognize our audio

with sr.Microphone(device_index = None) as source:  # Initializing our source to sr.Microphone()
    print('Speak Anything : ')
    
    r.adjust_for_ambient_noise(source, duration = 5) # Using the ambient noise suppression/adjustment

    audio = r.listen(source)  # Telling it to listen to source and storing it in audio

    try:
        text = r.recognize_google(audio)  # Converts audio into text
        print('You said : {}'.format(text))  # Prints what you said
    except:
        print('Sorry could not recognize your voice')