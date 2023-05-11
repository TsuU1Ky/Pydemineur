# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    if type(grille) != list:
        return False
    if not grille:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return not all(
        not isinstance(line, list) or len(line) != nc or not all(type_cellule(cell) for cell in line)
        for line in grille
    )

    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(lig:int, col:int) -> list:
    """
    Crée une grille (liste 2D) en fonction du nombre de lignes et de colonnes placées en paramètre.

    :param lig: Nombre de ligne de la grille
    :type lig: int
    :param col: Nombre de colonne de la grille
    :type col: int
    :raises ValueError: Si le nombre de lignes ou le nombre de colonnes est négatif ou nul
    :raise TypeError: Si l’un des deux paramètres (ou les deux) n’est pas de type entier
    :return: Une liste 2D de dimension (ligne,colonne)
    :rtype: list
    """

    if lig <= 0 or col <= 0 :
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {lig} ou de colonnes {col} est négatif ou nul.")
    if type(lig) != int or type(col)!=int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {lig} ou de colonnes {col} n'est pas un entier.")

    tab :list = []

    for i in range (lig):
        row :list = []

        for j in range(col):
            row.append(construireCellule())
            
        tab.append(row)

    return tab 


def getNbLignesGrilleDemineur(grille:list) -> int:
    """
    Récupère le nombre de ligne de la grille placée en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :raise TypeError: Si le paramètre ne correspond pas à une grille de démineur
    :return: Nombre de ligne de la grille
    :rtype: int
    """

    if not type_grille_demineur(grille):
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre {grille} n'est pas une grille.")

    return len(grille)


def getNbColonnesGrilleDemineur(grille:list) -> int:
    """
    Récupère le nombre de colonne de la grille placée en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :raise TypeError:  Si le paramètre ne correspond pas à une grille de démineur
    :return: Nombre de colonne de la grille
    :rtype: int
    """

    if not type_grille_demineur(grille):
        raise TypeError(f"getNbColonnesGrilleDemineur : Le paramètre {grille} n'est pas une grille.")

    return len(grille[0])


def isCoordonneeCorrecte(grille:list, coord:tuple) -> bool:
    """
    Vérifie si les coordonnées 'coord' placées en paramètre sont présentes dans la grille.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :raise TypeError : Si un des paramètres n’est pas du bon type ou ne représente pas une grille ou une coordonnée
    :return: 'Vrai' si les coordonnées sont dans la grille; 'False' sinon 
    :rtype: bool
    """

    if not type_grille_demineur(grille) :
        raise TypeError(f"isCoordonneeCorrecte : Le paramètres {grille} n'est pas du bon type.")
    if not type_coordonnee(coord):
        raise TypeError(f"isCoordonneeCorrecte : Le paramètres {coord} n'est pas du bon type.")

    if (coord[0] >= 0 and coord[0] <= getNbLignesGrilleDemineur(grille)-1) and (coord[1] >= 0 and coord[1] <= getNbColonnesGrilleDemineur(grille)-1):
        return True

    return False


def getCelluleGrilleDemineur(grille:list, coord:tuple) -> dict :
    """
    Récupère le dictionnaire, représentant une cellule, aux coordonnées 'coord' de la grille, tout deux placés en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :raise TypeError: Si un des paramètres n’est pas du bon type ou ne représente pas une grille ou une coordonnée
    :raise IndexError: Si la coordonnée ne se trouve pas dans la grille
    :return: Dictionnaire représentant une cellule de la grille
    :rtype: dict
    """

    if not type_grille_demineur(grille):
        raise TypeError(f"getCelluleGrilleDemineur : Le paramètres {grille} n'est pas du bon type.")
    if not type_coordonnee(coord):
        raise TypeError(f"getCelluleGrilleDemineur : Le paramètres {coord} n'est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord) :
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")

    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille:list, coord:tuple) -> int:
    """
    Récupère le contenu du dictionnaire, représentant une cellule, aux coordonnées 'coord' de la grille, tout deux placés en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :return: Contenu de la cellule, chiffre contenu entre 0 et 8 (inclus) ou const.ID_MINE
    :rtype: int
    """

    return getContenuCellule(getCelluleGrilleDemineur(grille,coord))


