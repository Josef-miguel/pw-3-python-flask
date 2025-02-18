#importando o flask
from flask import Flask

#Carregando o flask na variável app
app = Flask(__name__)

#Criando a primeira rota do site
@app.route('/')
#Criando função no python
def home():
    return '<h1> Bem-Vindo ao meu primeiro site em Flask! </h1>'
#Iniciando o servidor no localgost, porta 500,, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    