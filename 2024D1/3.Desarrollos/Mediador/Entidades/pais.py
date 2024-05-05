from pydantic import BaseModel
from datetime import datetime

class PaisModelo(BaseModel):
    IdPais: str
    Nombre: str
    activo: bool
    actualiza: datetime

