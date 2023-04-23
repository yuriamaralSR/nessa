import json
from time import sleep
import speech_recognition as sr
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import pyttsx3
import keyboard

ARQUIVO_CONFIG = "D:/ws_python/nessa/config.json"
NOME_DO_ASSISTENTE = 'nessa'


def iniciar():
    iniciou = False
    reconhecedor = sr.Recognizer()
    nessa_diz = pyttsx3.init()

    try:
        palavras_de_parada = set(stopwords.words('portuguese'))
        with open(ARQUIVO_CONFIG, "r") as arquivo_de_config:
            comandos_configuracao = json.load(arquivo_de_config)

            nome_do_assistente = NOME_DO_ASSISTENTE
            comandos = comandos_configuracao['comandos']
            
            arquivo_de_config.close()

        iniciou = True
    except:
        falar("Desculpe a inicialização falhou!")
    
    return iniciou, reconhecedor, nessa_diz, nome_do_assistente, palavras_de_parada, comandos

def falar(texto):
    if nessa_diz._inLoop:
        nessa_diz.endLoop()
    nessa_diz.say(texto)
    print("Nessa >> " + texto)
    nessa_diz.runAndWait()

def ouvir(reconhecedor):
    ouviu = False

    with sr.Microphone() as fonte_de_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_de_audio)
        
        falar("Estou ouvindo...")
        try:
            fala_usuario = reconhecedor.listen(fonte_de_audio, timeout = 5)
            ouviu = True
        except sr.UnknownValueError:
            falar("Desculpe, não entendi")
        except sr.RequestError:
            falar("Desculpe, o serviço está offline")

    return ouviu, fala_usuario

def trancrever(fala_usuario, reconhecedor):
    transcreveu = False

    try:
        transcricao = reconhecedor.recognize_google(fala_usuario, language="pt-BR")
        transcreveu = True

    except sr.UnknownValueError:
        falar("Desculpe, não consegui entender")
    except sr.RequestError:
        falar("Desculpe, o serviço está offline")

    print("Usuario >> ", transcricao.lower())

    return transcreveu, transcricao.lower()

def tokenizar(transcricao):
    return word_tokenize(transcricao)

def filtrar_tokens(tokens, palavras_de_parada):
    tokens_filtrados = []
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados


def validar_comando(tokens, nome_do_assistente, comandos):
    validado, modulo, objeto  = False, None, None

    if len(tokens) >= 3:
        if nome_do_assistente == tokens[0]:
            modulo = tokens[1]
            objeto = unidecode(tokens[2])
            parametro = tokens[3:]
            
        for modulos in comandos:
            if modulo == modulos["modulo"]:
                if objeto in modulos["objeto"]:
                    print(objeto)

    return validado

if __name__ == '__main__':
    iniciou, reconhecedor, nessa_diz, nome_do_assistente, palavras_de_parada, comandos = iniciar()
    boas_vindas = "Olá sou a Nêssa tudo bem? Estou aqui para lhe ajudar em seus estudos de programação."

    if iniciou:
        tokens = tokenizar('nessa buscar exercícios de programação')
        tokens_filtrados = filtragem_tokens(tokens, palavras_de_parada)
        print(tokens_filtrados)
        valido = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        #falar(boas_vindas)
        # while True:
        #     sleep(0.05)
        #     if keyboard.is_pressed('ctrl+alt+shift+n'):
                
        #         ouviu, fala_usuario = ouvir(reconhecedor)
                
        #         if ouviu:
        #             transcreveu, transcricao = trancrever(fala_usuario, reconhecedor)
        #             if transcreveu:
        #                 tokens = tokenizar(transcricao)
        #                 valido = validar_comando(tokens, nome_do_assistente, comandos)
        #     sleep(0.05)