import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Powiedz coś ciekawego: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language = 'pl-PL')
        print('Właśnie powiedziałeś: {}'.format(text))
    except:
        print('Nie można złapać Twojego głosu :/')
