from PyPDF2 import PdfMerger
import os
import shutil
import const


def mergedFiles(categoria: str, url_files: str):

    names_files = os.listdir(url_files)
    print(names_files)

    for name_file in names_files:

        file_path = url_files + "/" + name_file
        lenfile = os.listdir(file_path)

        if len(lenfile) > 18:

            pdfs = [
                f"{const.URL_PDF_FIG}/{categoria}/{name_file}-1.pdf",
                f"{const.URL_PDF_FIG}/{categoria}/{name_file}-2.pdf",
            ]
            print(pdfs)
            name_out = f"{const.URL_BASE}/{categoria}/{name_file}.pdf"
            fusionar = PdfMerger()

            for pdf in pdfs:
                fusionar.append(open(pdf, "rb"))
            with open(name_out, "wb") as salida_file:
                fusionar.write(salida_file)

        else:
            print(f"{const.URL_PDF_FIG}/{categoria}/{name_file}.pdf")
            shutil.move(
                f"{const.URL_PDF_FIG}/{categoria}/{name_file}.pdf",
                f"{const.URL_BASE}/{categoria}/",
            )


categoria = "Cat 12"
url_files = const.URL_BASE + "/" + categoria + "/IMG"


mergedFiles(categoria, url_files)
