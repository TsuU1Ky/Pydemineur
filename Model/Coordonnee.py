# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return (
        type(coord) == tuple
        and len(coord) == 2
        and type(coord[0]) == int
        and type(coord[1]) == int
        and coord[0] >= 0
        and coord[1] >= 0
    )


def construireCoordonnee(lig: int, col: int) -> tuple:
    """
    Crée des coordonnées sous format tuple, depuis le numéro de ligne et le numéro de colonne placé en paramètre.

    :param lig: Le numéro de ligne
    :type lig: int
    :param col: Le numéro de colonne
    :type col: int
    :raise TypeError: Si les paramètres ne sont pas des entiers
    :raise ValueError: Si les entiers ne sont pas positifs
    :return: Les coordonnées (ligne,colonne) mises en paramètre
    :rtype: tuple
    """
    
    if type(lig) != int or type(col) != int :
        raise TypeError(f"construireCoordonnee : Le numéro de ligne ({lig}) ou le numéro de colonne ({col}) ne sont pas des entiers.")
    if lig < 0 or col < 0 :
        raise ValueError(f"construireCoordonnee : Le numéro de ligne ({lig}) ou le numéro de colonne ({col}) ne sont pas positifs.")
    return (lig, col)


def getLigneCoordonnee(coord: tuple) -> int:
    """
    Récupère le numéro de ligne depuis les coordonnées sous format 'tuple' mis en paramètre.

    :param coord: Coordonnées (ligne,colonne)
    :type coord: tuple
    :raise TypeError: Si le paramètre passé en paramètre ne correspond pas à une coordonnée
    :return: Le numéro de ligne depuis les coordonnées mises en paramètre
    :rtype: int
    """
    
    if not type_coordonnee(coord):
        raise TypeError(f"getLigneCoordonnee : Le paramètre ({coord}) n’est pas une coordonnée")
    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    """
    Récupère le numéro de colonne depuis les coordonnées sous format 'tuple' mis en paramètre.

    :param coord: Coordonnées (ligne,colonne)
    :type coord: tuple
    :raise TypeError: Si le paramètre passé en paramètre ne correspond pas à une coordonnée
    :return: Le numéro de colonne depuis les coordonnées mises en paramètre
    :rtype: int
    """
    
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee : Le paramètre ({coord}) n’est pas une coordonnée")
    return coord[1]
