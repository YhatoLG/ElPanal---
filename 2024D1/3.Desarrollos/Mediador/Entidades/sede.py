from pydantic import BaseModel
from datetime import datetime

class SedeModelo(BaseModel):
    IdSede: str
    NombreDeSede: str
    activo: bool
    actualiza: datetime