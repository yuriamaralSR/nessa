import unittest
from nessa import *
from processar_audio import *

CHAMANDO_NOME_CORRETO = "audios/chamando_nome_correto.wav"
CHAMANDO_NOME_INCORRETO = "audios/chamando_nome_incorreto.wav"

BUSCAR_SOBRE = "audios/buscar_sobre_python.wav"
BUSCAR_EXERCICIO = "audios/buscar_exercicio.wav"
BUSCAR_EXERCICIOS = "audios/buscar_exercicio.wav"
BUSCAR_TUTORIAL = "audios/buscar_tutorial.wav"
BUSCAR_TUTORIAIS = "audios/buscar_tutoriais.wav"
BUSCAR_VIDEO = "audios/buscar_video.wav"
BUSCAR_VIDEOS = "audios/buscar_videos.wav"
ABRIR_DOCUMENTACAO_CPP = "audios/abrir_documentacao_cpp.wav"
ABRIR_DOCUMENTACAO_JAVA = "audios/abrir_documentacao_java.wav"
ABRIR_DOCUMENTACAO_PYTHON = "audios/abrir_documentacao_python.wav"
ABRIR_VSCODE = "audios/abrir_vscode.wav"

class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        iniciou, _, _, nome_do_assistente, palavras_de_parada, comandos = iniciar()

    def reconhecer_nome_teste(self):
        comando = processar_audio(CHAMANDO_NOME_CORRETO)
        comando = comando.split()

        nome_do_assistente = ""
        print(comando)
        if len(comando):
            nome_do_assistente = comando[0]
            print(f"nome do assistente: {nome_do_assistente}")
        self.assertIn("nessa", nome_do_assistente)
    
    def nao_reconhecer_outro_nome_teste(self):
        comando = processar_audio(CHAMANDO_NOME_INCORRETO)
        comando = comando.split()

        nome_do_assistente = ""
        print(comando)
        if len(comando):
            nome_do_assistente = comando[0]
            print(f"nome do assistente: {nome_do_assistente}")
        self.assertNotIn("nessa", nome_do_assistente)

class TesteModuloBuscar(unittest.TestCase):

    def setUp(self):
        iniciou, _, _, nome_do_assistente, palavras_de_parada, comandos = iniciar()

    def buscar_sobre_teste(self):
        comando = processar_audio(BUSCAR_SOBRE)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        print(tokens)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def buscar_exercico_teste(self):
        comando = processar_audio(BUSCAR_EXERCICIO)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        print(tokens)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def buscar_exercicos_teste(self):
        comando = processar_audio(BUSCAR_EXERCICIOS)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def buscar_tutorial_teste(self):
        comando = processar_audio(BUSCAR_TUTORIAL)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def buscar_tutoriais_teste(self):
        comando = processar_audio(BUSCAR_TUTORIAIS)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def buscar_video_teste(self):
        comando = processar_audio(BUSCAR_VIDEO)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def buscar_videos_teste(self):
        comando = processar_audio(BUSCAR_VIDEOS)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

class TesteModuloAbrir(unittest.TestCase):
    
    def setUp(self):
        iniciar()

    def abrir_documentacao_cpp_teste(self):
        comando = processar_audio(ABRIR_DOCUMENTACAO_CPP)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def abrir_documentacao_java_teste(self):
        comando = processar_audio(ABRIR_DOCUMENTACAO_JAVA)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def abrir_documentacao_python_teste(self):
        comando = processar_audio(ABRIR_DOCUMENTACAO_PYTHON)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

    def abrir_vscode_teste(self):
        comando = processar_audio(ABRIR_VSCODE)
        print(f"comando reconhecido: {comando}")

        tokens = tokenizar(comando)
        tokens_filtrados = filtrar_tokens(tokens, palavras_de_parada)
        validado, modulo, objeto, parametro = validar_comando(tokens_filtrados, nome_do_assistente, comandos)
        if validado:
            executou = executar_comando(modulo, objeto, parametro)

        self.assertTrue(executou)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteModuloBuscar))
    testes.addTest(carregador.loadTestsFromTestCase(TesteModuloAbrir))

    executor = unittest.TextTestRunner()
    executor.run(testes)