import webbrowser
import subprocess

def atuar_modulo_abrir(modulo, objeto, parametro):
    executou = False
    
    if modulo in ["abrir"]:
        print("cheguei no modulo")
        if objeto in ["documentacao"]:
            print("cheguei no objeto")
            if parametro == ['java']:
                print('cheguei')
                webbrowser.get('windows-default').open_new("https://docs.oracle.com/en/java/")
                executou = True
            elif parametro == ['python']:
                print('cheguei')
                webbrowser.get('windows-default').open_new("https://docs.python.org/3/")
                executou = True
            elif parametro == ['c++']:
                print('cheguei')
                webbrowser.get('windows-default').open_new("https://en.cppreference.com/w/")
                executou = True
        elif objeto in ["vscode"]:
            print('cheguei')
            subprocess.Popen(['cmd', '/c', 'start', 'code', '-n'])
            executou = True

    return executou