from flask import Flask
#Importa o flask Restful
from flask_restful import Api
app = Flask(__name__)
#Carregaando o flask Restful ma variavel api
api = Api(app)

#Adicionando os recursos da API
from .resources import game_resources


