from flask import render_template, request, redirect, url_for
from models.database import Game, Console, db

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
        
        
    #Rota de estoque (CRUD)
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        #verificar se foi enviado alguma ID
        if id:
            game = Game.query.get(id)
            #deltando o jogo
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))

        # = -> Atribuição 
        # == -> Comparação simples (valor)
        # === -> Compara valor e tipo da variavel
        if request.method == 'POST':
            #Cadastra novo jogo
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'], request.form['plataforma'], request.form['preco'],request.form['quantidade'])
            # newconsole = Console(request.form['nome'], request.form['fabricante'], request.form['preco'],request.form['quantidade'])
            #Envivando para o banco
            db.session.add(newgame) 
            # db.session.add(newconsole)
            #Confirmando as alterações
            db.session.commit()
            return redirect(url_for('estoque'))
            
        #Fazendo um select no banco (pegando todos os jogos da tabela)
        gameestoque = Game.query.all()
       
        return render_template('estoque.html', gamesestoque=gameestoque)    
        
        #flask-sqlalchemy auxilia na criação dos models
        #.findOne() .create() .delete() .update
        #pymysql Permiti conectar a aplicação flask ao banco MYSQL
        #mysqlcliente driver de conexão
    @app.route('/estoqueconsole', methods=['GET', 'POST'])
    @app.route('/estoqueconsole/<int:id>')
    def estoqueconsole(id=None):
        #verificar se foi enviado alguma ID
        if id:
            console = Console.query.get(id)
            #deltando o jogo
            db.session.delete(console)
            db.session.commit()
            return redirect(url_for('estoqueconsole'))
        if request.method == 'POST':
            #Cadastra novo jogo

            newconsole = Console(request.form['nome'], request.form['fabricante'], request.form['preco'], request.form['quantidade'])
            #Envivando para o banco
            db.session.add(newconsole) 
            # db.session.add(newconsole)
            #Confirmando as alterações
            db.session.commit()
            return redirect(url_for('estoqueconsole'))
        consoleestoque = Console.query.all()
        return render_template('estoqueconsole.html', consoleestoque=consoleestoque)   
    #Rota de edição de jogos
    @app.route('/editgame/<int:id>', methods=['GET','POST'])
    def editgame(id):
        #Busca o jogo pelo ID
        game = Game.query.get(id)
        #Editando o jogo com as informações vindas do formulário
        if request.method == 'POST':
            #Coletando as informações do form
            game.titulo = request.form['titulo']
            game.ano = request.form['ano']
            game.categoria = request.form['categoria']
            game.plataforma = request.form['plataforma']
            game.preco = request.form['preco']
            game.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editgame.html', game=game)
    @app.route('/editconsole/<int:id>', methods=['GET','POST'])
    def editconsole(id):
        #Busca o jogo pelo ID
        console = Console.query.get(id)
        #Editando o jogo com as informações vindas do formulário
        if request.method == 'POST':
            #Coletando as informações do form
            console.nome = request.form['nome']
            console.fabricante = request.form['fabricante']

            console.preco = request.form['preco']
            console.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editconsole.html', console=console)
    
    
        