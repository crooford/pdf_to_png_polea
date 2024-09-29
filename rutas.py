import os
import const

dir = const.URL_PDF
files_dir = os.listdir(dir)
dir_save = const.URL_SAVE

for file in files_dir:
    name = file.replace(".pdf", "")
    os.makedirs(dir_save + "/" + name)
print("EXITO RUTAS")
