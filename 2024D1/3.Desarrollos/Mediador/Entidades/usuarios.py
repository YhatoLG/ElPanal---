from pydantic import BaseModel
from datetime import datetime

class UsuarioModelo(BaseModel):
    IdUsuario: str
    Nombre: str
    Apellido: str
    Numero_de_telefono: str
    activo: bool
    actualiza: datetime