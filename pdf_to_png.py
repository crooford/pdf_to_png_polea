import os
from pdf2image import convert_from_path

poppler_path= r"C:\Users\Seozz_\Downloads\poppler-0.68.0\bin"

pdf_path = r"C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\PDF"


folder=r'C:\Users\Seozz_\Downloads\TRABAJO\POKAL\TIMON\Correciones\IMG'
file_pdf=os.listdir(pdf_path)

for file in file_pdf:
    name=file.replace('.pdf','')
    file_path=pdf_path+'/'+file
    pages = convert_from_path(pdf_path=file_path , poppler_path= poppler_path)
    saving_folder= folder+'/'+name
    c=1
    for page in pages:
        img_name = f"{name}_jugador-{c}.png"
        page.save(os.path.join(saving_folder, img_name),"PNG")
        c+=1




# def pendiente(x1,y1,x2,y2,x):
#     restay=(y2-y1)
#     restax=(x2-x1)
#     m= restay/restax
#     xcorte=m*(-x1)
#     sumaxy= xcorte+y1
#     penx= m*x
#     y= penx + sumaxy
#     print('resta y = ',restay,' resta x = ',restax ,' pendinte m = ', m)
#     print('pendiente por x1 = ',xcorte,' suma y1 mas multi = ',sumaxy ,'pen por x= ',penx,' y = ', y)


# pendiente(4,868,6,1152,15)
# import os
# from PIL import Image
# import math
# import PyPDF2

# # Definir la carpeta donde están los archivos PDF
# pdf_folder = 'C:\Users\Seozz_\Documents\Polea\2015\Chamacos'

# # Definir el tamaño de las miniaturas de las páginas
# thumbnail_size = (1080, 2490)

# # Definir el número de columnas y filas del grid
# grid_columns = 3
# grid_rows = 3

# # Crear una lista de todos los archivos PDF en la carpeta
# pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# # Crear una lista para almacenar todas las miniaturas de todas las páginas de todos los archivos
# thumbnails = []

# # Para cada archivo PDF
# for pdf_file in pdf_files:
#     # Abrir el archivo PDF y obtener el número de páginas
#     with open(os.path.join(pdf_folder, pdf_file), 'rb') as f:
#         pdf_reader = PyPDF2.PdfFileReader(f)
#         num_pages = pdf_reader.getNumPages()
        
#         # Para cada página del archivo
#         for page_num in range(num_pages):
#             # Leer la página y crear una miniatura
#             page = pdf_reader.getPage(page_num)
#             page_image = page.extractText().encode('utf-8')
#             im = Image.open(page_image)
#             im.thumbnail(thumbnail_size)
            
#             # Agregar la miniatura a la lista de miniaturas
#             thumbnails.append(im)

# # Calcular el número de miniaturas que caben en el grid
# num_thumbnails = len(thumbnails)
# grid_size = grid_columns * grid_rows
# num_rows = math.ceil(num_thumbnails / grid_columns)
# if num_rows > grid_rows:
#     num_rows = grid_rows

# # Crear una imagen de fondo para el grid
# grid_size_px = (grid_columns * thumbnail_size[0], grid_rows * thumbnail_size[1])
# grid_image = Image.new('RGB', grid_size_px, (255, 255, 255))

# # Para cada miniatura en la lista de miniaturas
# for i, thumbnail in enumerate(thumbnails):
#     # Calcular la posición de la miniatura en el grid
#     col_num = i % grid_columns
#     row_num = i // grid_columns
    
#     # Calcular la posición de la miniatura en la imagen de fondo del grid
#     pos_x = col_num * thumbnail_size[0]
#     pos_y = row_num * thumbnail_size[1]
    
#     # Pegar la miniatura en la imagen de fondo del grid
#     grid_image.paste(thumbnail, (pos_x, pos_y))
    
#     # Si se han pegado suficientes miniaturas en el grid, guardar el grid como un archivo PDF
#     if i == grid_size - 1:
#         output_file_name = os.path.splitext(pdf_file)[0] + '_grid.pdf'
#         with open(os.path.join(pdf_folder, output_file_name), 'wb') as f:
#             grid_image.save(f, 'PDF', resolution=100.0)
#         break

#     # Si no se han pegado suficientes miniaturas en el grid, mostrar un mensaje de advertencia
#     if len(thumbnails) < grid_size:
#         print(f'Warning: only {len(thumbnails)} thumbnails were created, which is not enough to fill a {grid_columns}x{grid_rows} grid.')


# #Recuerda que debes cambiar la variable `pdf_folder` en el código para que apunte a la carpeta donde están los archivos PDF que quieres procesar. Además, puedes ajustar los valores de `thumbnail_size`, `grid_columns` y `grid_rows` para obtener el resultado deseado.

# pages = convert_from_path(pdf_path=pdf_path , poppler_path= poppler_path)

# saving_folder= r"C:\Users\Seozz_\Documents\Polea\2011\DRAGONES"



