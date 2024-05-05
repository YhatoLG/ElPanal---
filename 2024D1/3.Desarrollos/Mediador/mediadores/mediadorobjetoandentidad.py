from fastapi import FastAPI 
import pymongo
import mysql.connector
#OBJETO
from Objetos.geografia import GeografiaModelo
from Objetos.organizacion import OrganizacionModelo
from Objetos.transaccional import TransaccionalModelo
from Objetos.domicilio import domicilioModelo
from Objetos.usuario import UsuarioModelo
#ENTIDAD
from Entidades.pais import PaisModelo
from Entidades.departamento import DepartamentoModelo
from Entidades.ciudad import CiudadModelo
from Entidades.detalle_factura import DetalleFacturaModelo
from Entidades.estadofactura import EstadoFacturaModelo
from Entidades.factura import FacturaModelo
from Entidades.empleado import EmpleadoModelo
from Entidades.empresa import EmpresaModelo
from Entidades.sede import SedeModelo
from Entidades.domicilio import DomicilioModelo
from Entidades.tipo_de_domicilio import TipoDeDomicilioModelo
from Entidades.tipo_de_documento import TipoDeDocumentoModelo
from Entidades.usuarios import UsuarioModelo




app: FastAPI = FastAPI(
    title="Mediador de Objeto and Entidad",
    description="Mediador de Objeto and Entidad",
)


#################################################

#objeto 
@app.post( 
    "/consultarJsonGeografia",
    response_model=list,
    summary="Consultar Geografia",
    description="Consultar Objeto Geografia",
    tags=["Geografia"]
)
async def consultar_geografia(geografiamodelo: GeografiaModelo) -> list:
    connection_string = "@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
    "/consultarJsonOrganizacion",
    response_model=list,
    summary="Consultar Organizacion",
    description="Consultar Objeto Organizacion",
    tags=["Organizacion"]
    )
async def consultar_organizacion(organizacionmodelo: OrganizacionModelo) -> list:
    connection_string = "@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
    "/consultarJsonTransaccional",
    response_model=list,
    summary="Consultar Transaccional",
    description="Consultar Objeto Transaccional",
    tags=["Transaccional"]
    )
async def consultar_transaccion(transaccionalmodelo: TransaccionalModelo) -> list:
    connection_string = "@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
    "/consultarJsonDomicilio",
    response_model=list,
    summary="Consultar Domicilio",
    description="Consultar Objeto Domicilio",
    tags=["Domicilio"]
    )
async def consultar_domicilio(domiciliomodelo: domicilioModelo) -> list:
    connection_string = "@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
    "/consultarJsonUsuario",
    response_model=list,
    summary="Consultar Usuario",
    description="Consultar Objeto Usuario",
    tags=["Usuario"]
    )
async def consultar_usuario(usuariomodelo: UsuarioModelo) -> list:
    connection_string = "@cluster0.nbfp451.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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


#################################################
#ENTIDAD

@app.post(
    "/consultarpais",
    response_model=list,
    summary="Consultar Pais",
    description="Consultar Entidad Pais",
    tags=["Geografia"]
)
async def consultar_pais(paismodelo: PaisModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaPais")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultaDepartamento",
    response_model=list,
    summary="Consultar Departamento",
    description="Consultar Entidad Departamento",
    tags=["Geografia"]
)
async def consultar_departamento(departamentomodelo: DepartamentoModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaDepartamento")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultarciudad",
    response_model=list,
    summary="Consultar Ciudad",
    description="Consultar Entidad Ciudad",
    tags=["Geografia"]
)
async def consultar_ciudad(ciudadmodelo: CiudadModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaCiudad")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultardetallefactura",
    response_model=list,
    summary="Consultar Detalle Factura",
    description="Consultar Entidad Detalle Factura",
    tags=["Transaccional"]
)
async def consultar_detalle_factura(detallefacturamodelo: DetalleFacturaModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaDetalleFactura")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultaestadofactura",
    response_model=list,
    summary="Consultar Estado Factura",
    description="Consultar Entidad Estado Factura",
    tags=["Transaccional"]
)
async def consultar_estado_factura(estadofacturamodelo: EstadoFacturaModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaEstadoFactura")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultarfactura",
    response_model=list,
    summary="Consultar Factura",
    description="Consultar Entidad Factura",
    tags=["Transaccional"]
)
async def consultar_factura(facturamodelo: FacturaModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaFactura")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultarempleado",
    response_model=list,
    summary="Consultar Empleado",
    description="Consultar Entidad Empleado",
    tags=["Organizacion"]
)
async def consultar_empleado(empleadoModelo: EmpleadoModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaEmpleado")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultarempresa",
    response_model=list,
    summary="Consultar Empresa",
    description="Consultar Entidad Empresa",
    tags=["Organizacion"]
)
async def consultar_empresa(empresamodelo: EmpresaModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaEmpresa")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultarsede",
    response_model=list,
    summary="Consultar Sede",
    description="Consultar Entidad Sede",
    tags=["Organizacion"]
)
async def consultar_sede(sedemodelo: SedeModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaSede")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultardomicilio",
    response_model=list,
    summary="Consultar Domicilio",
    description="Consultar Entidad Domicilio",
    tags=["Domicilio"]
)
async def consultar_domicilio(domiciliomodelo: DomicilioModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaDomicilio")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultartipodedomicilio",
    response_model=list,
    summary="Consultar Tipo de Domicilio",
    description="Consultar Entidad Tipo de Domicilio",
    tags=["Domicilio"]
)
async def consultar_tipo_de_domicilio(tipodedomiciliomodelo: TipoDeDomicilioModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaTipoDeDomicilio")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultartipodedocumento",
    response_model=list,
    summary="Consultar Tipo de Documento",
    description="Consultar Entidad Tipo de Documento",
    tags=["Usuario"]
)
async def consultar_tipo_de_documento(tipodedocumentomodelo: TipoDeDocumentoModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaTipoDeDocumento")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results

#################################################
#ENTIDAD

@app.post(
    "/consultarusuario",
    response_model=list,
    summary="Consultar Usuario",
    description="Consultar Entidad Usuario",
    tags=["Usuario"]
)
async def consultar_usuario(usuariomodelo: UsuarioModelo) -> list:
    results = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="elpanal"
    )
    try:
        cursor = db.cursor()
        cursor.callproc("ConsultaUsuario")
        for item in list(cursor.stored_results()):
            results = item.fetchall()
        db.commit()
        cursor.close()
    except Exception as ex:
        raise ValueError(ex)
    finally:
        db.disconnect()
    return results
