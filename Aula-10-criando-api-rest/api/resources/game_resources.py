#Importando a classa do resource do flask restful
from flask_restful import Resource
#Importando a classe API
from api import api
#Logo abaixo irá as repostas da API
class GameList(Resource):
    def get(self):
        return "Bem-Vindo a API The Games!!"
#Criando o endpoint principal da API
api.add_resource(GameList, '/games')