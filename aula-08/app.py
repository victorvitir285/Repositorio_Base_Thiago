from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<center><h1><br><hr>Aula a criação de API<br><h1></center>'

@app.route('/api')
def demo():
    return jsonify(mensagem="esta mensagem vai trasformar a sua vida")

@app.route('/api/<cliente>', methods=['get'])
def nome(cliente):
    return jsonify(mensagem=f'Oi {cliente}')

@app.route('/bemvindo/<idioma>/<nome>', methods=['get'])
def bemvindo(idioma, nome):
    mensagens = {
        'pt':'bom dia',
        'en':'good morning',
        'jp':'おはよう',
        'ar':'صباح الخير',
        'it':'Buongiorno',
        'de':'Guten Morgen'
    }

    mensagens = mensagens.get(idioma)
    return jsonify(msg=f'{mensagens} {nome}')

pedidos = [

     {'id':1, 'cliente':'Thiago','prato':'Churrasco','stutus':'aguardando'},
     {'id':2, 'cliente':'Fabio','prato':'Pizza','stutus':'aguardando'},
]

proximo_id = 3

@app.route('/pedidos', methods=['POST'])
def novospedidos():
    global proximo_id
    novo_pedido = request.json

    novo_pedido_molde = {
        'id':      proximo_id,
        'cliente': novo_pedido['cliente'],
        'prato':   novo_pedido['prato'],
        'status': 'aguardando'
    }

    pedidos.append(novo_pedido_molde)
    proximo_ID += 1

    return jsonify(novo_pedido_molde)

@app.route('/pedidos', methods=['GET'])
def verpedido():
    return jsonify(pedidos)



if __name__ == '__main__':
    app.run(debug=True)