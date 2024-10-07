import os
import const


def get_List(url_files: str):
    name_categorias = os.listdir(url_files)
    for name_categoria in name_categorias:
        url_name_team = url_files + "/" + name_categoria + "/IMG"
        name_files = os.listdir(url_name_team)
        print(f"**********************| {name_categoria} |**********************")
        for name_file in name_files:
            file_path = url_name_team + "/" + name_file
            lenfile = os.listdir(file_path)
            if len(lenfile) > 18:
                print(name_file + "-1")
                print(name_file + "-2")

            else:
                print(name_file)
        print("******************************************************")


url_files = const.URL_BASE
get_List(url_files)
