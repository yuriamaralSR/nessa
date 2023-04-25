import webbrowser
import subprocess

def atuar_modulo_abrir(modulo, objeto, parametro):
    executou = False

    if modulo in ["abrir"]:
        if objeto in ["documentacao"]:
            if parametro == ['java']:
                webbrowser.get('windows-default').open_new("https://docs.oracle.com/en/java/")
                executou = True
            elif parametro == ['python']:
                webbrowser.get('windows-default').open_new("https://docs.python.org/3/")
                executou = True
            elif parametro == ['c++', 'c']:
                webbrowser.get('windows-default').open_new("https://en.cppreference.com/w/")
                executou = True
            else:
                executou = False
        elif objeto in ["vscode", "vs code", "vs"]:
            subprocess.Popen(['cmd', '/c', 'start', 'code', '-n'])
            executou = True

    return executou