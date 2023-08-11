from Modelos import InventarioProducto
from Modelos.Almacenista import Almacenista
from Modelos.Producto import Producto
from Modelos.Inventario import Inventario
from Repositorio.RepositorioProducto import RepositorioProducto
from Repositorio.RepositorioAlmacenista import RepositorioAlmacenista
from Repositorio.RepositorioInventario import RepositorioInventario

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInventario():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        print("Creando ControladorInventario")
        self.repositorioInventario = RepositorioInventario();
        self.repositorioAlmacenista = RepositorioAlmacenista();
        self.repositorioProducto = RepositorioProducto();

    def index(self):
        print("Listar todos los Inventario")
        inventarios= self.repositorioInventario.findAll()
        for inventario in inventarios:

            idalmacenista=inventario["almacenista"]
            busqueda=self.repositorioAlmacenista.findById(idalmacenista)["nombre"]
            inventario["almacenista"]=busqueda

        return inventarios

    """Asignacion de almacenista y producto a inventario"""

    def create(self, infoInventario):
        print("Crear un Inventario")
        nuevoInventario = Inventario(infoInventario)
        nuevoInventario.almacenista=infoInventario["almacenista"]
        return self.repositorioInventario.save(nuevoInventario)

    def show(self, id):
        print("Mostrando un Inventario con id ", id)
        elInventario = Inventario(self.repositorioInventario.findById(id))

        return elInventario.__dict__

    def update(self, id, infoInventario):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        elInventario.fecha = infoInventario["fecha"]
        elInventario.almacenista = infoInventario["almacenista"]
        elInventario.nombreinventario = infoInventario["nombreinventario"]
        print(elInventario)
        return self.repositorioInventario.save(elInventario)

    def delete(self, id):
        print("Elimiando Inventario con id ", id)
        return self.repositorioInventario.delete(id)


