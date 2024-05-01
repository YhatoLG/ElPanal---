from pydantic import BaseModel
from bson import ObjectId

class OrganizacionModelo(BaseModel):
    _id: ObjectId
    IdSede: str
    NombreDeSede: str
    IdEmpresa: str
    NombreEmpresa: str
    Numero_de_Telefono: str
    IdEmpleado: str
    NumeroDeTelefono: str
    NombreDelEmpleado: str

    def organizacion_helper(organizacion):
        return{
            "id": str(organizacion['_id']),
            "IdSede": str(organizacion['IdSede']),
            "NombreDeSede": str(organizacion['NombreDeSede']),
            "IdEmpresa": str(organizacion['IdEmpresa']),
            "NombreEmpresa": str(organizacion['NombreEmpresa']),
            "Numero_de_Telefono": str(organizacion['Numero_de_Telefono']),
            "IdEmpleado": str(organizacion['IdEmpleado']),
            "NumeroDeTelefono": str(organizacion['NumeroDeTelefono']),
            "NombreDelEmpleado": str(organizacion['NombreDelEmpleado']),
        }