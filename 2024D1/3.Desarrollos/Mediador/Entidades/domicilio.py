from pydantic import BaseModel
from datetime import datetime

class DomicilioModelo(BaseModel):
    idDomicilio: str
    activo: bool
    actualiza: datetime