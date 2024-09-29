from PIL import Image
import os

folder_path=r'C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\IMG'

files_folder=os.listdir(folder_path)

for folder in files_folder:

    image_path= folder_path+'/'+folder
    file_images= os.listdir(image_path)

    for file in file_images:

        name=file.replace('.png','')
        img_name=f'r_{name}.png'
        img_path= image_path +'/'+ file
        img= Image.open(img_path)
        region= (0,0,425,535)
        img_recortada= img.crop(region)
        img_recortada.save(os.path.join(image_path, img_name),"PNG")



# image_path=r"C:\Users\Seozz_\Documents\Polea\2012\Zancudos\jugador-11.png"

# saving_folder= r"C:\Users\Seozz_\Documents\Polea\2012\Zancudos"

# img_name="r_jugador-11.png"

# img= Image.open(image_path)

# #425*678

##region= (0,0,425,535)

# img_recortada= img.crop(region)

# # img_recortada.show()

# img_recortada.save(os.path.join(saving_folder, img_name),"PNG")



    




