def setar_flag_true():
    flag_path = "conf/flag.txt"

    with open(flag_path, "w") as file:
        file.write("True")