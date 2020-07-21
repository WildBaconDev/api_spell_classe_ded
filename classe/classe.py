from spell import spell
import logging
import json

logger = logging.getLogger('Classe')


def classe():
    classes = ""
    for chave in spell.__spellByClass.keys():
        classes += chave + ", "

    logger.info(classes)

    return json.dumps(classes)
