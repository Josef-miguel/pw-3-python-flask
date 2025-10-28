#Importando o flask
from api import app

#rodando a API
if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)