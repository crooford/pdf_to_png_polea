import os
from pdf2image import convert_from_path


# URL DE POPPLER DENTRO DEL SISTEMA
poppler_path = r"C:\Users\Seozz_\Downloads\poppler-0.68.0\bin"
# URL DE CARPETA DE PDFS PARA CONVERTIR A PNG
pdf_path = r"C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\PDF"

# URL DE CARPETA DONDE SE GUARDAN LAS IMAGENES CONVERTIDAS
folder = r"C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\IMG"
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
