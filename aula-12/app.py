from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conta')
def conta():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    n3 = int(request.args.get('valor3',0))

    conta = n1 + n2+ n3

    return {'Numero1': n1,
            'Numero2': n2,
            'Numero3': n3,
            'Soma dos 3 numeros': conta
            
            }
if __name__ == '__main__':
    app.run(debug=True, port=5001)