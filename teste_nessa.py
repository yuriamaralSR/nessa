import unittest
from nessa import *

CHAMANDO_NOME_CORRETO = r"D:\ws_python\nessa\audios\chamando_nome_correto.wav"
CHAMANDO_NOME_INCORRETO = r"D:\ws_python\nessa\audios\chamando_nome_incorreto.wav"

BUSCAR_SOBRE = r"D:\ws_python\nessa\audios\buscar_sobre_python.wav"
BUSCAR_EXERCICIO = r"D:\ws_python\nessa\audios\buscar_exercicio.wav"
BUSCAR_EXERCICIOS = r"D:\ws_python\nessa\audios\buscar_exercicios.wav"
BUSCAR_TUTORIAL = r"D:\ws_python\nessa\audios\buscar_tutorial.wav"
BUSCAR_TUTORIAIS = r"D:\ws_python\nessa\audios\buscar_tutoriais.wav"
BUSCAR_VIDEO = r"D:\ws_python\nessa\audios\buscar_video.wav"
BUSCAR_VIDEOS = r"D:\ws_python\nessa\audios\buscar_videos.wav"
ABRIR_DOCUMENTACAO_CPP = r"D:\ws_python\nessa\audios\abrir_documentacao_cpp.wav"
ABRIR_DOCUMENTACAO_JAVA = r"D:\ws_python\nessa\audios\abrir_documentacao_java.wav"
ABRIR_DOCUMENTACAO_PYTHON = r"D:\ws_python\nessa\audios\abrir_documentacao_python.wav"

class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        iniciar()

    def reconhecer_nome_teste(self):
        transcreveu, transcricao = trancrever(BUSCAR_EXERCICIO, reconhecedor)
        if transcreveu:
            tokens = tokenizar(transcricao)
            nome_do_assistente = ""
            if len(tokens):
                nome_do_assistente = tokens[0]

        self.assertIn("nessa", nome_do_assistente)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))

    executor = unittest.TextTestRunner()
    executor.run(testes)