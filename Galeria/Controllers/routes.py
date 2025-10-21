from flask import render_template, request, url_for, flash, redirect
from Models.database import db, Imagem  
import os
import uuid

def init_app(app):

    @app.route('/')
    def home():
        return render_template('home.html')

    #Definindo tipos de arquivos permitidos
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
    
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES

    # UPLOAD DE IMAGENS
    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        # Seleciona os nomes dos arquivos de imagens no banco
        imagens = Imagem.query.all()
        if request.method == 'POST':
            # Captura o arquivo vindo do formulário
            file = request.files['file']
            # Verifica se a extensão do arquivo é permitida
            if not arquivos_permitidos(file.filename):
                flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
                return redirect(request.url)
            # Define um nome aleatório para o arquivo
            filename = str(uuid.uuid4())
            # Gravando o nome do arquivo no banco
            img = Imagem(filename)
            db.session.add(img)
            db.session.commit()
            
            # Salva o arquivo na pasta de uploads
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso!", 'success')
            return redirect(url_for('galeria'))
        return render_template('galeria.html', imagens=imagens)