import os
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from config import settings
from utils.logger import logger

def create_custom_pdf():
    """
    Genera un PDF A4 con las imágenes recortadas en una cuadrícula de 3x3.
    """
    base_dir = settings.BASE_DIR
    img_width = settings.PDF_IMG_WIDTH
    img_height = settings.PDF_IMG_HEIGHT
    margin = settings.PDF_MARGIN
    spacing = settings.PDF_SPACING
    
    logger.info("Iniciando generación de PDFs personalizados (A4)...")

    if not base_dir.exists():
        logger.error(f"Directorio base no encontrado: {base_dir}")
        return

    for category_path in base_dir.iterdir():
        if not category_path.is_dir():
            continue

        category_name = category_path.name
        img_base_dir = category_path / "IMG"
        
        if not img_base_dir.exists():
            continue

        for team_dir in img_base_dir.iterdir():
            if not team_dir.is_dir():
                continue

            team_name = team_dir.name
            
            # Recolectar imágenes recortadas
            cropped_images = sorted(
                [f for f in team_dir.iterdir() if f.name.startswith("r_") and f.suffix.lower() == ".png"],
                key=lambda x: x.name
            )

            if not cropped_images:
                continue
            
            logger.info(f"Procesando equipo para PDF: {team_name} ({len(cropped_images)} imágenes)")

            # Output to FINAL_PDF_DIR
            final_cat_dir = settings.FINAL_PDF_DIR / category_name
            final_cat_dir.mkdir(parents=True, exist_ok=True)
            
            output_filename = f"{team_name}.pdf" # User said "dejar los equipos en cada categoria"
            output_path = final_cat_dir / output_filename
            
            c = canvas.Canvas(str(output_path), pagesize=A4)
            width_a4, height_a4 = A4 # approx 595 x 842 points
            
            # Grid config
            cols = 3
            rows = 3
            images_per_page = cols * rows
            
            total_images = len(cropped_images)
            
            # Loop through images using an index
            for i in range(total_images):
                img_path = cropped_images[i]
                
                # Calculate index on current page (0 to 8)
                idx_on_page = i % images_per_page
                
                # Calculate row and col
                row = idx_on_page // cols
                col = idx_on_page % cols
                
                # Calculate X and Y coordinates
                # X: margin + (col * (width + spacing))
                x = margin + (col * (img_width + spacing))
                
                # Y: Top of page - margin - height - (row * (height + spacing))
                # Note: Coordinate system starts at bottom-left. 
                # So row 0 (top) needs to be near height_a4.
                y = height_a4 - margin - img_height - (row * (img_height + spacing))
                
                try:
                    c.drawImage(str(img_path), x, y, width=img_width, height=img_height)
                except Exception as e:
                    logger.error(f"Error dibujando imagen {img_path.name}: {e}")
                
                # If this is the last image on page OR last image total, showPage
                if idx_on_page == images_per_page - 1 or i == total_images - 1:
                    c.showPage()
            
            try:
                c.save()
                logger.info(f"PDF generado: {output_path}")
            except Exception as e:
                logger.error(f"Error guardando PDF {output_filename}: {e}")

    logger.info("Generación de PDFs A4 finalizada.")
