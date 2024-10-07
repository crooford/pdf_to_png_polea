import os
import const

dir = const.URL_BASE
files_dir = os.listdir(dir)
dir_save = const.URL_PDF_FIG

for file in files_dir:
    os.makedirs(dir_save + "/" + file)
print("EXITO RUTAS")
