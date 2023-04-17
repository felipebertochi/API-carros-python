from flask import Flask, jsonify, request
apiproj = Flask(__name__)

carros = [
    {
        'id': 1,
        'título': 'Bugatti Bolide',
        'Preço': '24 milhões'
    },
    {
        'id': 2, 
        'título': 'Pagani Huarya Imola',
        'Preço': '27 milhões'
    },
    {
        'id': 3,
        'título': 'Bugatti Divo',
        'Preço': '29,5 milhões'
    }
]

@apiproj.route('/carros')
def consultar_carros():
    return jsonify(carros)

@apiproj.route('/carros/<int:id>', methods = ['GET'])
def consultar_carros_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)

@apiproj.route('/carros/<int:id>', methods = ['PUT'])
def editar_carro_id(id):
    carro_editado = request.get_json()
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_editado)
            return jsonify(carros[indice])

@apiproj.route('/carros', methods = ['POST'])
def add_carro():
    carro_novo = request.get_json()
    carros.append(carro_novo)
    return jsonify(carros)

@apiproj.route('/carros/<int:id>', methods = ['DELETE'])
def excluir_carro_id(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
    return jsonify(carros)

apiproj.run(port=5000,host='localhost',debug=True)  