def setContenuGrilleDemineur(grille:list, coord:tuple, content:int) -> None:
    """
    Modifie / Actualise le contenu du dictionnaire représentant une cellule aux coordonnées 'coord' de la grille, tout deux placés en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :param content: Chiffre contenu entre 0 et 8 (inclus) ou 'const.ID_MINE' (valant -1)
    :type content: int
    :return: None
    """

    setContenuCellule(getCelluleGrilleDemineur(grille,coord), content)

    return None


def isVisibleGrilleDemineur(grille:list, coord:tuple) -> bool:
    """
    Affiche la visibilité du dictionnaire, représentant une cellule, aux coordonnées 'coord' de la grille, tout deux placés en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :return: Visibilité de la cellule, 'True' si Visible; 'False' sinon
    :rtype: bool
    """

    return isVisibleCellule(getCelluleGrilleDemineur(grille,coord))


def setVisibleGrilleDemineur(grille:list, coord:tuple, visible:bool) -> None:
    """
    Modifie / Actualise la visibilité du dictionnaire, représentant une cellule, aux coordonnées 'coord' de la grille, tout deux placés en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :param visible: Représente la visibilité de la cellule
    :type visible: bool
    :return: None
    """

    setVisibleCellule(getCelluleGrilleDemineur(grille,coord), visible)

    return None


def contientMineGrilleDemineur(grille:list, coord:tuple) -> bool:
    """
    Vérifie si la cellule aux positions 'coord' contient une mine.

    :param grille: Liste 2D représentant la grille
    :type grille: list 
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord: tuple
    :return: Retourne 'True' si la cellule aux positions 'coord' contient une mine; 'False' sinon
    :rtype: bool
    """
    return contientMineCellule(getCelluleGrilleDemineur(grille,coord))


