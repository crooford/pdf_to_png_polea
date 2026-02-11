import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Settings:
    # Rutas base
    BASE_DIR: Path = Path(os.getenv("BASE_DIR", "./cats"))
    FINAL_PDF_DIR: Path = Path(os.getenv("FINAL_PDF_DIR", "./finalpdf"))
    
    # Configuración de Poppler
    POPPLER_PATH: str = os.getenv("POPPLER_PATH", "./poppler-0.68.0/bin")

    # Configuración de Procesamiento de Imágenes
    CROP_REGION: tuple = (0, 0, 424, 530)
    
    # Configuración de Documento Word
    DOC_IMAGES_PER_ROW: int = 3
    DOC_IMAGE_WIDTH_INCHES: float = 1.5

    # Configuración de Generador PDF (A4)
    PDF_IMG_WIDTH: float = 191.7  # px/pt
    PDF_IMG_HEIGHT: float = 239.63 # px/pt
    PDF_MARGIN: float = 2.0        # px/pt
    PDF_SPACING: float = 1.0       # px/pt

    def validate(self):
        """Valida que las rutas críticas existan o sean configurables."""
        if not os.path.exists(self.POPPLER_PATH):
            print(f"ADVERTENCIA: La ruta de Poppler no existe: {self.POPPLER_PATH}")

settings = Settings()
settings.validate()
