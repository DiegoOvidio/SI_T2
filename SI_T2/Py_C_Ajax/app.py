from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conjunto de dados de filmes
filmes = [
    {"nome": "Mad Max", "genero": "Ação"},
    {"nome": "Mad Max 2", "genero": " Ação"},
    {"nome": "Homen de Ferro", "genero": "Ação"},
    {"nome": "Toy Story", "genero": "Comédia"},
    {"nome": "Sonic", "genero": "Comédia"},
    {"nome": "Invocação do Mal", "genero": "Terror"},
    {"nome": "Seesaw", "genero": "Terror"},
    {"nome": "O Rei Leão", "genero": "Animação"},
    {"nome": "Kung fu panda", "genero": "Animação"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recomendar', methods=['POST'])
def recomendar():
    # Obtém o gênero preferido do formulário
    genero_preferido = request.form['genero'].capitalize()

    # Filtra os filmes com o gênero escolhido
    sugestoes = [f['nome'] for f in filmes if f['genero'] == genero_preferido]

    # Retorna a sugestão em formato JSON
    if sugestoes:
        return jsonify(sugestoes=sugestoes)
    else:
        return jsonify(sugestoes=[])

if __name__ == '__main__':
    app.run(debug=True)
