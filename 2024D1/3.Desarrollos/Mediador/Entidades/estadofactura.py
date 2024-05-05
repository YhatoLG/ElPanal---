from  pydantic import BaseModel
from datetime import datetime

class EstadoFacturaModelo(BaseModel):
    IdEstadoFactura: str
    EstadoFactura: str
    activo: bool
    actualiza: datetime