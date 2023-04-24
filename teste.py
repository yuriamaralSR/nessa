import speech_recognition as sr

# Cria um objeto de reconhecimento de fala
r = sr.Recognizer()

# Abre o arquivo de áudio
with sr.AudioFile(r'D:\ws_python\nessa\audios\buscar_exercicio.wav') as source:
    # Lê o áudio do arquivo
    audio = r.record(source)
    
# Usa o Google Speech Recognition para transcrever o áudio em texto
try:
    text = r.recognize_google(audio, language="pt-BR")
    print("Transcrição: " + text)
except sr.UnknownValueError:
    print("Não foi possível transcrever o áudio")
except sr.RequestError as e:
    print("Não foi possível conectar-se ao serviço de reconhecimento de fala; {0}".format(e))
