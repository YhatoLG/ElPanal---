from pydantic import BaseModel
from datetime import datetime

class FacturaModelo(BaseModel):
    IdFactura: str
    NumComprobante: str
    IVA: float
    Total: float
    activo: bool
    actualiza: datetime