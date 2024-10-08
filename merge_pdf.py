from PyPDF2 import PdfMerger
import os
import shutil
import const


def mergedFiles(categoria: str, url_files: str, url_files_figma: str):
    # lista de los nombres de los equipos dentro de la categoria indicada sacados de los nombres de las carpetas de IMG
    path_name_files = f"{url_files}/{categoria}/IMG"
    names_files = os.listdir(path_name_files)

    for name_file in names_files:
        # ruta de cada equipo para chequeo de numero de elementos dentro de la carpeta
        file_path = path_name_files + "/" + name_file
        lenfile = os.listdir(file_path)
        # si el numero de elementos es mayor a 18 significa que hay 2 pdfs para fusionar
        if len(lenfile) > 18:
            # lista de los pdfs para fusionar
            pdfs = [
                f"{url_files_figma}/{name_file}-1.pdf",
                f"{url_files_figma}/{name_file}-2.pdf",
            ]
            # nombre de salida del pdf fusionado
            name_out = f"{url_files}/{categoria}/{name_file}.pdf"
            fusionar = PdfMerger()
            # fusiona los pdfs por cada pdf dentro de la lista de pdfs
            for pdf in pdfs:
                fusionar.append(open(pdf, "rb"))
            with open(name_out, "wb") as salida_file:
                fusionar.write(salida_file)
            print(f"se fusiono el equipo {name_file}")
        # si el numero de elementos es menor a 18 significa que solo hay 1 pdf por lo tanto solo se mueve el pdf
        else:
            shutil.move(
                f"{url_files_figma}/{name_file}.pdf", f"{url_files}/{categoria}/"
            )
            print(f"se movio el equipo {name_file}")

    print(f"cantidad de pdfs {len(names_files)}")


categoria = "Cat 17"
url_files = const.URL_BASE
url_files_figma = const.URL_FOLDER_FIGMA + "/" + categoria
# print(url_files_figma, url_files, (url_files + "/" + categoria))
mergedFiles(categoria, url_files, url_files_figma)
