from pydantic import BaseModel
from bson import ObjectId

class domicilioModelo(BaseModel):
    _id: ObjectId
    Tarifas: str
    IdDomicilio: str
    ServicioOfrecidos: str
    IdTipo_De_Domicilio: str
    NombreDelTipoDeDomicilio: str

    def domicilio_helper(domicilio):
        return{
            "id": str(domicilio['_id']),
            "Tarifas": str(domicilio['Tarifas']),
            "IdDomicilio": str(domicilio['IdDomicilio']),
            "ServicioOfrecidos": str(domicilio['ServicioOfrecidos']),
            "IdTipo_De_Domicilio": str(domicilio['IdTipo_De_Domicilio']),
            "NombreDelTipoDeDomicilio": str(domicilio['NombreDelTipoDeDomicilio']),
        }