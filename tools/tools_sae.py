"""
========================
Module `tools_sae`
========================

A télécharger :download:`ici </../../src/tools/tools_sae.py>`.

"""
import datetime
import os.path
import typing

import tools_constantes
import tools_date


def lecture_fichier(chemin: str) -> typing.Optional[str]:
    """
    Lecture d'un fichier, indiqué par son ``chemin`` relatif depuis le
    répertoire d'exécution du script python.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou
             :py:obj:`None` si le fichier n'a pu être lu
    """
    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None


def lecture_fichier_evenements(chemin: str) -> typing.Optional[typing.List[str]]:
    """
    Lecture d'un fichier d'évènements au format ``csv``, indiqué par son
    ``chemin`` relatif depuis le répertoire d'exécution du script python.

    :param chemin: le chemin du fichier
    :return: la liste des évènements au format csv.
    """

    with open(chemin, encoding="utf8") as fh:
            content = fh.readlines()
            calendrier = [l[:-1] if l.endswith("\n") else l for l in content]
            return calendrier

def extrait_evenement_par_id(calendrier: typing.List[str],
                             id: str) -> typing.Optional[str]:
    """
    Pour **débogage** : Recherche l'événement d'``id`` donné dans une
    liste d'événements ``calendrier`` donné au format `csv`.
    Renvoie l'événement trouvé ou :py:obj:`None` s'il n'est pas dans la liste.

    :param calendrier: Liste d'événements csv
    :return: L'événement
    """
    for event in calendrier:
        if event.startswith(id):
            return event
    return None


def liste_jours_ouvres_universitaires() -> typing.List[str]:
    """
    Renvoie la liste de tous les jours ouvrés de l'année universitaire
    (hors WE, jours fériés et vacances). Chaque jour ouvré est une chaine
    de caractères de la forme ``"JJ-MM-AAAA"``.

    :return: Liste des jours ouvrés
    """
    annee = int(tools_constantes.DEBUT_ANNEE.split("-")[-1])
    [heure_deb, minutes_deb] = [int(val) for val in tools_constantes.HEURE_DEBUT.split(":")]  # début des cours
    [heure_fin, minutes_fin] = [int(val) for val in tools_constantes.HEURE_FIN.split(":")]  # fin des cours

    periodes_scolaires = []
    for [debut, fin] in tools_constantes.PERIODES_SCOLAIRES:
        val_debut = tuple([int(val) for val in debut.split("-")][::-1])
        val_fin = tuple([int(val) for val in fin.split("-")][::-1])
        date_debut = datetime.datetime(*val_debut, hour=heure_deb, minute=minutes_deb)
        date_fin = datetime.datetime(*val_fin, hour=heure_fin, minute=minutes_fin)
        periodes_scolaires.append((date_debut, date_fin))  # date + heures des périodes de cours

    # L'année universitaire (mois, annee) hors vacances
    jours = []
    annee_universitaire = [(m, annee) for m in range(9, 13)]  # septembre-décembre
    annee_universitaire += [(m, annee + 1) for m in range(1, 9)]  # janvier-août inclus
    for (m, a) in annee_universitaire:
        for j in range(1, 32):
            valide = tools_date.est_valide(j, m, a)  # est une date valide
            jour_semaine = tools_date.get_numero_jour_semaine(j, m, a)  # le jour de la semaine
            if valide and 1 <= jour_semaine <= 5:  # les jours valides de la semaine
                # dans périodes scolaires ?
                ddate = datetime.datetime(year=a, month=m, day=j, hour=12, minute=0)  # le jour j à 12h
                dans_periode = False
                for p in periodes_scolaires:
                    if p[0] <= ddate <= p[1]:
                        dans_periode = True
                if dans_periode:
                    jours.append("{:02d}-{:02d}-{:4d}".format(j, m, a))

    # Suppression des fériés
    jours_ouvres = jours[::]
    for ferie in tools_constantes.JOURS_FERIES:
        if ferie in jours_ouvres:
            i_deb = jours_ouvres.index(ferie)  # le jour ferié
            jours_ouvres = jours_ouvres[:i_deb] + jours_ouvres[i_deb + 1:]
    return jours_ouvres


def trie_evenements_par_date(calendrier: typing.List[str]) -> typing.List[str]:
    """
    Partant d'une liste d'évènements au format `csv`, donnée
    dans ``calendrier``, retourne la liste de ses événements triés par date
    croissante.
    :fa:`warning` L'heure n'est pas prise en compte.

    :param calendrier: Liste d'événements au format `csv`
    :return: Liste d'événements triés
    """

    return sorted(calendrier, key=lambda e: "-".join(e.split(";")[1].split("-")[::-1]))


def affiche_liste_csv(donnees_csv: typing.List[str]):
    """Partant d'une liste de données au format `csv`, affiche
    dans la console chaque élément de la liste, chacun sur une ligne.

    :param calendrier: Liste de données au format `csv`
    :return: :py:obj:`None`
    """
    print("\n".join(donnees_csv))