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

    def create(self, infoUsuarioAlmacenista, id_Almacenista):
        print("Crear un UsuarioAlmacenista")
        nuevoUsuarioAlmacenista = UsuarioAlmacenista(infoUsuarioAlmacenista)
        nuevoUsuarioAlmacenista.Almacenista=id_Almacenista
        print(self.repositorioUsuarioAlmacenista.save(nuevoUsuarioAlmacenista))
        return self.repositorioUsuarioAlmacenista.save(nuevoUsuarioAlmacenista)

    def show(self, id):
        print("Mostrando un Usuario Almacenista con id ", id)
        elUsuarioAlmacenista = UsuarioAlmacenista(self.repositorioUsuarioAlmacenista.findById(id))
        return elUsuarioAlmacenista.__dict__

    def update(self, id, infoUsuarioAlmacenista, id_Almacenista):
        elUsuarioAlmacenista = UsuarioAlmacenista(self.repositorioUsuarioAlmacenista.findById(id))
        elUsuarioAlmacenista.correo = infoUsuarioAlmacenista["correo"]
        elUsuarioAlmacenista.contraseña = infoUsuarioAlmacenista["contraseña"]
        elAlmacenista = Almacenista(self.repositorioAlmacenista.findById(id_Almacenista))
        elUsuarioAlmacenista.Almacenista = elAlmacenista
        return self.repositorioUsuarioAlmacenista.save(elUsuarioAlmacenista)

    def delete(self, id):
        print("Elimiando UsuarioAlmacenisya con id ", id)
        return self.repositorioUsuarioAlmacenista.delete(id)


