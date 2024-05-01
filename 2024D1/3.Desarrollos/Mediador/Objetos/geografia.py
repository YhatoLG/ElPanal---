# geografia:

from pydantic import BaseModel
from bson import ObjectId

class GeografiaModelo(BaseModel):
    _id: ObjectId
    idpais: str
    iddepartamento: str
    idciudad: str
    nombrepais: str
    nombredepartamento: str
    nombreciudad: str

    def geografia_helper(geografia):
        return{
            "id": str(geografia['_id']),
            "IdPais": str(geografia['IdPais']),
            "IdDepartamento": str(geografia['IdDepartamento']),
            "IdCiudad": str(geografia['IdCiudad']),
            "NombrePais": str(geografia['NombrePais']),
            "NombreDepartamento": str(geografia['NombreDepartamento']),
            "NombreCiudad": str(geografia['NombreCiudad']),
        }