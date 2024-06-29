import subprocess
import os
from func.instalar_bibliotecas_necessarias import instalar_bibliotecas_necessarias
from func.verificar_e_definir_flag import verificar_e_definir_flag
from func.setar_flag_true import setar_flag_true

cor_vermelha = "\033[1;31m"
cor_verde = "\033[1;32m"
cor_amarela = "\033[1;33m"
cor_azul = "\033[1;34m"
cor_roxa = "\033[1;35m"
cor_ciano = "\033[1;36m"
cor_branca = "\033[1;37m"
cor_reset = "\033[0m"  


def dragondfa():
    banner = f"""
            """
    print(banner)


def imprimir_banner():
    banner = """
"""
    print(f"{cor_azul} {cor_roxa} {banner}{cor_reset}")

python_command = "python"

if __name__ == "__main__":
    if os.name == "posix": 
        os.system("clear")
    elif os.name == "nt":  
        os.system("cls")

    flag_status = verificar_e_definir_flag()

    if flag_status == "True":
        print(f"{cor_azul}[{cor_verde}+{cor_azul}] Verificação já foi executada anteriormente {cor_reset}")
        if os.name == "nt":
            dragondfa()

        subprocess.run([python_command, "./conf/scripts/main.pyw"])
    else:
        imprimir_banner()
        instalar_bibliotecas_necessarias()
        setar_flag_true()
        print(f"{cor_azul}[{cor_verde}!{cor_azul}] Bibliotecas instaladas. Verificação concluída.{cor_reset}")
        if os.name == "nt":
            dragondfa()

        subprocess.run([python_command, "./conf/scripts/main.pyw"])