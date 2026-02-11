import os
from pathlib import Path
from PIL import Image
from config import settings
from utils.logger import logger

def crop_images():
    """
    Recorta las imágenes generadas.
    Busca imágenes en IMG/NombreEquipo, las recorta y guarda con prefijo 'r_'.
    """
    base_dir = settings.BASE_DIR
    crop_region = settings.CROP_REGION

    logger.info("Iniciando recorte de imágenes...")

    if not base_dir.exists():
        logger.error(f"Directorio base no encontrado: {base_dir}")
        return

    for category_path in base_dir.iterdir():
        if not category_path.is_dir():
            continue

        img_base_dir = category_path / "IMG"
        if not img_base_dir.exists():
            continue

        for team_dir in img_base_dir.iterdir():
            if not team_dir.is_dir():
                continue

            # Iterar sobre las imágenes en la carpeta del equipo
            for img_file in team_dir.iterdir():
                # Procesar solo PNGs que NO empiecen con 'r_' (para evitar re-procesar o procesar ya recortadas)
                if img_file.suffix.lower() == ".png" and not img_file.name.startswith("r_"):
                    output_name = f"r_{img_file.name}"
                    output_path = team_dir / output_name

                    # Si ya existe, podemos saltar o sobrescribir. Por ahora sobrescribimos.
                    try:
                        with Image.open(img_file) as img:
                            cropped_img = img.crop(crop_region)
                            cropped_img.save(output_path, "PNG")
                            logger.debug(f"Imagen recortada: {output_name}")
                    except Exception as e:
                        logger.error(f"Error recortando {img_file.name}: {e}")

    logger.info("Recorte de imágenes finalizado.")
