import json
from time import sleep
import webbrowser
import speech_recognition as sr
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import pyttsx3
import keyboard
import wikipedia

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

def extrair_parametro(tokens):
    parametro = tokens[3:]

    return parametro


def validar_comando(tokens, nome_do_assistente, comandos):
    validado, modulo, objeto  = False, None, None

    if len(tokens) >= 3:
        if nome_do_assistente == tokens[0]:
            modulo = tokens[1]
            objeto = unidecode(tokens[2])
            
        for chaves in comandos:
            if modulo == chaves["modulo"]:
                if objeto in chaves["objeto"]:
                    parametro = chaves["parametros"]
                    parametro = extrair_parametro(tokens)
                    validado = True
    else:
        falar('O comando não foi validado!')

    return validado, modulo, objeto, parametro

def buscar_conceito(parametro):
    wikipedia.set_lang('pt')
    try:
        pagina = wikipedia.page(parametro)
        conceito = wikipedia.summary(parametro)
        url = pagina.url

    except wikipedia.exceptions.DisambiguationError as e:
        falar(f"Não foi possível encontrar uma definição precisa para '{parametro}'.")
        falar("Por favor, tente especificar sua pesquisa com mais detalhes ou escolha um dos seguintes termos:")
        for i, termo in enumerate(e.options):
            print(f"{i + 1}. {termo}")
    return conceito, url

def buscar_exercicio(parametros):
    url = "https://google.com"
    webbrowser.get('windows-default').open_new(f'{url}/search?q=exercício+{parametros}')

def buscar_video(parametros):
    url = "https://youtube.com"
    webbrowser.get('windows-default').open_new(f'{url}/search?q={parametros}')

def abrir_documentacao(parametro):
    if parametro == 'java':
        url = "https://docs.python.org/3/"
        webbrowser.get(url)
    elif parametro == 'python':
        ...
    elif parametro == 'c++':
        ...
    

def verificar_comando(objeto, parametro):
    veja_mais = ''
    if objeto in "sobre":
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            executar, url = buscar_conceito(parametros)
            veja_mais = (f'Veja mais em: {url}')
        else:
            executar, url = buscar_conceito(parametros)
            veja_mais = (f'Veja mais em: {url}')
    
    elif objeto in {'tutoriais', 'tutorial', 'videos', 'video'}:
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            executar = buscar_video(parametros)
    elif objeto in {"exercicios", "exercicio"}:
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            executar = buscar_exercicio(parametros)
    elif objeto in 'documentacao':
        if len(parametro) >= 1:
            parametros = " ".join(parametro)
            executar = abrir_documentacao(parametros)
    else:
        ...
    return executar, veja_mais

def executar_comando(modulo, objeto, parametro):
    if parametro != []:
        falar(f"Executando o comando... {modulo} {objeto} {parametro}")
        executar, veja_mais = verificar_comando(objeto, parametro)
        falar(executar)
        falar(veja_mais)

    else:
        falar(f"Executando o comando... {modulo} {objeto}")

if __name__ == '__main__':
    iniciou, reconhecedor, nessa_diz, nome_do_assistente, palavras_de_parada, comandos = iniciar()
    boas_vindas = "Olá sou a Nêssa tudo bem? Estou aqui para lhe ajudar em seus estudos de programação."

    if iniciou:
        tokens = tokenizar('nessa abrir documentacao python')
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro  = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executar_comando(modulo, objeto, parametro)
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