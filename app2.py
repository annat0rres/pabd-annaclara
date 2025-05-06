from flask import Flask
import datetime

app2 = Flask(__name__)

@app2.route('/')
def hello():
    return "DATETIME; digite na barra de pesquisa por dia ou hora"

@app2.route('/dia')
def mostrar_data():
    data = datetime.date.today()
    return f"hoje é {data}"

@app2.route('/hora')
def mostrar_hora():
    h = datetime.datetime.now()
    hora = h.strftime("%H:%M:%S")
    return f"agora são {hora}"