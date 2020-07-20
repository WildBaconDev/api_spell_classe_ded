import os
from flask import Flask
from spell import spell
from classe import classe

app = Flask(__name__)


@app.route('/')
def home():
    return "Servidor funcionando"


@app.route('/listaSpell/', methods=['GET'])
def get_lista_spells():
    return spell.spells()


@app.route('/listaSpell/<classe>', methods=['GET'])
def get_lista_spells_por_classe(classe):
    if classe is None:
        return "..."

    return spell.spells_por_classe(classe)


@app.route("/listaClasse/", methods=['GET'])
def get_lista_classe():
    return classe.classe()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)