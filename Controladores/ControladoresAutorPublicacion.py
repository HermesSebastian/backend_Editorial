from Modelos.AutorPublicacion import AutorPublicacion
from Modelos.Autor import Autor
from Modelos.Publicacion import Publicacion

from Repositorio.RepositorioAutorPublicacion import RepositorioAutorPublicacion
from Repositorio.RepositorioAutor import RepositorioAutor
from Repositorio.RepositorioPublicacion import RepositorioPublicacion
class ControladoresAutorPublicacion():

    def __init__(self):
        self.repositorioAutor = RepositorioAutor()
        self.repositorioPublicacion =RepositorioPublicacion()
        self.repositorioAutorPublicacion = RepositorioAutorPublicacion()

        print("Creando Controlador AutorPublicacion")

    def index(self):
        print("Listar todos los AutorPublicacion")
        return self.repositorioAutorPublicacion.findAll()

    def create(self, infoAutorPublicacion, id_autor, id_publicacion):
        nuevoAutorpublicacion = AutorPublicacion(infoAutorPublicacion)
        elAutor = (self.repositorioAutor.findById(id_autor))
        laPublicacion = Publicacion(self.repositorioPublicacion.findById(id_publicacion))
        nuevoAutorpublicacion.Autor = elAutor
        nuevoAutorpublicacion.Publicacion = laPublicacion
        return self.repositorioAutorPublicacion.save(nuevoAutorpublicacion)

    def show(self, id):
        elAutorLibro = AutorPublicacion(self.repositorioAutorPublicacion.findById(id))
        return elAutorLibro.__dict__

    def update(self, id, infoAutorPublicacion, id_autor, id_publicacion):
        elAutorPublicacion = AutorPublicacion(self.repositorioAutorPublicacion.findById(id))
        elAutorPublicacion.volumen = infoAutorPublicacion["volumen"]
        elAutorPublicacion.descripcion = infoAutorPublicacion["descripcion"]
        elAutorPublicacion.numeropaginas =infoAutorPublicacion["numeropaginas"]
        elAutor = Autor(self.repositorioAutor.findById(id_autor))
        laPublicacion= Publicacion(self.repositorioPublicacion.findById(id_publicacion))
        elAutorPublicacion.Autor = elAutor
        elAutorPublicacion.Publicacion = laPublicacion
        return self.repositorioAutorPublicacion.save(elAutorPublicacion)

    def delete(self, id):
        return self.repositorioAutorPublicacion.delete(id)
