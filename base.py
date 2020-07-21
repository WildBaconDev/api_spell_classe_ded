import os
from flask import Flask
from spell import spell
from classe import classe
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger("Endpoint")

app = Flask(__name__)


@app.route('/')
def home():
    return "Server on"


@app.route('/listaSpell/', methods=['GET'])
def get_lista_spells():
    logger.info("/listaSpell")
    result = spell.spells()
    logger.info("Return - " + result)
    return result


@app.route('/listaSpell/<classe>', methods=['GET'])
def get_lista_spells_por_classe(classe):
    logger.info("/listaSpell/<classe>")
    if classe is None:
        return "..."
    result = spell.spells_por_classe(classe)
    logger.info("Return - " + result)
    return result


@app.route("/listaClasse/", methods=['GET'])
def get_lista_classe():
    logger.info("/listaClasse")
    result = classe.classe()
    logger.info("Return - " + result)
    return result


@app.route("/spell/<spell_name>", methods=['GET'])
def get_spell_especifica(spell_name):
    logger.info("/spell/" + spell_name)
    result = spell.spell_especifica(spell_name)
    logger.info("Return - " + result)
    return result


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
