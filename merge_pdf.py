from PyPDF2 import PdfMerger
import os
import shutil


def mergedFiles(cat: str, url_files: str, fig_cat: str):

    names_files = os.listdir(url_files)

    for name_file in names_files:

        file_path = url_files + "/" + name_file
        lenfile = os.listdir(file_path)

        if len(lenfile) > 18:

            pdfs = [
                f"C:/Users/Seozz_/Desktop/pdf-fig/{fig_cat}/{name_file}-1.pdf",
                f"C:/Users/Seozz_/Desktop/pdf-fig/{fig_cat}/{name_file}-2.pdf",
            ]
            print(pdfs)
            name_out = f"C:/Users/Seozz_/Desktop/CopaT/{cat}/{name_file}.pdf"
            fusionar = PdfMerger()

            for pdf in pdfs:
                fusionar.append(open(pdf, "rb"))
            with open(name_out, "wb") as salida_file:
                fusionar.write(salida_file)

        else:
            print(f"C:/Users/Seozz_/Desktop/pdf-fig/{fig_cat}/{name_file}.pdf")
            shutil.move(
                f"C:/Users/Seozz_/Desktop/pdf-fig/{fig_cat}/{name_file}.pdf",
                f"C:/Users/Seozz_/Desktop/CopaT/{cat}/"
            )


def get_List(url_files: str):
    name_files = os.listdir(url_files)
    for name_file in name_files:
        file_path = url_files + "/" + name_file
        lenfile = os.listdir(file_path)
        if len(lenfile) > 18:
            print(name_file,"-1")
            print(name_file,"-2")

        else:
            print(name_file)


url_files = r"C:\Users\Seozz_\Desktop\CopaT\Cat 08\IMG"
category = "Cat 08"
fig_cat = "cat08"

# get_List(url_files)

mergedFiles(category, url_files, fig_cat)