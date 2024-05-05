from pydantic import BaseModel
from datetime import datetime

class EmpresaModelo(BaseModel):
    IdEmpresa: str
    NombreEmpresa: str
    Numero_de_Telefono: str
    activo: bool
    actualiza: datetime