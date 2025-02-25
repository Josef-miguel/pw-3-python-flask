from flask import render_template, request
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'Quemario', 'Trop', 'aspax', 'maxxdiego']
def init_app(app):
        #Criando a primeira rota do site
    @app.route('/')
    #Criando função no python
    def home():
        return render_template('index.html')
    # Rota de games {do lado esquerdo é chave do lado direito}
    @app.route('/games', methods=['GET','POST'])
    def games(): 
        #Dicionário em python (Objeto em python)
        game = {
            'titulo' : 'CS-GO',
                'ano' : 2012,
        'categoria' :'FPS Online'
            
        }


        categoria = 'FPS Online'
        
        #Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            #Verificar se o campo jogador exist
            if request.form.get('jogador'):
                #O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            
            
            
            
        jogos = ['Valorant','League of legends', 'Minecraft', 'Gta 5', 'Sonic']
        return render_template('games.html',
                                game=game,
                            jogadores=jogadores,
                            jogos=jogos)