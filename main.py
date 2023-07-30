from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json

import certifi
from waitress import serve
from Repositorio.InterfaceRepositorio import InterfaceRepositorio
from Controladores.ControladorAlmacenista import ControladorAlmacenista
from Controladores.ControladorProducto import ControladorProducto
from Controladores.ControladorProveedor import ControladorProveedor
from Controladores.ControladorInventario import ControladorInventario
from Controladores.ControladorInventarioProducto import ControladorInventarioProducto
from Controladores.ControladorUsuarioAlmacenista import ControladorUsuarioAlmacenista

app = Flask(__name__)
cors = CORS(app)

"""
Implementacion de los controladores
"""
miControladorProveedor = ControladorProveedor()
miControladorAlmacenista = ControladorAlmacenista()
miControladorProducto = ControladorProducto()
miControladorInventario = ControladorInventario()
miControladorInventarioProducto = ControladorInventarioProducto()
miControladorUsuarioAlmacenista = ControladorUsuarioAlmacenista()
miInterfaceRepositorio = InterfaceRepositorio()

"""
Servicios que el servidor ofrecerá; se definen las rutas
y tipos de peticiones a las cuales el servidor responderá CRUD.
"""


##########################SERVICIOS PROVEEDOR##############################

@app.route("/proveedor", methods=['GET'])
def getProveedores():
    json = miControladorProveedor.index()
    return jsonify(json)


@app.route("/proveedor", methods=['POST'])
def crearProveedor():
    data = request.get_json()
    json = miControladorProveedor.create(data)
    return jsonify(json)


@app.route("/proveedor/<string:id>", methods=['GET'])
def getProveedor(id):
    json = miControladorProveedor.show(id)
    return jsonify(json)


@app.route("/proveedor/<string:id>", methods=['PUT'])
def modificarProveedor(id):
    data = request.get_json()
    json = miControladorProveedor.update(id, data)
    return jsonify(json)


@app.route("/proveedor/<string:id>", methods=['DELETE'])
def eliminarProveedor(id):
    json = miControladorProveedor.delete(id)
    return jsonify(json)


######################################SERVICIOS ALMACENISTA###################################

@app.route("/almacenista", methods=['GET'])
def getAlmacenistas():
    json = miControladorAlmacenista.index()
    return jsonify(json)


@app.route("/almacenista", methods=['POST'])
def crearAlmacenista():
    data = request.get_json()
    json = miControladorAlmacenista.create(data)
    return jsonify(json)


@app.route("/almacenista/<string:id>", methods=['GET'])
def getAlmacenista(id):
    json = miControladorAlmacenista.show(id)
    return jsonify(json)


@app.route("/almacenista/<string:id>", methods=['PUT'])
def modificarAlmacenista(id):
    data = request.get_json()
    json = miControladorAlmacenista.update(id, data)
    return jsonify(json)


@app.route("/almacenista/<string:id>", methods=['DELETE'])
def eliminarAlmacenista(id):
    json = miControladorAlmacenista.delete(id)
    return jsonify(json)


""""@app.route("/almacenista/<string:id>/producto/<string:id_producto>", methods=['PUT'])
def asignarProductoa(id,id_producto):
    json=miControladorAlmacenista.asignarProducto(id, id_producto)
    return  jsonify(json)"""


######################################SERVICIOS PRODUCTO###################################

@app.route("/producto", methods=['GET'])
def getProductos():
    json = miControladorProducto.index()
    return jsonify(json)


@app.route("/producto", methods=['POST'])
def crearProducto():
    data = request.get_json()
    json = miControladorProducto.create(data)
    return jsonify(json)


@app.route("/producto/<string:id>", methods=['GET'])
def getProducto(id):
    json = miControladorProducto.show(id)
    return jsonify(json)


@app.route("/producto/<string:id>", methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json = miControladorProducto.update(id, data)
    return jsonify(json)


@app.route("/producto/<string:id>", methods=['DELETE'])
def eliminarProducto(id):
    json = miControladorProducto.delete(id)
    return jsonify(json)


######################################SERVICIOS INVENTARIO###################################

@app.route("/inventario", methods=['GET'])
def getInventarios():
    json = miControladorInventario.index()
    return jsonify(json)


@app.route("/inventario/<string:id>", methods=['GET'])
def getInventario(id):
    json = miControladorInventario.show(id)
    return jsonify(json)


@app.route("/inventario", methods=['POST'])
def crearInventario():
    data = request.get_json()
    json = miControladorInventario.create(data)
    return jsonify(json)


@app.route("/inventario/<string:id_inventario>", methods=['PUT'])
def modificarInventario(id_inventario):
    data = request.get_json()
    json = miControladorInventario.update(id_inventario, data)
    return jsonify(json)


@app.route("/inventario/<string:id_inventario>", methods=['DELETE'])
def eliminarInventario(id_inventario):
    json = miControladorInventario.delete(id_inventario)
    return jsonify(json)

######################################SERVICIOS INVENTARIO PRODUCTOS###################################

@app.route("/inventarioproducto", methods=['GET'])
def getInventariosProductos():
    json = miControladorInventarioProducto.index()
    return jsonify(json)


@app.route("/inventarioproducto/<string:id>", methods=['GET'])
def getInventarioProductos(id):
    json = miControladorInventarioProducto.show(id)
    return jsonify(json)


@app.route("/inventarioproducto", methods=['POST'])
def crearInventarioProducto():
    data = request.get_json()
    json = miControladorInventarioProducto.create(data)
    return jsonify(json)


@app.route("/inventarioproducto/<string:id_inventarioproducto>", methods=['PUT'])
def modificarInventarioProducto(id_inventarioproducto,):
    data = request.get_json()
    json = miControladorInventarioProducto.update(id_inventarioproducto, data)
    return jsonify(json)


@app.route("/inventarioproducto/<string:id_inventarioproducto>", methods=['DELETE'])
def eliminarInventarioProducto(id_inventarioproducto):
    json = miControladorInventarioProducto.delete(id_inventarioproducto)
    return jsonify(json)


######################################SERVICIOS USUARIOS ALMACENISTAS###################################

@app.route("/usuarioalmacenista", methods=['GET'])
def getUsuarioAlmacenista():
    json = miControladorUsuarioAlmacenista.index()
    return jsonify(json)


@app.route("/usuarioalmacenista/<string:id>", methods=['GET'])
def getUsuarioAlmacenistaid(id):
    json = miControladorUsuarioAlmacenista.show(id)
    return jsonify(json)


@app.route("/usuarioalmacenista", methods=['POST'])
def crearUsuarioAlmacenista():
    data = request.get_json()
    json = miControladorUsuarioAlmacenista.create(data)
    return jsonify(json)


@app.route("/usuarioalmacenista/<string:id_usuarioalmacenista>", methods=['PUT'])
def modificarUsuarioAlmacenista(id_usuarioalmacenista,):
    data = request.get_json()
    json = miControladorUsuarioAlmacenista.update(id_usuarioalmacenista, data)
    return jsonify(json)


@app.route("/usuarioalmacenista/<string:id_usuarioalmacenista>", methods=['DELETE'])
def eliminarUsuarioAlmacenista(id_usuarioalmacenista):
    json = miControladorUsuarioAlmacenista.delete(id_usuarioalmacenista)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
    Se crea la instancia del servidor con la url del backend y puerto especificado 
    en el archivo de configuración.
    """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
