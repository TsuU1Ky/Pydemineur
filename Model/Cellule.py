# Model/Cellule.py
#
from typing import Union
from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(content:int) -> bool:
    """
    Vérifie si le paramètre 'content' est bien un chiffre de type 'int', et est entre 0 et 8 (inclus).

    :param content: Chiffre contenu entre 0 et 8 (inclus) ou const.ID_MINE (valant -1)
    :type content: int
    :return: 'Vrai' si 'content' est un chiffre contenu entre 0 et 8 (inclu) ou const.ID_MINE; 'False' sinon
    :rtype: bool
    """

    if type(content) == int and content >= 0 and content <= 8 or content == const.ID_MINE:
        return True
    else :
        return False


def construireCellule(content:int = 0, visible:bool = False) -> dict :
    """
    Crée un dictionnaire qui formera une cellule, construit d'un chiffre : 'content', et d'une visibilité : 'visible'.

    :param content: Chiffre contenu entre 0 et 8 (inclus) ou const.ID_MINE (valant -1)
    :type content: int
    :param visible: Bool valant False tant que la case n'est pas visible
    :type visible: bool
    :raise ValueError: Si le paramètre correspondant au contenu n’est pas correct
    :raise TypeError: Si le second paramètre n’est pas un booléen
    :return: Dictionnaire représentant une cellule
    :rtype: dict
    """

    if not isContenuCorrect(content) :
        raise ValueError(f"construireCellule : Le contenu {content} n'est pas correct")
    if type(visible) != bool :
        raise TypeError(f"construireCellule : Le second paramètre {visible} n'est pas un booléen")

    cellule = {
        const.CONTENU : content,
        const.VISIBLE : visible,
        const.ANNOTATION : None
    }

    return cellule


def getContenuCellule(cell:dict) -> int:
    """
    Récupère le contenu de la cellule placée en paramètre.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :raise TypeError: : Si le paramètre n’est pas une cellule
    :return: Le contenu de la cellule, chiffre entre -1 et 8 (inclu)
    :rtype: int
    """

    if not type_cellule(cell):
        raise TypeError(f"getContenuCellule : Le paramètre {cell} n'est pas une cellule.")

    return cell[const.CONTENU]


def isVisibleCellule(cell:dict) -> bool :
    """
    Récupère la constante 'const.VISIBLE' de la cellule placée en paramètre.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :raise TypeError: : Si le paramètre n’est pas une cellule
    :return: La visibilité de la cellule, soit True ou False
    :rtype: bool
    """

    if not type_cellule(cell):
        raise TypeError(f"isVisibleCellule : Le paramètre {cell} n'est pas une cellule.")

    return cell[const.VISIBLE]


def setContenuCellule(cell:dict, content:int) -> None:
    """
    Modifie / Actualise le contenu de la cellule placée en paramètre.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :param content: Chiffre contenu entre 0 et 8 (inclus) ou const.ID_MINE (valant -1)
    :type content: int
    :raise TypeError: Si le premier paramètre n’est pas une cellule
    :raise TypeError: Si le contenu n’est pas de type int 
    :raise ValueError: Si le paramètre correspondant au contenu n’est pas correct
    :return: None
    """

    if type(content) != int :
        raise TypeError(f"setContenuCellule : Le second paramètre {content} n'est pas un entier.")
    if not type_cellule(cell):
        raise TypeError(f"setContenuCellule :  Le premier paramètre {cell} n'est pas une cellule.")
    if not isContenuCorrect(content) :
        raise ValueError(f"setContenuCellule : la valeur du contenu {content} n'est pas correcte")
    

    cell[const.CONTENU] = content

    return None


def setVisibleCellule(cell:dict,visible:bool) -> None:
    """
    Modifie / Actualise la visibilité de la cellule placée en paramètre.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :param visible: Visibilité de la cellule, 'True' = visible, 'False' = Non-visible
    :type visible: bool
    :raise TypeError: Si le paramètre n’est pas une cellule
    :raise TypeError: Si le second paramètre n’est pas un booléen
    :return: None
    """

    if not type_cellule(cell):
        raise TypeError(f"setVisibleCellule : Le premier paramètre {cell} n'est pas une cellule.")
    if type(visible) != bool :
        raise TypeError(f"setVisibleCellule : Le second paramètre {visible} n'est pas un booléen.")

    cell[const.VISIBLE] = visible

    return None


def contientMineCellule(cell:dict) -> bool:
    """
    Vérifie si la cellule placée en paramètre contient une mine.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :raise TypeError: Si le paramètre n’est pas une cellule
    :return: 'True' si la cellule contient une mine; 'False' sinon
    :rtype: bool
    """

    if not type_cellule(cell):
        raise TypeError(f"contientMineCellule : Le paramètre {cell} n'est pas une cellule.")
    
    if getContenuCellule(cell) == const.ID_MINE : 
        return True
    
    return False


def isAnnotationCorrecte(annotation:str) -> bool :
    """
    Vérifique que l'annotation en paramètre soit bien égal à 'None', 'const.DOUTE' ou 'const.FLAG'.

    :param annotation : Str pouvant contenir 'None', 'const.DOUTE' ou 'const.FLAG'
    :type annotation; str
    :return: 'True' si l'annotation est bien égal à 'None', 'const.DOUTE' ou 'const.FLAG'; 'False' sinon
    :rtype: bool
    """

    if annotation in (None,const.FLAG,const.DOUTE):
        return True

    return False


def getAnnotationCellule(cell:dict) -> Union[str, None]:
    """
    Récupère la valeur de l'annotation de la cellule.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :raise TypeError: Si le paramètre n’est pas une cellule
    :return: Retourne l'annotation contenu dans la cellule, ou 'None'
    :rtype: Union[str, None]
    """

    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n'est pas une cellule")
    if const.ANNOTATION not in cell:
        return None

    return cell[const.ANNOTATION]


def changeAnnotationCellule(cell:dict) -> None:
    """
    Modifie la valeur de la const.ANNOTATION dans la cellule mise en paramètre, selon la boucle suivante : "None" -> "const.FLAG" -> "const.DOUTE".

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :raise TypeError: Si le paramètre n’est pas une cellule
    :return: None
    """

    if not type_cellule(cell):
        raise TypeError(f"changeAnnotationCellule : le paramètre {cell} n'est pas une cellule")
    
    if getAnnotationCellule(cell) == None:
        cell[const.ANNOTATION] = const.FLAG

    elif getAnnotationCellule(cell) == const.FLAG:
        cell[const.ANNOTATION] = const.DOUTE
        
    elif getAnnotationCellule(cell) == const.DOUTE:
        cell[const.ANNOTATION] = None

    return None


def reinitialiserCellule(cell:dict) -> None :
    """
    Réinitialise la cellule mise en paramètre avec les valeur par défaut.

    :param cell: Dictionnaire représentant une cellule
    :type cell: dict
    :return: None
    """

    setContenuCellule(cell, 0)
    setVisibleCellule(cell, False)
    cell[const.ANNOTATION] = None

    return None