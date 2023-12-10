from Modelos.TipoPublicacion import TipoPublicacion

from Repositorio.RepositorioTipoPublicacion import RepositorioTipoPublicacion


class ControladoresTipoPublicacion():

    def __init__(self):
        self.RepositorioTipoPublicacion = RepositorioTipoPublicacion()
        print("Creando Controlador  TipoPublicacion")

    def index(self):
        print("Listar todos las Tipo de Publicacion")
        return self.RepositorioTipoPublicacion.findAll()

    def create(self, infoTipoPublicacion, id_TipoPublicacion):
        nuevoTipoEditorial= TipoPublicacion(infoTipoPublicacion)
        return self.RepositorioTipoPublicacion.save(nuevoTipoEditorial)

    def show(self, id):
        elTipoPublicacion = TipoPublicacion(self.RepositorioTipoPublicacion.findById(id))
        return elTipoPublicacion.__dict__

    def update(self, id, infoTipoPublicacion):
        elTipoPublicacion = TipoPublicacion(self.RepositorioTipoPublicacion.findById(id))
        elTipoPublicacion.formato = infoTipoPublicacion["formato"]
        elTipoPublicacion.genero = infoTipoPublicacion["genero"]
        return self.RepositorioTipoPublicacion.save(elTipoPublicacion)

    def delete(self, id):
        print("Eliminando un tipo de publicacion con id ", id)
        resultado = self.RepositorioTipoPublicacion.delete(id)
        print(f"Editorial eliminada con id {id}: {resultado}")
        return resultado




