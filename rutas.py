import os

dir=r'C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\PDF'
files_dir=os.listdir(dir)
dir_save=r'C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\IMG'
print(files_dir)
for file in files_dir:
    name=file.replace('.pdf','')
    os.makedirs(dir_save +'/'+name)