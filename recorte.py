from PIL import Image
import os
import const

categoria = "Cat 12"
folder_path = const.URL_BASE + "/" + categoria + "/IMG"

files_folder = os.listdir(folder_path)

for folder in files_folder:

    image_path = folder_path + "/" + folder
    file_images = os.listdir(image_path)

    for file in file_images:

        name = file.replace(".png", "")
        img_name = f"r_{name}.png"
        img_path = image_path + "/" + file
        img = Image.open(img_path)
        region = (0, 0, 425, 529)
        img_recortada = img.crop(region)
        img_recortada.save(os.path.join(image_path, img_name), "PNG")

print("FIN RECORTE")
