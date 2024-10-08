import os
import const
import shutil


def create_folders(url: str):
    split_url = url.split("/")
    split_url.pop(4)
    url_to_figma = "/".join(split_url)

    os.makedirs(url_to_figma + "/FigmaCopa")
    # listar todas las categorias y guardarlas en all categorias
    all_categorias = os.listdir(url)

    # para cada categoria dentro de all categorias se crearan las carpetas IMG y PDF
    for categoria in all_categorias:
        os.makedirs(const.URL_BASE + "/" + categoria + "/IMG")
        os.makedirs(const.URL_BASE + "/" + categoria + "/PDF")
        os.makedirs(const.URL_FOLDER_FIGMA + "/" + categoria)
        # se listan todos los pdfs de la categoria y se mueven a la carpeta PDF
        pdf_files = os.listdir(const.URL_BASE + "/" + categoria)
        for pdf_file in pdf_files:
            if pdf_file.endswith(".pdf"):

                shutil.move(
                    url + "/" + categoria + "/" + pdf_file,
                    const.URL_BASE + "/" + categoria + "/PDF",
                )
        # se listan todos los pdfs dentro de la carpeta PDF y se crean las carpetas correspondientes en IMG
        dir = const.URL_BASE + "/" + categoria + "/PDF"
        files_dir = os.listdir(dir)
        dir_save = const.URL_BASE + "/" + categoria + "/IMG"
        # para cada pdf dentro de la carpeta PDF se crea una carpeta con el nombre del pdf en la carpeta IMG
        for file in files_dir:
            name = file.replace(".pdf", "")
            os.makedirs(dir_save + "/" + name)

    print("EXITO RUTAS")


if __name__ == "__main__":
    create_folders(const.URL_BASE)
