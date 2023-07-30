from Modelos.Producto import Producto
from Modelos.InventarioProducto import InventarioProducto
from Repositorio.RepositorioInventarioProducto import RepositorioInventarioProducto
from Repositorio.RepositorioProducto import RepositorioProducto


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInventarioProducto():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        print("Creando ControladorInventario-Producto")
        self.repositorioInventarioProducto = RepositorioInventarioProducto();
        self.repositorioProducto = RepositorioProducto();

    def index(self):
        print("Listar todos los Inventario")
        return self.repositorioInventarioProducto.findAll()

    def create(self, data):
        print("Crear un Inventario")
        nuevoInventarioProducto = InventarioProducto(data)
        #nuevoInventarioProducto.inventario = data["inventario"]
        #nuevoInventarioProducto.producto = data["producto"]
        return self.repositorioInventarioProducto.save(nuevoInventarioProducto)

    #{
    #    "_id": "64c535a2fc1d152c2b417792",
    #    "inventario": "64c534fdfc1d152c2b41778f",
    #    "producto": "64be7e83ef2a10e082aa8a02"
    #},

    def show(self, id):
        print("Mostrando un Inventario Producto con id ", id)
        elInventarioProducto = self.repositorioInventarioProducto.query({"inventario": id})
        #como convertir este dict en una lista de objetos inventarioproducto ?? el append funciona?
        for inventarioproducto in elInventarioProducto:
            idproducto=inventarioproducto["producto"]
            inventarioproducto["producto"]=Producto(self.repositorioProducto.findById(idproducto)).__dict__

        return elInventarioProducto

    def update(self, id_inventarioproducto,data):
        elInventarioProducto = InventarioProducto(self.repositorioInventarioProducto.findById(id_inventarioproducto))
        elInventarioProducto.inventario = data["inventario"]
        elInventarioProducto.producto = data["producto"]
        return self.repositorioInventarioProducto.save(elInventarioProducto)

    def delete(self, id_inventarioproducto):
        print("Elimiando Inventario producto con id ", id_inventarioproducto)
        return self.repositorioInventarioProducto.delete(id_inventarioproducto)


