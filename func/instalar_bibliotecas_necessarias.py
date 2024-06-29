import subprocess

cor_vermelha = "\033[1;31m"
cor_verde = "\033[1;32m"
cor_amarela = "\033[1;33m"
cor_azul = "\033[1;34m"
cor_roxa = "\033[1;35m"
cor_ciano = "\033[1;36m"
cor_branca = "\033[1;37m"
cor_reset = "\033[0m" 

def instalar_bibliotecas_necessarias():
    bibliotecas = [
        "qdarkstyle",
        "colorama",
        "PyQt5",
        "matplotlib",
        "pyinstaller"
    ]

    print(f"\n{cor_amarela}Verificando bibliotecas...{cor_reset}")

    for biblioteca in bibliotecas:
        print(f"{cor_reset}[{cor_amarela}*{cor_reset}]{cor_amarela} Verificando {biblioteca}{cor_reset}")
        try:
            __import__(biblioteca)
            print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} {biblioteca} Verificada {cor_reset}")
        except ImportError:
            print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Instalando biblioteca {biblioteca}{cor_reset}")
            # Comando para instalar a biblioteca usando pip
            subprocess.check_call(["pip", "install", biblioteca])
