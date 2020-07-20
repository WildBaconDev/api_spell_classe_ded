from spell import spell
import logging

logger = logging.getLogger('Classe')


def classe():
    classes = ""
    for chave in spell.__spellByClass.keys():
        classes += chave + ", "

    logger.info(classes)

    return classes
