from fastapi import FastAPI 
import pymongo
from Objetos.geografia import GeografiaModelo
from Objetos.organizacion import OrganizacionModelo
from Objetos.transaccional import TransaccionalModelo
from Objetos.domicilio import domicilioModelo
from Objetos.usuario import UsuarioModelo



app: FastAPI = FastAPI(
    title="Mediador de Objeto",
    description="Mediador de Objeto"
)


#################################################

#objeto 
@app.post( 
    "/consultargeografia",
    response_model=list,
    summary="Consultar Geografia",
    description="Consultar Objeto Geografia",
    tags=["Geografia"]
)
async def consultar_geografia(geografiamodelo: GeografiaModelo) -> list:
    connection_string = "mongodb+srv://@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    results = []
    client = pymongo.MongoClient(connection_string)
    try:
        db = client["dbElPanal"]
        col = db["Geografia"]
        result = col.find()
        for item in list(result):
            results.append(GeografiaModelo.geografia_helper(item))
    except Exception as ex:
        raise ValueError(ex)
    finally:
        client.close()
    return results # type: ignore

#################################################

#objeto 
@app.post(
    "/consultarorganizacion",
    response_model=list,
    summary="Consultar Organizacion",
    description="Consultar Objeto Organizacion",
    tags=["Organizacion"]
    )
async def consultar_organizacion(organizacionmodelo: OrganizacionModelo) -> list:
    connection_string = "mongodb+srv://@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    results = []
    client = pymongo.MongoClient(connection_string)
    try:
        db = client["dbElPanal"]
        col = db["Organizacion"]
        result = col.find()
        for item in list(result):
            results.append(OrganizacionModelo.organizacion_helper(item))
    except Exception as ex:
        raise ValueError(ex)
    finally:
        client.close()
    return results 

#################################################
#objeto 

@app.post(
    "/consultartransaccional",
    response_model=list,
    summary="Consultar Transaccional",
    description="Consultar Objeto Transaccional",
    tags=["Transaccional"]
    )
async def consultar_transaccion(transaccionalmodelo: TransaccionalModelo) -> list:
    connection_string = "mongodb+srv://@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    results = []
    client = pymongo.MongoClient(connection_string)
    try:
        db = client["dbElPanal"]
        col = db["Transaccional"]
        result = col.find()
        for item in list(result):
            results.append(TransaccionalModelo.transaccional_helper(item))
    except Exception as ex:
        raise ValueError(ex)
    finally:
        client.close()
    return results

#################################################
#objeto 

@app.post(
    "/consultardomicilio",
    response_model=list,
    summary="Consultar Domicilio",
    description="Consultar Objeto Domicilio",
    tags=["Domicilio"]
    )
async def consultar_domicilio(domiciliomodelo: domicilioModelo) -> list:
    connection_string = "mongodb+srv://@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    results = []
    client = pymongo.MongoClient(connection_string)
    try:
        db = client["dbElPanal"]
        col = db["Domicilio"]
        result = col.find()
        for item in list(result):
            results.append(domicilioModelo.domicilio_helper(item))
    except Exception as ex:
        raise ValueError(ex)
    finally:
        client.close()
    return results

#################################################
#objeto 

@app.post(
    "/consultarusuario",
    response_model=list,
    summary="Consultar Usuario",
    description="Consultar Objeto Usuario",
    tags=["Usuario"]
    )
async def consultar_usuario(usuariomodelo: UsuarioModelo) -> list:
    connection_string = "mongodb+srv://@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    results = []
    client = pymongo.MongoClient(connection_string)
    try:
        db = client["dbElPanal"]
        col = db["Usuarios"]
        result = col.find()
        for item in list(result):
            results.append(UsuarioModelo.usuario_helper(item))
    except Exception as ex:
        raise ValueError(ex)
    finally:
        client.close()
    return results