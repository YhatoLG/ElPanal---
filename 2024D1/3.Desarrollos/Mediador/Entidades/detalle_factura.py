from pydantic import BaseModel
from datetime import datetime

class DetalleFacturaModelo(BaseModel):
    IdDetalle_Factura: str
    Cotizacion: str
    Fecha: datetime
    Activo: bool
    Actualiza: datetime