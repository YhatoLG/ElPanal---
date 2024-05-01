from pydantic import BaseModel
from bson import ObjectId

class TransaccionalModelo(BaseModel):
    _id: ObjectId
    IVA: str
    Fecha: str
    Total: str
    Estado: str
    IdFactura: str
    Cotizacion: str
    NumComprobante: str
    IdEstadoFactura: str
    IdDetalle_Factura: str

    def transaccional_helper(transaccional):
        return{
            "id": str(transaccional['_id']),
            "IVA": str(transaccional['IVA']),
            "Fecha": str(transaccional['Fecha']),
            "Total": str(transaccional['Total']),
            "Estado": str(transaccional['Estado']),
            "IdFactura": str(transaccional['IdFactura']),
            "Cotizacion": str(transaccional['Cotizacion']),
            "NumComprobante": str(transaccional['NumComprobante']),
            "IdEstadoFactura": str(transaccional['IdEstadoFactura']),
            "IdDetalle_Factura": str(transaccional['IdDetalle_Factura']),
        }