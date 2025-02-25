#importando o flask e o render_template
from flask import Flask, render_template

#Carregando o flask na variável app
app = Flask(__name__, template_folder='views')

#Criando a primeira rota do site
@app.route('/')
#Criando função no python
def home():
    return render_template('index.html')
# Rota de games {do lado esquerdo é chave do lado direito}
@app.route('/games')
def games(): 
    #Dicionário em python (Objeto em python)
    game = {
          'titulo' : 'CS-GO',
              'ano' : 2012,
    'categoria' :'FPS Online'
        
    }


    categoria = 'FPS Online'
    jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'Quemario', 'Trop', 'aspax', 'maxxdiego']
    jogos = ['Valorant','League of legends', 'Minecraft', 'Gta 5', 'Sonic']
    return render_template('games.html',
                            game=game,
                           jogadores=jogadores,
                           jogos=jogos)

#Iniciando o servidor no localgost, porta 500,, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    