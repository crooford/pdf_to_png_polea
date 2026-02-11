import os
import shutil
from pathlib import Path
from config import settings
from utils.logger import logger

def create_structure():
    """
    Recrea la lógica de rutas.py:
    1. Crea carpetas base si no existen.
    2. Organiza los PDFs en carpetas por categoría/equipo.
    """
    base_dir = settings.BASE_DIR
    
    logger.info(f"Iniciando organización en {base_dir}")

    if not base_dir.exists():
        logger.error(f"El directorio base no existe: {base_dir}")
        return

    # Iterar sobre categorías en BASE_DIR
    for category_path in base_dir.iterdir():
        if not category_path.is_dir():
            continue
        
        category_name = category_path.name
        logger.info(f"Procesando categoría: {category_name}")

        # Crear subcarpetas IMG y PDF
        img_dir = category_path / "IMG"
        pdf_dir = category_path / "PDF"
        
        img_dir.mkdir(exist_ok=True)
        pdf_dir.mkdir(exist_ok=True)
        
        # Mover PDFs de la raíz de la categoría a la carpeta PDF
        for file in category_path.iterdir():
            if file.is_file() and file.suffix.lower() == ".pdf":
                target = pdf_dir / file.name
                shutil.move(str(file), str(target))
                logger.debug(f"Movido {file.name} a PDF/")

        # Crear carpetas para cada equipo dentro de IMG basado en los PDFs
        # La lógica original itera sobre los PDFs que acabamos de mover
        for pdf_file in pdf_dir.iterdir():
            if pdf_file.suffix.lower() == ".pdf":
                team_name = pdf_file.stem # nombre sin extensión
                team_img_dir = img_dir / team_name
                team_img_dir.mkdir(exist_ok=True)
                logger.debug(f"Directorio de equipo creado: {team_img_dir}")

    logger.info("Organización de archivos completada.")
