from flask import Flask, app, render_template
from datetime import date

minha_app = Flask(__name__)

@minha_app.route('/')
def home():
    return render_template('index.html', pagina_selecionada = 'inicio')

@minha_app.route('/sobre')
def sobre():
    idade = calculo_idade(date(1990,3,19))
    return render_template('sobre.html', idade = idade, pagina_selecionada = 'sobre')

def calculo_idade(nascimento):
    today = date.today()
    idade = today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))
    return idade

@minha_app.route('/trabalhos-academicos')
def trabalhos():
    return render_template('trabalhos-academicos.html', pagina_selecionada = 'trabalhos-academicos')   

@minha_app.route('/projetos')
def projetos():
    return render_template('projetos.html', pagina_selecionada = 'projetos')    

if __name__ == '__main__':
    minha_app.run('0.0.0.0')
