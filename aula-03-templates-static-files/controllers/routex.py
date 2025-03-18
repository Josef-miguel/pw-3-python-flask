from flask import render_template, request, redirect, url_for
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'Quemario', 'Trop', 'aspax', 'maxxdiego']

 #Dicionário em python (Objeto em python)
        #Array de objetos [{},{},{}]
gamelist = [{
           'titulo' : 'CS-GO',
                'ano' : 2012,
        'categoria' :'FPS Online'
            
        }]
consolelist = [{
    'nome' : '',
    'fabricante' : '',
    'ano' : '',
    'preco': ''
}]
def init_app(app):
        #Criando a primeira rota do site
    @app.route('/')
    #Criando função no python
    def home():
        return render_template('index.html')
    # Rota de games {do lado esquerdo é chave do lado direito os valores}
    @app.route('/games', methods=['GET','POST'])
    def games(): 
      
        game = gamelist[0]
  


        
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
    #Rota de cadastro de jogos (EM dicionario)
    @app.route('/cadgames', methods=['GET','POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'titulo': request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)
        
        #Rota de cadastro de consoles
    @app.route('/consoles', methods=['GET','POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('fabricante') and request.form.get('ano') and request.form.get('preco'):
                consolelist.append({'nome': request.form.get('nome'), 'fabricante' : request.form.get('fabricante'), 'ano': request.form.get('ano'), 'preco' : request.form.get('preco')})
            return redirect(url_for('consoles'))
        return render_template('consoles.html',
                               consolelist=consolelist)