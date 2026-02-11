import typer
from core import organizer, converter, image_processor, pdf_manager, document_builder, pdf_generator
from utils.logger import logger

app = typer.Typer(help="Herramienta de procesamiento de PDFs para Polea")

@app.command()
def organize():
    """Organiza los archivos en carpetas."""
    organizer.create_structure()

@app.command()
def convert():
    """Convierte los PDFs a imágenes PNG."""
    converter.convert_pdfs_to_images()

@app.command()
def crop():
    """Recorta las imágenes generadas."""
    image_processor.crop_images()

@app.command()
def merge():
    """Gestiona los PDFs finales (fusión/movimiento) para Figma."""
    pdf_manager.manage_pdfs()

@app.command()
def create_doc():
    """Genera documentos Word con las imágenes recortadas."""
    document_builder.create_word_docs()

@app.command()
def create_pdf():
    """Genera archivos PDF A4 con las imágenes recortadas (3x3)."""
    pdf_generator.create_custom_pdf()

@app.command()
def run_all():
    """Ejecuta todo el pipeline en orden: Organizar -> Convertir -> Recortar -> Generar PDF Final."""
    logger.info("Iniciando pipeline completo...")
    organizer.create_structure()
    converter.convert_pdfs_to_images()
    image_processor.crop_images()
    # pdf_manager.manage_pdfs()  # Deshabilitado por solicitud del usuario
    # document_builder.create_word_docs() # Deshabilitado por solicitud del usuario
    pdf_generator.create_custom_pdf()
    logger.info("Pipeline completado exitosamente.")

if __name__ == "__main__":
    app()
