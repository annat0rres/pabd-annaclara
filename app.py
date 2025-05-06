from flask import Flask
app = Flask(__name__)

@app.route('/')
def bemvindo():
    return 'olá, seja bem vindo! na barra de pesquisa digite os números que quer somar entre barras (/)'

@app.route('/magic/<n1>/<n2>')
def resultado(n1, n2):
    soma = int(n1) + int(n2)
    return f'a soma entre esses dois números é: {str(soma)}'

# @app.route('/magic/<palavra>')
# def mostrar(palavra):
#     return palavra