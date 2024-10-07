import os
import const

categoria = "Cat 11"
dir = const.URL_RUTAS
files_dir = os.listdir(dir)
dir_save = const.URL_RUTAS_SAVE

for file in files_dir:
    name = file.replace(".pdf", "")
    os.makedirs(dir_save + "/" + name)
print("EXITO RUTAS")
