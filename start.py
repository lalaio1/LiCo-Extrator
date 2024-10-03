import subprocess
import os
from func.instalar_bibliotecas_necessarias import instalar_bibliotecas_necessarias
from func.verificar_e_definir_flag import verificar_e_definir_flag
from func.setar_flag_true import setar_flag_true
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

def exibir_banner(titulo):
    print(f"{Cores['azul']} {Cores['roxa']} {titulo}{Cores['reset']}")

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar_tela()

    flag_status = verificar_e_definir_flag()

    if flag_status == "True":
        if os.name == "nt":
            exibir_banner("Dragondfa")
        subprocess.run([sys.executable, "./conf/scripts/main.pyw"])
    else:
        exibir_banner("Iniciando a instalação das bibliotecas...")
        instalar_bibliotecas_necessarias()
        setar_flag_true()
        print(f"{Cores['azul']}[{Cores['verde']}!{Cores['azul']}] Bibliotecas instaladas. Verificação concluída.{Cores['reset']}")
        
        if os.name == "nt":
            exibir_banner("Dragondfa")
        subprocess.run([sys.executable, "./conf/scripts/main.pyw"])

if __name__ == "__main__":
    main()