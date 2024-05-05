from pydantic import BaseModel
from datetime import datetime

class TipoDeDomicilioModelo(BaseModel):
    IdTipoDeDomicilio: str
    Nombre_Del_Tipo_De_Domicilio: str
    servicio_ofrecidos: str
    tarifas: str
    activo: bool
    actualiza: datetime