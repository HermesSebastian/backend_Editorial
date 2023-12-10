from Modelos.Publicacion import Publicacion
from Modelos.TipoPublicacion import TipoPublicacion

from Repositorio.RepositorioTipoPublicacion import RepositorioTipoPublicacion
from Repositorio.RepositorioPublicacion import RepositorioPublicacion


class ControladoresPublicacion():

        def __init__(self):
            self.RepositorioPublicacion = RepositorioPublicacion()
            self.RepositorioTipoPublicacion = RepositorioTipoPublicacion()
            print("Creando Controlador Publicacion")

        def index(self):
            return self.RepositorioPublicacion.findAll()

        def create(self, infoPublicacion):
            nuevapublicacion = Publicacion(infoPublicacion)
            return self.RepositorioPublicacion.save(nuevapublicacion)


        def show(self, id):
            elPublicacion = Publicacion(self.RepositorioPublicacion.findById(id))
            return elPublicacion.__dict__

        def update(self, id, infoPublicacion):
            PublicacionActual = Publicacion(self.RepositorioPublicacion.findById(id))
            PublicacionActual.titulo = infoPublicacion["titulo"]
            PublicacionActual.isbn = infoPublicacion["isbn"]
            PublicacionActual.fecha = infoPublicacion["fecha"]
            PublicacionActual.programa=infoPublicacion["programa"]

            return self.RepositorioPublicacion.save(PublicacionActual)

        def delete(self, id):
            return self.RepositorioPublicacion.delete(id)

        """
        Relación Publicacion y Tipo de publicacion
        """

        def asignarTipoPublicacion(self, id, id_tipopublicacion):
            PublicacionActual = Publicacion(self.RepositorioPublicacion.findById(id))
            TipoPublicacionActual = TipoPublicacion(self.RepositorioPublicacion.findById(id_tipopublicacion))
            PublicacionActual.tipopublicacion = TipoPublicacionActual
            return self.RepositorioPublicacion.save(PublicacionActual)

