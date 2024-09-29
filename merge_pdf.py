from PyPDF2 import PdfMerger
import os
import shutil

def mergedFiles(cat:str , url_files:str):
    
    names_files=os.listdir(url_files)

    for name_file in names_files:

        file_path = url_files + "/" + name_file
        lenfile= os.listdir(file_path)

        if len(lenfile) > 9:

            pdfs=[f"C:/Users/Seozz_/Downloads/{name_file} pag1.pdf",f"C:/Users/Seozz_/Downloads/{name_file} pag2.pdf"]
            name_out=f"C:/Users/Seozz_/Downloads/TRABAJO/POKAL/TIMON/{cat}/{name_file}.pdf"
            fusionar = PdfMerger()

            for pdf in pdfs:
                fusionar.append(open(pdf, "rb"))
            with open(name_out, "wb") as salida_file:
                fusionar.write(salida_file)
     
        else:

            shutil.move(f"C:/Users/Seozz_/Downloads/{name_file}.pdf", f"C:/Users/Seozz_/Downloads/TRABAJO/POKAL/TIMON/{cat}/")
            
      

def get_List(url_files:str):
    name_files = os.listdir(url_files)
    for name_file in name_files:
        file_path = url_files + "/" + name_file
        lenfile= os.listdir(file_path)
        if len(lenfile) > 9:
            print(name_file,"pag1")
            print(name_file,"pag2")

        else:
            print(name_file)



url_files = r"C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\2012\IMG"
category = "2012"

get_List(url_files)

mergedFiles(category, url_files)