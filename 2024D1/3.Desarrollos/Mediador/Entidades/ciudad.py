from pydantic import BaseModel
from datetime import datetime

class CiudadModelo(BaseModel):
    IdCiudad: str
    Nombre: str
    Direccion: str
    Codigo_Postal: str
    Municipio: str
    activo: bool
    actualiza: datetime