def getCoordonneeVoisinsGrilleDemineur(grille:list, coord:tuple) -> list:
    """
    Place les coordonnées de toutes les cellules voisines de la cellule aux coordonnées 'coord', dans une liste.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées (ligne,colonne)
    :type coord tuple
    :raise TypeError: Si les paramètres ne correspondent pas à une grille et à une coordonnée
    :raise IndexError: Si la coordonnée ne tombe pas dans la grille
    :return: Retourne une liste contenant toutes les coordonnées des cellules voisines
    :rtype: list
    """

    if not type_grille_demineur(grille):
        raise TypeError(f"getCoordonneeVoisinsGrilleDemineur : Le paramètres {grille} n'est pas du bon type.")
    if not type_coordonnee(coord):
        raise TypeError(f"getCoordonneeVoisinsGrilleDemineur : Le paramètres {coord} n'est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord) :
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : Coordonnées non contenue dans la grille.")

    ligne = coord[0]
    colonne = coord[1]
    voisins:list = []

    #Vérif que les ligne ne puissent pas être négatif
    if ligne-1 >= 0 : 
        if isCoordonneeCorrecte(grille,(coord[0] - 1,colonne + 1)) : #cellule Nord-Est
            voisins.append((ligne - 1,colonne + 1))

        if isCoordonneeCorrecte(grille,(ligne - 1,colonne)) : #cellule Nord
            voisins.append((ligne - 1,colonne))

    #Vérif que ligne et colonne ne puissent pas être négatif
    if ligne-1 >= 0 and colonne-1 >= 0 : 
        if isCoordonneeCorrecte(grille,(coord[0] - 1,colonne - 1)) : #cellule Nord-Ouest
            voisins.append((ligne - 1,colonne - 1))

    #Vérif que les colonne ne puissent pas être négatif
    if colonne-1 >= 0 : 
        if isCoordonneeCorrecte(grille,(ligne,colonne - 1)) : #cellule Ouest
            voisins.append((ligne,colonne - 1))

        if isCoordonneeCorrecte(grille,(ligne + 1,colonne - 1)) : #cellule Sud-Ouest
            voisins.append((ligne + 1,colonne - 1))


    if isCoordonneeCorrecte(grille,(ligne + 1,colonne)): #cellule Sud
        voisins.append((ligne + 1,colonne))
    
    if isCoordonneeCorrecte(grille,(ligne + 1,colonne + 1)): #cellule Sud-Est
        voisins.append((ligne + 1,colonne + 1))

    if isCoordonneeCorrecte(grille,(ligne,colonne + 1)): #cellule Est
        voisins.append((ligne,colonne + 1))

    
    return voisins


def placerMinesGrilleDemineur(grille:list, nb:int, coord:tuple) -> None:
    """
    Place le nombre de mine 'nb', de façon aléatoire, sauf sur la cellule de coordonnées 'coord'.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param nb: Nombre de mine devant être créé et placée par la foncion
    :type nb: int
    :param coord: Tuple de coordonnées(ligne,colonne) de la cellule de départ
    :type coord: tuple
    :raise ValueError: Si le nombre de mines est négatif ou dépasse le nombre total de cases de la grille moins une case
    :raise IndexError: Si la coordonnée ne tombe pas dans la grille
    :return: None
    """

    if nb < 0 or nb >= getNbLignesGrilleDemineur(grille)*getNbColonnesGrilleDemineur(grille) -1 :
        raise ValueError(f"placerMinesGrilleDemineur : Nombre de bombes {nb} à placer incorrect")
    if not isCoordonneeCorrecte(grille,coord): 
        raise IndexError(f"placerMinesGrilleDemineur : les coordonnées {coord} ne sont pas dans la grille")

    i = 0

    #Tant que le nombre de mine placée est inférieur au nombre de mine demandé en paramètre, faire :
    while i < nb:
        #Génère aléatoirement des coordonnées (y,x) dans la grille
        mine_coord_y = randint(0,getNbLignesGrilleDemineur(grille)-1)
        mine_coord_x = randint(0,getNbColonnesGrilleDemineur(grille)-1)

        #Exeption si les coordonneés générées aléatoirement son les mêmes que les coordonnées placées en paramètre
        while (mine_coord_y, mine_coord_x) == coord:
            mine_coord_y = randint(0,getNbLignesGrilleDemineur(grille)-1)
            mine_coord_x = randint(0,getNbColonnesGrilleDemineur(grille)-1)

        #Si le contenu de la cellule selectionnée au hasard ne contient pas de mine, alors on lui donne une mine
        if getContenuGrilleDemineur(grille,(mine_coord_y,mine_coord_x)) != const.ID_MINE :
            setContenuGrilleDemineur(grille, (mine_coord_y,mine_coord_x), const.ID_MINE)
            i += 1

    compterMinesVoisinesGrilleDemineur(grille)
    
    return None


def compterMinesVoisinesGrilleDemineur(grille:list) -> None:
    """
    Parcours de toutes la grille, et définit le contenu de chaque cellule en fonction du nombre de voisin étant une mine.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :return: None
    """

    #Boucle parcourant toutes les lignes de la grille
    for i in range(0, getNbLignesGrilleDemineur(grille)):

        #Boucle parcourant toutes les colonnes de la grille
        for j in range(0, getNbColonnesGrilleDemineur(grille)):

            nb = 0

            #Si la cellule (i,j) est une mine, on la skip
            if not contientMineGrilleDemineur(grille,(i,j)):
                lst_voisins = getCoordonneeVoisinsGrilleDemineur(grille,(i,j))

                #Pour chaque voisin de la cellule (i,j), on regarde s'il est une mine
                for elem in lst_voisins:
                
                    #On incrémente 'nb' de 1 si un voisin de (i,j) est une mine
                    if contientMineGrilleDemineur(grille,elem):
                        nb += 1

                setContenuGrilleDemineur(grille,(i,j),nb)
    

    return None


def getNbMinesGrilleDemineur(grille:list) -> int:
    """
    Parcours de toutes la grille, et compte le nombre de mine.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :raise ValueError: Si le paramètre n’est pas une grille
    :return: Le nombre de mine se trouvant dans la grille
    :rtype: int
    """

    if not type_grille_demineur(grille):
        raise ValueError(f"getNbMinesGrilleDemineur : le paramètre {grille} n'est pas une grille.")

    nb_mines = 0

    #Boucle parcourant toutes les lignes de la grille
    for i in range(0, getNbLignesGrilleDemineur(grille)):

        #Boucle parcourant toutes les colonnes de la grille
        for j in range(0, getNbColonnesGrilleDemineur(grille)):

            #On regarde si la cellule (i,j) est une mine
            if contientMineGrilleDemineur(grille,(i,j)):
                nb_mines += 1

    return nb_mines


def getAnnotationGrilleDemineur(grille:list, coord:tuple) -> str:
    """
    Récupère l'annotation du dictionnaire, représentant une cellule, aux coordonnées 'coord' de la grille, tout deux placés en paramètre.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :param coord: Tuple de coordonnées(ligne,colonne)
    :type coord: tuple
    :return: Valeur de l'annotation de la cellule, pouvant être ('None','Flag','Doute')
    :rtype: str
    """

    return getAnnotationCellule(getCelluleGrilleDemineur(grille,coord))


def getMinesRestantesGrilleDemineur(grille:list) -> int:
    """
    Parcours de toutes la grille, et compte le nombre de drapeau 'FLAG' posé sur la grille.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :return: Le nombre de mines moins le nombre de drapeau présent sur la grille; Soit le nombre de drapeau restant à poser
    :rtype: int
    """

    nb_FLAG = 0
    nb_mines = getNbMinesGrilleDemineur(grille)

    #Boucle parcourant toutes les lignes de la grille
    for i in range(0, getNbLignesGrilleDemineur(grille)):

        #Boucle parcourant toutes les colonnes de la grille
        for j in range(0, getNbColonnesGrilleDemineur(grille)):

            #On regarde si la cellule (i,j) est un drapeau
            if getAnnotationCellule(getCelluleGrilleDemineur(grille,(i,j))) == const.FLAG:
                nb_FLAG += 1

    return nb_mines - nb_FLAG


def gagneGrilleDemineur(grille: list) -> bool:
    """
    Vérifie si la partie est gagné, c'est-à-dire que toutes les cellules ne contenant pas de mine sont dévoillées, et que toutes les mines sont marquées par un drapeau.

    :param grille: Liste 2D représentant la grille
    :type grille: list
    :return: 'True' si toutes les cellules ne contenant pas de mine sont dévoillées, et que toutes les mines sont marquées par un drapeau; 'False' sinon
    :rtype: bool
    """

    # Initialisation des variables
    ligne = getNbLignesGrilleDemineur(grille)
    colonne = getNbColonnesGrilleDemineur(grille)
    nb_case_total = ligne * colonne
    nb_case_devoille = 0
    nb_mines = 0

    # Boucle parcourant toutes les lignes de la grille
    for i in range(0, ligne):

        # Boucle parcourant toutes les colonnes de la grille
        for j in range(0, colonne):

            # Compte le nombre de cellule qui sont dévoillées
            if isVisibleCellule(getCelluleGrilleDemineur(grille, (i, j))):
                nb_case_devoille += 1

            # Compte du nombre de mine
            if contientMineGrilleDemineur(grille, (i, j)):
                nb_mines += 1
                
    # Return 'True' si le nombre des cases dévoillé et le nombre de mine est égal au total de cases dans la grille; 'False' sinon 
    return nb_mines + nb_case_devoille == nb_case_total

def perduGrilleDemineur(grille:list) -> bool:
    """
    Vérifie si la partie est perdu, c'est-à-dire quand une mine est dévoillée.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :return: 'True' si une mine est dévoillée; 'False' sinon 
    :rtype: bool
    """

    #Boucle parcourant toutes les lignes de la grille
    for i in range(0, getNbLignesGrilleDemineur(grille)):

        #Boucle parcourant toutes les colonnes de la grille
        for j in range(0, getNbColonnesGrilleDemineur(grille)):

            #Vérifie qu'aucune mine n'est dévoillé
            if contientMineGrilleDemineur(grille, (i,j)) and isVisibleCellule(getCelluleGrilleDemineur(grille,(i,j))):
                return True
    
    return False


def reinitialiserGrilleDemineur(grille:list) -> None :
    """
    Réinitialise toutes les cellules de la grille une par une.

    :param grille: Liste 2D représentant la grille 
    :type grille: list
    :return: None
    """

    #Boucle parcourant toutes les lignes de la grille
    for i in range(0, getNbLignesGrilleDemineur(grille)):

        #Boucle parcourant toutes les colonnes de la grille
        for j in range(0, getNbColonnesGrilleDemineur(grille)):
            
            reinitialiserCellule(getCelluleGrilleDemineur(grille, (i,j)))


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Rend visible toutes les cellules voisines des cellules valant 0, et ainsi de suite.

    :param grille: Liste 2D représentant la grille
    :type grille: list
    :param coord : Tuple représentant les coordonnées de la cellule sélectionnée
    :type coord: tuple
    :return: L'ensemble des positions des cellules découvertes
    :rtype: set
    """
    # Initalisation des variables
    cell_decouverte = {coord}
    cell_a_decouvrir = {coord}

    # On affiche la cellule en position 'coord'
    setVisibleGrilleDemineur(grille, coord, True)

    #Si le contenu de la cellule en position 'coord' vaut 0, faire:
    if getCelluleGrilleDemineur(grille, coord)[const.CONTENU] == 0:

        # Tant que l'ensemble 'cell_a_decouvrir' n'est pas vide, faire :
        while cell_a_decouvrir:

            # On rend visibile les positions récupérées dans 'cell_a_decouvrir'
            pos = cell_a_decouvrir.pop()
            setVisibleGrilleDemineur(grille, pos, True)
            # On ajoute 'pos' dans l'ensemble des 'cell_decouverte'
            cell_decouverte.add(pos)
            # On récupère les voisins de la cellule 'pos'
            voisins = getCoordonneeVoisinsGrilleDemineur(grille, pos)
            
            # Pour chaque voisin, on vérifie qu'il n'a pas déjà été découvert, sinon on le découvre et l'ajoute à l'ensemble des 'cell_decouverte'
            for cellule in voisins:

                if cellule not in cell_decouverte:
                    
                    # Si le contenu du voisin vaut 0, on l'ajoute dans l'ensemble des 'cell_a_decouvrir'
                    if getCelluleGrilleDemineur(grille, cellule)[const.CONTENU] == 0:
                        cell_a_decouvrir.add(cellule)
                        
                    setVisibleGrilleDemineur(grille, cellule, True)
                    cell_decouverte.add(cellule)


    return cell_decouverte


def simplifierGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Prend la cellule sélectionnée, et regarde dans ses voisins si le nombre de drapeau est égal au nombre de son contenu;
    si oui, la fonction rend visible tout les cellules voisines, qui ne le sont pas.

    :param grille: Liste 2D représentant la grille
    :type grille: list
    :param coord : Tuple représentant les coordonnées de la cellule sélectionnée
    :type coord: tuple
    :return: L'ensemble des positions des cellules rendues visibles
    :rtype: set
    """

    rendu_visible = set()

    if not isVisibleGrilleDemineur(grille, coord):
        return rendu_visible

    # Récupération des voisins de la cellule en position 'coord'
    voisins: list = getCoordonneeVoisinsGrilleDemineur(grille, coord)

    # Compte du nombre de cellule ayant un drapeau dans les voisins de la cellule
    cell_flagged = 0
    for cellule in voisins:
        if getAnnotationGrilleDemineur(grille, cellule) == const.FLAG:
            cell_flagged += 1

    # Si le contenu de la cellule sélectionnée est égal aux nombre de case ayant un drapeau voisines, faire:
    if getContenuGrilleDemineur(grille, coord) == cell_flagged:

        for cellule in voisins:
            if (
                not isVisibleGrilleDemineur(grille, cellule)
                and getAnnotationGrilleDemineur(grille, cellule) != const.FLAG
            ):
                setVisibleGrilleDemineur(grille, cellule, True)
                rendu_visible.add(cellule)

    return rendu_visible


def ajouterFlagsGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Prend la cellule sélectionnée, et regarde dans ses voisins si le nombre de cellule étant non-visible est égal au nombre de son contenu;
    si oui, la fonction pose des drapeaux sur tout les cellules voisines non-visible.

    :param grille: Liste 2D représentant la grille
    :type grille: list
    :param coord : Tuple représentant les coordonnées de la cellule sélectionnée
    :type coord: tuple
    :return: L'ensemble des positions des cellules qui ont reçu un drapeau
    :rtype: set
    """

    cellule_flagged = set()

    if not isVisibleGrilleDemineur(grille, coord):
        return cellule_flagged

    # Récupération des voisins de la cellule en position 'coord'
    voisins: list = getCoordonneeVoisinsGrilleDemineur(grille, coord)

    # Compte du nombre de cellule non visible dans les voisins de la cellule
    cell_a_flag = 0
    for cellule in voisins:
        if not isVisibleGrilleDemineur(grille, cellule):
            cell_a_flag += 1

    # Si le contenu de la cellule sélectionnée est égal aux nombre de case non visible voisines, faire:
    if getContenuGrilleDemineur(grille, coord) == cell_a_flag:
        for cellule in voisins:
            # Si la cellule n'est pas visible et qu'elle n'a pas déjà un drapeau, faire:
            if (
                not isVisibleGrilleDemineur(grille, cellule)
                and getAnnotationGrilleDemineur(grille, cellule) != const.FLAG
            ):
                # Modification de l'annotation de la cellule, pour lui mettre un drapeau
                changeAnnotationCellule(getCelluleGrilleDemineur(grille, cellule))
                cellule_flagged.add(cellule)

    return cellule_flagged


def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """
    Tant que la grille peut évolué, lance les fonctions 'simplifierGrilleDemineur' et 'ajouterFlagsGrilleDemineur' sur toutes les cellules de la grille.

    :param grille: Liste 2D représentant la grille
    :type grille: list
    :return: Tuple: Premier élément : L’ensemble des coordonnées des cellules rendues visible;
                           Second élément : L’ensemble des coordonnées des cellules sur lesquelles a été ajouté un drapeau
    :rtype: tuple
    """

    # Initialisation des variables
    visible = set()
    flagged = set()
    update_possible = True
    old_visible = set()
    old_flagged = set()
    resolu = set()

    while update_possible:

        # Boucle parcourant toutes les lignes de la grille
        for i in range(0, getNbLignesGrilleDemineur(grille)):

            # Boucle parcourant toutes les colonnes de la grille
            for j in range(0, getNbColonnesGrilleDemineur(grille)):
                
                # Si la cellule en position (i,j) n'a pas été complètement résolu, faire :
                if (i, j) not in resolu:
                    # Initiation du compte de voisin découvert
                    devoille = 0
                    # Récupération des voisins de la cellule en position '(i, j)'
                    voisins: list = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))

                    # Check si tout les voisins sont dévoilés, afin de
                    for cellule in voisins:
                        # On regarde que chaque voisin et soit découvert, soit marqué d'un drapeau
                        if (isVisibleGrilleDemineur(grille, cellule) or getAnnotationGrilleDemineur(grille, cellule) == const.FLAG):
                            devoille += 1

                            # Si les voisins de la cellule sont tous dévoillés (ou marqué), elle est donc résolu, plus besoin de passer par elle
                            if devoille == 8:
                                resolu.add((i, j))

                    visible |= simplifierGrilleDemineur(grille, (i, j))
                    flagged |= ajouterFlagsGrilleDemineur(grille, (i, j))

        # Vérification d'une modification entre l'ancienne grille et la nouvelle
        if visible == old_visible and flagged == old_flagged:
            update_possible = False

        # Récupération de l'état de l'ancienne grille
        old_visible |= visible
        old_flagged |= flagged

    return (visible, flagged)