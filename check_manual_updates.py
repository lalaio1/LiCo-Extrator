import subprocess
import urllib.request
import os

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

if __name__ == "__main__":
    os.system("clear" if os.name != "nt" else "cls")
    check_for_updates()