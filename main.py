from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
from Controladores.ControladoresAutor import ControladoresAutor
from Controladores.ControladoresAutorPublicacion import ControladoresAutorPublicacion
from Controladores.ControladoresTipoPublicacion import ControladoresTipoPublicacion
from Controladores.ControladoresPublicacion import ControladoresPublicacion

import json

app = Flask(__name__)
miControladoresAutor = ControladoresAutor()
miControladoresAutorPublicacion = ControladoresAutorPublicacion()
miControladoresTipoPublicacion = ControladoresTipoPublicacion()
miControladoresPublicacion = ControladoresPublicacion()
cors = CORS(app)


######################### Autor ###################################


@app.route("/autor", methods=['GET'])
def getAutorById():
    json = miControladoresAutor.index()
    return jsonify(json)


@app.route("/autor", methods=['POST'])
def crearAutor():
    data = request.get_json()
    json = miControladoresAutor.create(data, 'some_id')
    return jsonify(json)


@app.route("/autor/<string:id>", methods=['GET'])
def getAutor(id):
    json = miControladoresAutor.show(id)
    return jsonify(json)


@app.route("/autor/<string:id>", methods=['PUT'])
def modificarAutor(id):
    data = request.get_json()
    json = miControladoresAutor.update(id, data)
    return jsonify(json)


@app.route("/autor/<string:id>", methods=['DELETE'])
def eliminarAutor(id):
    json = miControladoresAutor.delete(id)
    return jsonify(json)


################### AUTOR DE UNA PUBLICACION #################################################


@app.route("/autorpublicacion", methods=['GET'])
def getAutorPublicacionById():
    json = miControladoresAutorPublicacion.index()
    print("Mensaje: ", json)
    return jsonify(json)


@app.route("/autorpublicacion/<string:id>", methods=['GET'])
def getAutorPublicacion(id):
    json = miControladoresAutorPublicacion.show(id)
    return jsonify(json)


@app.route("/autorpublicacion/autor/<string:id_autor>/publicacion/<string:id_publicacion>", methods=['POST'])
def crearAutorPublicacion(id_autor, id_publicacion):
    data = request.get_json()
    json = miControladoresAutorPublicacion.create(data, id_autor, id_publicacion)
    return jsonify(json)


@app.route("/autorpublicacion/<string:id_autorpublicacion>/autor/<string:id_autor>/publicacion/<string:id_publicacion>",
           methods=['PUT'])
def modificarAutorPublicacion(id_autorpublicacion, id_autor, id_publicacion):
    data = request.get_json()
    json = miControladoresAutorPublicacion.update(id_autorpublicacion, data, id_autor, id_publicacion)
    return jsonify(json)


@app.route("/autorpublicacion/<string:id>", methods=['DELETE'])
def eliminarAutorPublicacion(id):
    json = miControladoresAutorPublicacion.delete(id)
    return jsonify(json)


###########################tipo publicacion########################


@app.route("/tipopublicacion", methods=['GET'])
def getTipoPublicacionById():
    json = miControladoresTipoPublicacion.index()
    return jsonify(json)


@app.route("/tipopublicacion", methods=['POST'])
def crearTipoPublicacion():
    data = request.get_json()
    json = miControladoresTipoPublicacion.create(data, 'some_id')
    return jsonify(json)


@app.route("/tipopublicacion/<string:id>", methods=['GET'])
def getTipoPublicacion(id):
    json = miControladoresTipoPublicacion.show(id)
    return jsonify(json)


@app.route("/tipopublicacion/<string:id>", methods=['PUT'])
def modificarTipoPublicacion(id):
    data = request.get_json()
    json = miControladoresTipoPublicacion.update(id, data)
    return jsonify(json)


@app.route("/tipopublicacion/<string:id>", methods=['DELETE'])
def eliminarTipoPublicacion(id):
    json = miControladoresTipoPublicacion.delete(id)
    return jsonify(json)


#############################publicacion#######################

@app.route("/publicacion", methods=['GET'])
def getPublicacionById():
    json = miControladoresPublicacion.index()
    return jsonify(json)


@app.route("/publicacion/<string:id>", methods=['GET'])
def getPublicacion(id):
    json = miControladoresPublicacion.show(id)
    return jsonify(json)


@app.route("/publicacion", methods=['POST'])
def crearPublicacion():
    data = request.get_json()
    json = miControladoresPublicacion.create(data)
    return jsonify(json)


@app.route("/publicacion/<string:id>", methods=['PUT'])
def modificarPublicacion(id):
    data = request.get_json()
    json = miControladoresPublicacion.update(id, data)
    return jsonify(json)


@app.route("/publicacion/<string:id>", methods=['DELETE'])
def eliminarPublicacion(id):
    json = miControladoresPublicacion.delete(id)
    return jsonify(json)


@app.route("/publicacion/<string:id>/tipopublicacion/<string:id_tipopublicacion>", methods=['PUT'])
def asignarPublicacionATipoPublicacion(id, id_tipopublicacion):
    json = miControladoresPublicacion.asignarTipoPublicacion(id, id_tipopublicacion)
    return jsonify(json)


#########################################################


@app.route("/", methods=['GET'])
def test():
    json_data = {"message": "Server running ..."}
    return jsonify(json_data)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running: " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
