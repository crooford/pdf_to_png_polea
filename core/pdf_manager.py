import os
import shutil
from pathlib import Path
from pypdf import PdfWriter, PdfReader
from config import settings
from utils.logger import logger

def manage_pdfs():
    """
    Gestiona la fusión o movimiento de PDFs finales.
    Basado en la cantidad de imágenes en la carpeta IMG, decide si fusionar 2 PDFs 
    o simplemente mover uno desde FIGMA_DIR a FINAL_PDF_DIR.
    """
    base_dir = settings.BASE_DIR
    figma_dir = settings.FIGMA_DIR
    final_pdf_dir = settings.FINAL_PDF_DIR

    logger.info("Iniciando gestión de PDFs finales...")

    if not final_pdf_dir.exists():
        final_pdf_dir.mkdir(parents=True, exist_ok=True)

    for category_path in base_dir.iterdir():
        if not category_path.is_dir():
            continue

        category_name = category_path.name
        img_base_dir = category_path / "IMG"
        
        # Crear carpeta de categoría en destino final
        final_category_dir = final_pdf_dir / category_name
        final_category_dir.mkdir(parents=True, exist_ok=True)

        if not img_base_dir.exists():
            continue

        for team_dir in img_base_dir.iterdir():
            if not team_dir.is_dir():
                continue

            team_name = team_dir.name
            
            # Contar imágenes en la carpeta del equipo
            # La lógica original contaba archivos totales. 
            # Aquí contaremos solo PNGs para ser más precisos, o todos si hay basura.
            # Original: len(os.listdir) > 18
            files_in_team = list(team_dir.iterdir())
            count = len(files_in_team)

            # Lógica de negocio: > 18 archivos implica 2 PDFs
            if count > 18:
                pdf1 = figma_dir / category_name / f"{team_name}-1.pdf"
                pdf2 = figma_dir / category_name / f"{team_name}-2.pdf"
                
                output_pdf = final_category_dir / f"{team_name}.pdf"
                
                if pdf1.exists() and pdf2.exists():
                    try:
                        merger = PdfWriter()
                        merger.append(str(pdf1))
                        merger.append(str(pdf2))
                        merger.write(str(output_pdf))
                        merger.close()
                        logger.info(f"Fusionado: {team_name}.pdf")
                    except Exception as e:
                        logger.error(f"Error fusionando {team_name}: {e}")
                else:
                    logger.warning(f"No se encontraron partes para fusionar {team_name}: {pdf1} o {pdf2}")
            else:
                # Caso contrario: solo mover
                source_pdf = figma_dir / category_name / f"{team_name}.pdf"
                dest_pdf = final_category_dir / f"{team_name}.pdf"
                
                if source_pdf.exists():
                    try:
                        shutil.copy(str(source_pdf), str(dest_pdf)) # Usamos copy para no destruir origen por si acaso
                        logger.info(f"Copiado: {team_name}.pdf")
                    except Exception as e:
                        logger.error(f"Error copiando {team_name}: {e}")
                else:
                    logger.warning(f"PDF original no encontrado: {source_pdf}")

    logger.info("Gestión de PDFs finalizada.")
