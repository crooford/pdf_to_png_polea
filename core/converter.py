import os
from pathlib import Path
from pdf2image import convert_from_path
from config import settings
from utils.logger import logger

def convert_pdfs_to_images():
    """
    Convierte PDFs a imágenes PNG.
    Recorre BASE_DIR -> Categoría -> PDF, convierte cada PDF y guarda las imágenes en IMG/NombreEquipo.
    """
    base_dir = settings.BASE_DIR
    poppler_path = settings.POPPLER_PATH

    logger.info("Iniciando conversión de PDF a PNG...")

    if not base_dir.exists():
        logger.error(f"Directorio base no encontrado: {base_dir}")
        return

    for category_path in base_dir.iterdir():
        if not category_path.is_dir():
            continue

        category_name = category_path.name
        pdf_dir = category_path / "PDF"
        img_base_dir = category_path / "IMG"

        if not pdf_dir.exists():
            logger.warning(f"No hay carpeta PDF en {category_name}")
            continue

        for pdf_file in pdf_dir.iterdir():
            if pdf_file.suffix.lower() == ".pdf":
                team_name = pdf_file.stem
                output_folder = img_base_dir / team_name
                
                # Asegurar que existe la carpeta de salida (organizer.py ya debería haberla creado, pero por seguridad)
                output_folder.mkdir(parents=True, exist_ok=True)

                logger.info(f"Convirtiendo: {pdf_file.name} -> {output_folder}")

                try:
                    pages = convert_from_path(str(pdf_file), poppler_path=poppler_path)
                    
                    for i, page in enumerate(pages, start=1):
                        img_name = f"{team_name}_jugador-{i}.png"
                        save_path = output_folder / img_name
                        page.save(str(save_path), "PNG")
                        logger.debug(f"Guardada imagen: {img_name}")
                        
                except Exception as e:
                    logger.error(f"Error convirtiendo {pdf_file.name}: {e}")

    logger.info("Conversión de PDF a PNG finalizada.")
