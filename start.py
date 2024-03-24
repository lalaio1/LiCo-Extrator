import subprocess
import sys
import os
import urllib.request

#variavel das cores
cor_vermelha = "\033[1;31m"
cor_verde = "\033[1;32m"
cor_amarela = "\033[1;33m"
cor_azul = "\033[1;34m"
cor_roxa = "\033[1;35m"
cor_ciano = "\033[1;36m"
cor_branca = "\033[1;37m"
cor_reset = "\033[0m"  


   

def dragondfa():
    banner = f"""{cor_vermelha}


──────────────▒███░───░████████▒ 
───────────█████▒░█████░▒▒▒▒▒▒█████ 
──────────██▒▒▒▒██████████████▒▒▒██░ 
─────────██▒▒▒▒███▒██▒██▒▒█████▒░▒██ 
─────────█░▒▒▒██▒████████████▒█▒▒▒█░ 
─────────█▒▒▒▒██▒▒▒░▓▓▒░▓▒▒████▒▒██ 
─────────█▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒█▒█░▒████ 
─────███████████▒▒▒▒▒▒▒▒██████▒██▓▒███ 
─────██▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒█████▒▒▒▒▒██ 
───────██▒▒▒▒▒▒▒▓██████▒▒▒▒▒██▒▒▒▒▒▒███ 
────█████▒▒▒▒▒▒▒▒▒▒████▒▒▒██▒▒▒▒▒▒███ 
────██▒▒▒███▒▒▒▒▒▒▒▒▒▒▓█████▒▒▒▒▒███ 
────███▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒███▓▒▒███ 
──────█████▒▒████▒▒▒▒▒▒▒▒▒▒█████ 
─────────████▒▒██████▒▒▒▒█████ 
────────────███▒▒██████████ 
──────────────████▓──█▓█ 
────────────────────████ 
────────────────────█░█─────█████████ 
────────────────────█▓█───█████████████ 
──░█████████───────████──██▓███▒▓████ 
─█████████████─────█░███████░██████ 
───████░▒███▒██────█▓██████████ 
─────█████▓▒█████─████ 
─────────██████████▓█ 
──────────────────█▓█────████▒█▓▒█ 
─────────────────█▓██──█████████████ 
─────────────────█▓█──██▒████░█████ 
────────────────██████████▒██████ 
────────────────█▓███████████ 
───────────────████ 
───────────────█▒█ 
───────────────███ 

            """
    print(banner)

# Chame a função 'imprimir_banner()' onde você deseja exibir o banner


def instalar_bibliotecas_necessarias():
    bibliotecas = [
    "qdarkstyle",
    "colorama",
    "PyQt5",
    "matplotlib",
    "pywin32",
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
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])

def verificar_e_definir_flag():
    flag_path = "conf/flag.txt"

    if os.path.exists(flag_path):
        with open(flag_path, "r") as file:
            flag_status = file.read().strip()
    else:
        flag_status = "False"

    return flag_status

def setar_flag_true():
    flag_path = "conf/flag.txt"

    with open(flag_path, "w") as file:
        file.write("True")




def check_for_updates():
    try:
        with urllib.request.urlopen("https://raw.githubusercontent.com/lalaio1/LiCo-Extrator/main/version.txt") as response:
            latest_version = response.read().decode().strip()
            current_version = get_current_version()
            if latest_version != current_version:
                print("[!] Uma nova versão está disponível. Atualizando...")
                update_repository()
                update_version_file(latest_version)
                print("[/] Atualização concluída com sucesso.")
            else:
                print("[i] Você já tem a versão mais recente.")
    except Exception as e:
        print(f"[e] Erro ao verificar atualizações: {e}")

def get_current_version():
    try:
        with open("version.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def update_repository():
    try:
        subprocess.run(["git", "pull"])
    except Exception as e:
        print(f"[e] Erro ao atualizar o repositório: {e}")

def update_version_file(version):
    try:
        with open("version.txt", "w") as file:
            file.write(version)
    except Exception as e:
        print(f"[e] Erro ao atualizar o arquivo de versão: {e}")


def imprimir_banner():
    banner = """
 ██▓     ██▓ ▄████▄   ▒█████      ██▒   █▓▓█████  ██▀███   ██▓  █████▒▓██   ██▓
▓██▒    ▓██▒▒██▀ ▀█  ▒██▒  ██▒   ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓██▒▓██   ▒  ▒██  ██▒
▒██░    ▒██▒▒▓█    ▄ ▒██░  ██▒    ▓██  █▒░▒███   ▓██ ░▄█ ▒▒██▒▒████ ░   ▒██ ██░  
▒██░    ░██░▒▓▓▄ ▄██▒▒██   ██░     ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░██░░▓█▒  ░   ░ ▐██▓░
░██████▒░██░▒ ▓███▀ ░░ ████▓▒░      ▒▀█░  ░▒████▒░██▓ ▒██▒░██░░▒█░      ░ ██▒▓░
░ ▒░▓  ░░▓  ░ ░▒ ▒  ░░ ▒░▒░▒░       ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░░▓   ▒ ░       ██▒▒▒ 
░ ░ ▒  ░ ▒ ░  ░  ▒     ░ ▒ ▒░       ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ▒ ░ ░       ▓██ ░▒░ 
  ░ ░    ▒ ░░        ░ ░ ░ ▒          ░░     ░     ░░   ░  ▒ ░ ░ ░     ▒ ▒ ░░  
    ░  ░ ░  ░ ░          ░ ░           ░     ░  ░   ░      ░           ░ ░     
            ░                         ░                                ░ ░            

            
┳┓•       ┓   ┓  ┓  •  ┓
┃┃┓┏┏┏┓┏┓┏┫•  ┃┏┓┃┏┓┓┏┓┃
┻┛┗┛┗┗┛┛ ┗┻•  ┗┗┻┗┗┻┗┗┛┻
                                    
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
    print(f"{cor_azul} {cor_roxa} {banner}{cor_reset}")



if __name__ == "__main__":
    os.system("clear" if os.name != "nt" else "cls")

    flag_status = verificar_e_definir_flag()

    if flag_status == "True":
        print(f"{cor_azul}[{cor_verde}+{cor_azul}] Verificação já foi executada anteriormente {cor_reset}")
        os.system("clear" if os.name != "nt" else "cls")
        if os.name == "nt":
            dragondfa()
            python_command = "python"
        else:  # Ambientes Unix
            python_command = "python3"
        check_for_updates()
        os.system(f"{python_command} ./conf/scripts/main.pyw")
    else:
        imprimir_banner()
        instalar_bibliotecas_necessarias()
        setar_flag_true()
        print(f"{cor_azul}[{cor_verde}!{cor_azul}] Bibliotecas instaladas. Verificação concluída.{cor_reset}")
        if os.name == "nt":
            dragondfa()
            python_command = "python"
        else:  # Ambientes Unix
            python_command = "python3"
        check_for_updates()
        os.system(f"{python_command} ./conf/scripts/main.pyw")
