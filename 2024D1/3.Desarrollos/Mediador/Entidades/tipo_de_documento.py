from pydantic import BaseModel
from datetime import datetime

class TipoDeDocumentoModelo(BaseModel):
    IdTipoDeDocumento: str
    TipoDeDocumento: str
    NumeroDocumento: str
    activo: bool
    actualiza: datetime