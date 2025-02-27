from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Igor',
        'habilidades': ['Python', 'Django']
    }
]


# Devolve um dev por um ID, também altera e deleta um Dev
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adminastror da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro excluído'})


# Listar os Dev's e permite registrar um novo Dev
@app.route('/dev/', methods=['POST', 'GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
