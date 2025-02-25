#importando o flask e o render_template
from flask import Flask, render_template
#Importando as rotas que estão nos controllers
from controllers import routex

#Carregando o flask na variável app
app = Flask(__name__, template_folder='views')
#Chamando as rotas
routex.init_app(app)

#Iniciando o servidor no localgost, porta 500,, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    