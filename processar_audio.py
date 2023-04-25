import speech_recognition as sr

def processar_audio(audio):
    microfone = sr.Recognizer()

    with sr.AudioFile(audio) as fonte_audio:
        fala = microfone.listen(fonte_audio)
        try:
            comando = microfone.recognize_google(fala, language='pt-BR')
        except sr.UnknownValueError:
            pass

    return comando.lower()