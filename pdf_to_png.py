import os
from pdf2image import convert_from_path
import const

# URL DE POPPLER DENTRO DEL SISTEMA
poppler_path = const.URL_POPPLER

# URL DE CARPETA DE PDFS PARA CONVERTIR A PNG
pdf_path = const.URL_PDF

# URL DE CARPETA DONDE SE GUARDAN LAS IMAGENES CONVERTIDAS
folder = const.URL_IMG
file_pdf = os.listdir(pdf_path)

for file in file_pdf:
    name = file.replace(".pdf", "")
    file_path = pdf_path + "/" + file
    pages = convert_from_path(pdf_path=file_path, poppler_path=poppler_path)
    saving_folder = folder + "/" + name
    c = 1
    for page in pages:
        img_name = f"{name}_jugador-{c}.png"
        page.save(os.path.join(saving_folder, img_name), "PNG")
        c += 1
print("FIN PDF TO PNG")
