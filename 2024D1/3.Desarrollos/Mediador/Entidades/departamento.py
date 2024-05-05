from pydantic import BaseModel
from datetime import datetime

class DepartamentoModelo(BaseModel):
    IdDepartamento: str
    Nombre: str
    activo: bool
    actualiza: datetime