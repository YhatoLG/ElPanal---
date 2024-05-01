from pydantic import BaseModel
from bson import ObjectId

class UsuarioModelo(BaseModel): 
    _id: ObjectId
    IdUsuario: str
    NombreUsuario: str
    TipoDocumento: str
    ApellidoUsuario: str
    NumeroDocumento: str
    TelefonoUsuario: str
    IdTipoDeDocumento: str

    def usuario_helper(usuario):
        return{
            "id": str(usuario['_id']),
            "IdUsuario": str(usuario['IdUsuario']),
            "NombreUsuario": str(usuario['NombreUsuario']),
            "TipoDocumento": str(usuario['TipoDocumento']),
            "ApellidoUsuario": str(usuario['ApellidoUsuario']),
            "NumeroDocumento": str(usuario['NumeroDocumento']),
            "TelefonoUsuario": str(usuario['TelefonoUsuario']),
            "IdTipoDeDocumento": str(usuario['IdTipoDeDocumento']),
        }
    
