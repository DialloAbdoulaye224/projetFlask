from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("accueil.html")

@app.route('/page')
def page():
    return render_template("page.html")

@app.route('/search')
def search():
    query = request.args.get('query')
    # Ajoutez ici le code pour traiter la requête de recherche
    return f"Résultats de recherche pour : {query}"

if __name__ == '__main__':
    app.run(debug=True)
