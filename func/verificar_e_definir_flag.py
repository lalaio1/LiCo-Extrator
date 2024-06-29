import os

def verificar_e_definir_flag():
    flag_path = "conf/flag.txt"

    if os.path.exists(flag_path):
        with open(flag_path, "r") as file:
            flag_status = file.read().strip()
    else:
        flag_status = "False"

    return flag_status