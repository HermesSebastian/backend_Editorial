from Modelos.Autor import Autor
from Repositorio.RepositorioAutor import RepositorioAutor

class ControladoresAutor():
    def __init__(self):
        self.RepositorioAutor = RepositorioAutor()
        print("Creando Controlador Autor")

    def index(self):
        print("Listar todos los Autores")
        return self.RepositorioAutor.findAll()

    def create(self, infoAutor, id_Autor):
        nuevoAutor = Autor(infoAutor)
        return self.RepositorioAutor.save(nuevoAutor)

    def show(self, id):
        elAutor = Autor(self.RepositorioAutor.findById(id))
        return elAutor.__dict__

    def update(self, id, infoAutor):
        elAutor = Autor(self.RepositorioAutor.findById(id))
        elAutor.nombres = infoAutor["nombres"]
        elAutor.apellidos = infoAutor["apellidos"]
        elAutor.direccion = infoAutor["direccion"]
        elAutor.nivelacademico=infoAutor["nivelacademico"]
        elAutor.correoelectronico=infoAutor["correoelectronico"]
        return self.RepositorioAutor.save(elAutor)

    def delete(self, id):
        print("Eliminando Autor con id ", id)
        resultado = self.RepositorioAutor.delete(id)
        print(f"Autor eliminado con id {id}: {resultado}")
        return resultado
