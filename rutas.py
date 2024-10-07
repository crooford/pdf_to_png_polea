import os
import const
import shutil


def create_folders(url: str):
    all_categorias = os.listdir(url)

    for categoria in all_categorias:
        os.makedirs(const.URL_BASE + "/" + categoria + "/IMG")
        os.makedirs(const.URL_BASE + "/" + categoria + "/PDF")
        pdf_files = os.listdir(const.URL_BASE + "/" + categoria)
        for pdf_file in pdf_files:
            if pdf_file.endswith(".pdf"):

                shutil.move(
                    url + "/" + categoria + "/" + pdf_file,
                    const.URL_BASE + "/" + categoria + "/PDF",
                )
        dir = const.URL_BASE + "/" + categoria + "/PDF"
        files_dir = os.listdir(dir)
        dir_save = const.URL_BASE + "/" + categoria + "/IMG"

        for file in files_dir:
            name = file.replace(".pdf", "")
            os.makedirs(dir_save + "/" + name)

    print("EXITO RUTAS")


if __name__ == "__main__":
    create_folders(const.URL_BASE)
