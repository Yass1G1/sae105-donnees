"""
====================
Module `tools_date`
====================

A télécharger :download:`ici </../../src/tools/tools_date.py>`.

"""
# Les jours de la semaine
JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]

# Les mois
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]

import datetime  # Import du package gérant les dates


def get_date_courante() -> str:
    """Renvoie la date courante à partir de l'horloge-système.

    :return: La date courante au format ``JJ-MM-AAAA``
    """
    n = datetime.date.today()
    return "{:02d}-{:02d}-{}".format(n.day, n.month, n.year)


def get_numero_jour_semaine(jour: int, mois: int, annee: int) -> int:
    """Pour une date donnée avec son numéro de ``jour``, de ``mois`` et son ``annee``, détermine le jour de la semaine
    auquel correspond la date du ``jour-mois-annee``. La fonction calcule (et renvoie) un
    numéro dont la valeur s'interprète avec la correspondance suivante :

    +-----------+----------+-------+-------+----------+-------+----------+--------+
    | numéro    | 0        | 1     | 2     | 3        | 4     | 5        | 6      |
    +===========+==========+=======+=======+==========+=======+==========+========+
    | Jour      | dimanche | lundi | mardi | mercredi | jeudi | vendredi | samedi |
    +-----------+----------+-------+-------+----------+-------+----------+--------+

    :param jour: le jour dans la date à analyser
    :param mois: le mois dans la date à analyser
    :param annee: l'année dans la date à analyser
    :return: le numéro du jour de la semaine
    """
    c = (14 - mois) // 12
    a = annee - c
    m = mois + 12 * c - 2
    numero = (jour + a + a // 4 - a // 100 + a // 400 + 31 * m // 12) % 7
    return numero


def est_valide(jour: int, mois: int, annee: int) -> bool:
    """
    Teste si la date, fournie avec son ``jour``, son ``mois`` et son ``annee``, est valide et renvoie la réponse au
    format booléen.

    :param jour: le jour de la date à analyser
    :param mois: le mois de la date à analyser
    :param annee: l'année de la date à analyser
    :return: la date est-elle valide ?
    """

    if annee < 1583:  # Limite du calendrier Grégorien
        return False
    else:
        # Test du mois
        if mois in [1, 3, 5, 7, 8, 10,
                    12]:  # Le mois est-il janvier ou mars ou mai ou juillet ou août ou octobre ou décembre,
            if 1 <= jour <= 31:  # le jour est-il compris entre 1 et 31 inclus
                return True
            else:
                return False
        elif mois in [4, 6, 9, 11]:  # Le mois est-il avril, juin, septembre, novembre
            if 1 <= jour <= 30:  # le jour est-il compris entre 1 et 30 inclus
                return True
            else:
                return False
        elif mois == 2:  # mois de fevrier
            # L'année est-elle bissextile ? (cf. exo anneeBissextile)
            bissextile = not (annee % 4) and (annee % 100) or not (annee % 400)

            if bissextile and (1 <= jour <= 29):  # bissextile à 29 jours ?
                return True
            elif not bissextile and (1 <= jour <= 28):  # non bissextile avec 28 jours ?
                return True
            else:  # hors limite des jours
                return False
        else:  # mois inexistant
            return False


def lendemain(date: str) -> str:
    """
    Calcule la date du lendemain.

    :param date: la date
    :return: la date du lendemain
    """
    jour = datetime.datetime.strptime(date, "%d-%m-%Y")
    duree_de_un_jour = datetime.timedelta(1)  # Représente la durée d'une journée
    demain = jour + duree_de_un_jour
    return demain.strftime("%d-%m-%Y")


def conversion_date_iso(date: str) -> str:
    """
    Convertit une date au format français (``"jj-mm-aaaa"``) vers le format iso (``"aaaa-mm-jj"``).

    :param date: la date au format français
    :return: la date au format iso
    """
    jour = datetime.datetime.strptime(date, "%d-%m-%Y")
    return jour.isoformat()


def nombre_jours(date1: str, date2: str) -> int:
    """
    Calcule le nombre de jours entre la date ``date1`` et la date ``date2``.
    Celles-ci sont données au format français ``"jj-mm-aaaa"`` et ``date1`` est antérieure à ``date2``.

    :param date1: la première date
    :param date2: la seconde date
    :return: le nombre de jours entre ``date1`` et ``date2``
    """

    d1 = datetime.datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(date2, "%d-%m-%Y")
    delta = d2 - d1
    return delta.days

