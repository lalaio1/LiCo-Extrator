import subprocess
import sys

Cores = {
    "vermelha": "\033[1;31m",
    "verde": "\033[1;32m",
    "amarela": "\033[1;33m",
    "azul": "\033[1;34m",
    "roxa": "\033[1;35m",
    "ciano": "\033[1;36m",
    "branca": "\033[1;37m",
    "reset": "\033[0m",
}

def verificar_biblioteca(biblioteca):
    try:
        __import__(biblioteca)
        return True
    except ImportError:
        return False

def instalar_biblioteca(biblioteca):
    print(f"{Cores['reset']}[{Cores['vermelha']}-{Cores['reset']}]{Cores['vermelha']} Instalando biblioteca {biblioteca}...{Cores['reset']}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
        print(f"{Cores['reset']}[{Cores['azul']}+{Cores['reset']}]{Cores['verde']} {biblioteca} instalada com sucesso.{Cores['reset']}")
    except subprocess.CalledProcessError:
        print(f"{Cores['reset']}[{Cores['vermelha']}x{Cores['reset']}]{Cores['vermelha']} Erro ao instalar {biblioteca}. Verifique a saída do comando para mais detalhes.{Cores['reset']}")

def instalar_bibliotecas_necessarias():
    bibliotecas = [
        "qdarkstyle",
        "PyQt5"
    ]

    print(f"\n{Cores['amarela']}Verificando bibliotecas...{Cores['reset']}")

    for biblioteca in bibliotecas:
        print(f"{Cores['reset']}[{Cores['amarela']}*{Cores['reset']}]{Cores['amarela']} Verificando {biblioteca}{Cores['reset']}")
        if verificar_biblioteca(biblioteca):
            print(f"{Cores['reset']}[{Cores['azul']}+{Cores['reset']}]{Cores['verde']} {biblioteca} já está instalada.{Cores['reset']}")
        else:
            instalar_biblioteca(biblioteca)

