from Modelos.Almacenista import Almacenista
from Modelos.UsuarioAlmacenista import UsuarioAlmacenista
from Repositorio.RepositorioUsuarioAlmacenista import RepositorioUsuarioAlmacenista
from Repositorio.RepositorioAlmacenista import RepositorioAlmacenista


class ControladorUsuarioAlmacenista():

    def __init__(self):
        print("Creando ControladorUsuarioAlmacenista")
        self.repositorioUsuarioAlmacenista = RepositorioUsuarioAlmacenista();
        self.repositorioAlmacenista = RepositorioAlmacenista();

    def index(self):
        print("Listar todos los UsuariosAlmacenista")
        return self.repositorioUsuarioAlmacenista.findAll()

    def create(self, data):
        print("Crear un Inventario")
        nuevoUsuarioAlmacenista = UsuarioAlmacenista(data)
        return self.repositorioUsuarioAlmacenista.save(nuevoUsuarioAlmacenista)

    def show(self, id):
        print("Mostrando un Usuario Almacenista con id ", id)
        elUsuarioAlmacenista = self.repositorioUsuarioAlmacenista.query({"usuario": id})
        # como convertir este dict en una lista de objetos inventarioproducto ?? el append funciona?
        for usuarioalmacenista in elUsuarioAlmacenista:
            idusuario = usuarioalmacenista["almacenista"]
            usuarioalmacenista["almacenista"] = Almacenista(self.repositorioAlmacenista.findById(idusuario)).__dict__
        return elUsuarioAlmacenista

    def update(self, id_usuarioalmacenista, dataUsuarioAlmacenista):
        elUsuarioAlmacenista = UsuarioAlmacenista(self.repositorioUsuarioAlmacenista.findById(id_usuarioalmacenista))
        elUsuarioAlmacenista.usuario = dataUsuarioAlmacenista["usuario"]
        elUsuarioAlmacenista.almacenista = dataUsuarioAlmacenista["almacenista"]
        return self.repositorioUsuarioAlmacenista.save(elUsuarioAlmacenista)

    def delete(self, id):
        print("Elimiando UsuarioAlmacenisya con id ", id)
        return self.repositorioUsuarioAlmacenista.delete(id)


