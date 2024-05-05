from pydantic import BaseModel
from datetime import datetime

class EmpleadoModelo(BaseModel):
    IdEmpleado: str
    Nombre_Del_Tecnico: str
    Numero_De_Telefono: str
    activo: bool
    actualiza: datetime