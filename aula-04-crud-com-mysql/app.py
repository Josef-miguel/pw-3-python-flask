#importando o flask e o render_template
from flask import Flask, render_template
#Importando as rotas que estão nos controllers
from controllers import routex
#importando o PYMySQL
import pymysql
#Importando o model
from models.database import db
#Carregando o flask na variável app
app = Flask(__name__, template_folder='views')
#Definir o nome do banco de dados
DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME 

#Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

#Chamando as rotas
routex.init_app(app)

#Iniciando o servidor no localgost, porta 500,, modo de depuração ativado
if __name__ == '__main__':
    #Conectando ao MySQL e crianco o banco de dados com suas tabelas,
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            # Executar uma query para criar o banco
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O banco de dados está criado!")
        
    except Exception as error:
        print(f"Erro ao criar o banco: {error}")
        
        
    finally:
        connection.close()
        
        
        #Criação das tabelas
        db.init_app(app=app)
        with app.test_request_context():
            db.create_all()
    app.run(host='localhost', port=5000, debug=True)
    