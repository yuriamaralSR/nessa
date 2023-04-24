import json
from time import sleep
import speech_recognition as sr
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import pyttsx3
import keyboard
from buscar import *
from abrir import *

ARQUIVO_CONFIG = "D:/ws_python/nessa/config.json"
NOME_DO_ASSISTENTE = 'nessa'
ATUADORES = [
    {
        "atuar": atuar_modulo_buscar,
    },
    {
        "atuar": atuar_modulo_abrir,
    },
    
]


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
        try:
            reconhecedor.adjust_for_ambient_noise(fonte_de_audio)
            falar("Estou ouvindo...")
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

def extrair_parametro(tokens):
    parametro = ""
    parametro = tokens[3:]
    

    return parametro


def validar_comando(tokens, nome_do_assistente, comandos):
    validado, modulo, objeto  = False, None, None

    if len(tokens) >= 3:
        if nome_do_assistente == tokens[0]:
            modulo = tokens[1]
            if len(tokens[2]) == 2:
                objeto = tokens[2:]
            objeto = unidecode(tokens[2])
            
        for chaves in comandos:
            if modulo == chaves["modulo"]:
                if objeto in chaves["objeto"]:
                    parametro = chaves["parametros"]
                    if parametro == [""]:
                        parametro = extrair_parametro(tokens)

                    validado = True
    else:
        falar('O comando não foi validado!')

    return validado, modulo, objeto, parametro

def executar_comando(modulo, objeto, parametro):
    if parametro == "":
        falar(f"Executando o comando: {modulo} {objeto} ")
    falar(f"Executando o comando: {modulo} {objeto} {parametro}")
    for atuador in ATUADORES:
        atuou = atuador["atuar"](modulo, objeto, parametro)
        if atuou:
            break

if __name__ == '__main__':
    iniciou, reconhecedor, nessa_diz, nome_do_assistente, palavras_de_parada, comandos = iniciar()
    SAUDACAO = "Olá sou a Nêssa tudo bem? Estou aqui para lhe ajudar em seus estudos de programação."
    INSTRUCAO = "Pressione 'ctrl+alt+shift+n' para começar."
    if iniciou:
        falar(SAUDACAO)
        falar(INSTRUCAO)
        while True:
            sleep(0.05)
            if keyboard.is_pressed('ctrl+alt+shift+n'):
                ouviu, fala_usuario = ouvir(reconhecedor)
                if ouviu:
                    transcreveu, transcricao = trancrever(fala_usuario, reconhecedor)
                    if transcreveu:
                        tokens = tokenizar(transcricao)
                        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
                        validado, modulo, objeto, parametro  = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
                        if validado:
                            executar_comando(modulo, objeto, parametro)
            sleep(0.05)