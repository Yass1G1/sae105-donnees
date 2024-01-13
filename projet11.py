# coding: UTF-8
"""
Script: SAE105/projet11
Création: chouitiy, le 14/11/2023
"""

import matplotlib.pyplot as mp
from matplotlib.gridspec import GridSpec
import numpy as np

try:
    import tools_constantes
    import tools_sae
    import tools_date
except ModuleNotFoundError:
    import tools.tools_sae
    import tools.tools_constantes
    import tools.tools_date


# Fonctions
def calcule_nombre_minutes(heure):
    """
    Converti un temps donné en heure et minutes, en minutes.
    Paramètres:
        heure (str): Heure au format "HH:MM"
    Retourne:
        (str): Nombre de minutes
    """
    heures = int(heure.split(":")[0])
    minutes = int(heure.split(":")[1])

    return heures * 60 + minutes


def calcule_duree(heure_debut, heure_fin):
    """
    Renvoi la durée d'un événement basé sur son heure de début et de fin; au format HH:MM
    Paramètres:
        heure_debut (str): l'heure de début au format "HH:MM"
        heure_fin (str): l'heure de fin au format "HH:MM"
    Retourne
        (str):  la durée au format "HH:MM"
    """
    temps_en_minute = calcule_nombre_minutes(heure_fin) - calcule_nombre_minutes(heure_debut)
    heures = temps_en_minute // 60
    minutes = temps_en_minute % 60

    if heures < 10:
        heures = "0" + str(temps_en_minute // 60)
    if minutes < 10:
        minutes = "0" + str(temps_en_minute % 60)

    return f'{heures}:{minutes}'


def compare_heures(heure1, heure2):
    """
    Renvoi 1, 0, ou 1 si heure1 est après, avant ou pareil que heure2 (respectivement).
    Paramètres:
        heure1 (str): la première heure
        heure2 (str): la seconde heure
    Retourne:
        (int): Résultat de comparaison
    """
    heure1_minute = calcule_nombre_minutes(heure1)
    heure2_minute = calcule_nombre_minutes(heure2)

    if heure1_minute < heure2_minute:
        return -1
    elif heure1_minute > heure2_minute:
        return 1
    else:
        return 0


def compare_dates(date1, date2):
    """
    Vérifie si date1 est après, avant ou pareil que date2
        Paramètres:
            date1 (str) : la première date
            date2 (str) : la deuxième date

        Retourne:
            (int) : Renvoi 1, -1 ou 0 selon si date1 est après, avant ou pareil que date2
    """
    if date1 == date2:
        return 0
    else:
        date1 = date1.split("-")
        date2 = date2.split("-")
        if date1[::-1] > date2[::-1]:  # comparer l'année > mois > jours
            return 1
        else:
            return -1


def est_date_dans_intervalle(date, debut, fin):
    """
    Vérifie si une date est incluse dans une intervalle donnée.
        Paramètres:
            date (str): la date à vérifier
            debut (str): la date de début d'intervalle (incluse)
            fin (str): la date de début d'intervalle (incluse)

        Retourne:
            (bool): Si la date est dans l'intervalle
    """
    if date == debut or date == fin:
        return True
    else:
        if compare_dates(date, debut) == 1 and compare_dates(fin, date) == 1:  # début > date > fin
            return True
        else:
            return False


def recupere_champ_csv(evenement, nom):
    """
    Sélectionne et renvoi le champ "nom" dans l'évènement spécifié.
        Paramètres:
            evenement (str): évènement au format csv
            nom (str): nom du champ spécifique

        Retourne:
                (str): le champ associé à l'évènement
    """
    event_l = evenement.split(";")
    csv_template = ["uid", "date", "debut|fin", "modules", "modalite", "evaluation", "theme", "salles", "profs", "groupes"]

    if nom == "heure":
        return event_l[2]
    elif nom == "debut":
        return event_l[2].split("|")[0]
    elif nom == "fin":
        return event_l[2].split("|")[1]
    elif nom not in csv_template:
        return None
    else:
        return event_l[csv_template.index(nom)]


def selectionne_SAE105_groupe(calendrier, groupe):
    """
    Extrait les évènements relatifs à la SAE105 auxquels assiste le groupe de TD "groupe".
    Paramètres:
        calendrier (str): Une liste d'évènements ADE
        groupe (str): Un groupe de TD

    Retourne:
        (list of str): liste de cours de SAE105 suivie par le groupe de TD
    """
    event_list = []

    for event in calendrier:
        evenement = event.split(";")
        ressource = evenement[3].split("-")[0]  # [3] = champ ressource
        group_event = evenement[-1]
        if "SAÉ105" == ressource and groupe in group_event:
            event_list.append(event)

    return tools_sae.trie_evenements_par_date(event_list)


def selectionne_ressources_groupe(calendrier, groupe):
    """
    Extrait les évènements auxquels assiste le groupe de TD "groupe".
    Paramètres:
        calendrier (str): Une liste d'évènements ADE
        groupe (str): Un groupe de TD

    Retourne:
        (list of str): liste de ressource suivie par le groupe de TD
    """
    event_list = []

    for event in calendrier:
        evenement = event.split(";")
        group_event = evenement[-1]
        if groupe in group_event:
            event_list.append(event)

    return tools_sae.trie_evenements_par_date(event_list)


def deduit_annee_du_module(module):
    """
    Déduit l'année d'un module "module" à partir de son code.
    Paramètres:
        module (str): Le module

    Retourne:
        (int or None): L'année (1, 2 ou 3) auquel à lieu le module OU None
    """
    if module == "Autre":
        return None
    elif "R" == module[0]:  # Forme "RXYY" ou "RXcyYY"
        semestre = int(module[1])  # "explicit is better than implicit"
        return (semestre + 1) // 2
    else:  # Forme commençant par "SAÉ"
        semestre = int(module[3])
        return (semestre + 1) // 2


def deduit_annee_du_groupe(groupe):
    """
    Déduit l'année du groupe de TD.
    Paramètres:
        groupe (str): Le groupe

    Retourne:
        (int or None): L'année (1, 2 ou 3) auquel appartient le groupe
    """
    return int(groupe[1])


def est_dans_competence_S1(module, competence):
    """
    Vérifie si un module fait bien parti du S1 ET de la compétence "competence".
    Paramètres:
        module (str): Un module (code & diminutif)
        competence (str): Une compétence

    Retourne:
        fait_partie (bool): True si le module fait partie de la compétence, False sinon.
    """
    fait_partie = False

    if competence not in tools_constantes.COMPETENCES:
        return fait_partie
    elif "R" == module[0] and int(module[1]) != 1:  # Forme "RXYY" ou "RXcyYY"
        return fait_partie
    elif "S" == module[1] and int(module[3]) != 1:  # Forme commençant par "SAÉ"
        return fait_partie
    else:
        num_competence = int(competence[2])
        for ressources in tools_constantes.COEFFS_S1:
            if module in ressources[0]:
                if ressources[num_competence] != 0:
                    fait_partie = True

        return fait_partie


def selectionne_creneaux_groupe_competence(calendrier, groupe, competence):
    """
    Extrait la liste d'évènement auxquels participent le groupe de TD, selon un module d'une competence du S1.
    Paramètres:
        calendrier (list of str): Liste d'évènement
        groupe (str): Groupe de TD
        competence (str): Compétence

    Retourne:
        (list of str): Liste d'évènement qui respecent les conditions de groupe et de coméptence.
    """
    event_list = []

    for event in calendrier:
        event_group = recupere_champ_csv(event, "groupes").split("|")
        if groupe in event_group:
            module = recupere_champ_csv(event, "modules").split("-")[0]
            if est_dans_competence_S1(module, competence):
                event_list.append(event)
    return tools_sae.trie_evenements_par_date(event_list)


def exemple_export_markdown():
    """
    Affiche un tableau markdown selon des données initialisées dans la fonction
    Retourne:
        None
    """
    entetes = ["Code", "Diminutif", "Discipline"]
    donnees = ["R102;ArchiRes;Réseaux", "R204;Téléphonie;Télécoms", "R107;Python1;Info"]
    donnees_split = [x.split(";") for x in donnees]
    col_size = [len(x) + 1 for x in entetes]  # définit la largeur de chaque colonne

    # Vérifie que les données ne sont pas "plus large" que la colonne
    for size in range(len(col_size)):
        for data in range(len(donnees_split)):
            if col_size[size] < len(donnees_split[data][size]) + 1:
                col_size[size] = len(donnees_split[data][size]) + 1

    # Ligne d'entête (en comblant la largeur avec des espaces)
    print("|", end="")
    for i in range(len(entetes)):
        print(f' {entetes[i]}{(col_size[i] - len(entetes[i])) * " "}|', end="")

    # Ligne du séparateur (selon la largeur) + 2 ([0] = ":" et [-1] = "-")
    print("\n|", end="")
    for j in range(len(entetes)):
        print(f':{"-" * col_size[j]}|', end="")

    # Lignes des données (en alignant les colonnes en comblant avec des espaces)
    for k in range(len(donnees)):
        print("\n|", end="")
        for champ in range(len(donnees)):
            print(f' {donnees_split[k][champ]}{(col_size[champ] - len(donnees_split[k][champ]) - 1) * " "} |', end="")

    print("")


def nb_heures_par_modalite(calendrier):
    """
    Renvoi le nombre d'heures par modalité.
    Paramètres:
        calendrier (list of str): Liste d'événement sous forme de str

    Retourne:
        (list of floats): nombre d'heures par modalité (TP, CM etc.)

    """
    heures = [0, 0, 0, 0, 0]

    for event in calendrier:
        modalite = recupere_champ_csv(event, "modalite")

        h_debut = recupere_champ_csv(event, "debut")
        h_fin = recupere_champ_csv(event, "fin")
        duree = calcule_nombre_minutes(calcule_duree(h_debut, h_fin))

        heures[tools_constantes.MODALITES.index(modalite)] += duree
        heures[-1] += duree  # Total

    return [(x / 60) for x in heures]


def repartition_moyenne_volume_horaire_competence(calendrier, competence):
    """
    Calcule la répartition moyenne des voluymes horaires par modalité des modules du S1 ayant trait à une compétence.
    Paramètres:
        calendrier: Liste d'événement
        competence: Une compétence parmi 'RT1-Administrer', 'RT2-Connecter', 'RT3-Programmer'

    Retourne:
        (str): repartition moyenne du volume horaires des cours de la compétence
    """

    all_groups = [[0, 0, 0, 0, 0] for x in range(4)]

    for i in range(4):
        groupe = "B1G" + str(i + 1)
        for event in calendrier:
            module = recupere_champ_csv(event, "modules")
            if est_dans_competence_S1(module, competence) and groupe in recupere_champ_csv(event, "groupes"):

                # Durée en minute
                debut = recupere_champ_csv(event, "debut")
                fin = recupere_champ_csv(event, "fin")
                duree_heure = calcule_duree(debut, fin)
                duree_minute = calcule_nombre_minutes(duree_heure)

                # Modalite
                modalite = recupere_champ_csv(event, "modalite")
                index_modalite = tools_constantes.MODALITES.index(modalite)

                # Ajout aux listes
                all_groups[i][index_modalite] += duree_minute
                all_groups[i][-1] += duree_minute

    # Rassemblement des valeurs
    all_groups_average = [0, 0, 0, 0, 0]
    for groupe in all_groups:
        for j in range(5):
            all_groups_average[j] += groupe[j]

    # Moyenne des valeurs
    for k in range(len(all_groups_average)):
        all_groups_average[k] = (all_groups_average[k] / 60) / 4
        all_groups_average[k] = format(all_groups_average[k], '.2f')

    return f'{competence};{all_groups_average[0]};{all_groups_average[1]};{all_groups_average[2]};{all_groups_average[3]};{all_groups_average[4]}'


def traitement(calendrier):
    """
    Calcule pour les 3 compétences du S1 la répartition des volumes horaires par modalité, en donnant les moyennes par groupe.
    Paramètres:
        calendrier: Liste d'événement

    Retourne:
        (list of str): Liste du rapport de volume horaire par compétence
    """
    return [repartition_moyenne_volume_horaire_competence(calendrier, tools_constantes.COMPETENCES[x]) for x in range(3)]


def export_markdown(resultats, entetes):
    """
    Affiche un tableau markdown selon les données passées en paramètre.
    Paramètres:
        resultats: Liste des différents volumes horaires de chaque compétences
        entetes: Liste des titres de colonnes

    Retourne:
        None
    """
    donnees_split = [x.split(";") for x in resultats]
    col_size = [len(x) + 1 for x in entetes]  # définit la largeur de chaque colonne

    # Vérifie que les données ne sont pas "plus large" que la colonne
    for size in range(len(col_size)):
        for data in range(len(donnees_split)):
            if col_size[size] < len(donnees_split[data][size]) + 1:
                col_size[size] = len(donnees_split[data][size]) + 1

    # Ligne d'entête (en comblant la largeur avec des espaces)
    print("|", end="")
    for i in range(len(entetes)):
        print(f' {entetes[i]}{(col_size[i] - len(entetes[i])) * " "}|', end="")

    # Ligne du séparateur (selon la largeur) + 2
    print("\n|", end="")
    for j in range(len(entetes)):
        print(f':{"-" * col_size[j]}|', end="")

    # Lignes des données (en alignant les colonnes en comblant avec des espaces)
    for k in range(len(resultats)):
        print("\n|", end="")
        for champ in range(len(entetes)):
            print(f' {donnees_split[k][champ]}{(col_size[champ] - len(donnees_split[k][champ]) - 1) * " "} |', end="")

    print("")

def export_png(resultats):
    """
    Affiche une graphique présentant la répartion du volume horaire selon chaque modalité pour chaque compétence.
    Paramètres:
        resultats (list of str): Volumes horaires par compétence

    Retourne:
        None
    """
    x = np.array(tools_constantes.COMPETENCES)
    proj_y = np.array([float(x.split(";")[-2]) for x in resultats])
    tp_y = np.array([float(x.split(";")[-3]) for x in resultats])
    td_y = np.array([float(x.split(";")[-4]) for x in resultats])
    cm_y = np.array([float(x.split(";")[-5]) for x in resultats])

    # Grille pour l'affichage du tableau en dessous du graph
    fig = mp.figure(figsize=(8, 6))
    gs = GridSpec(2, 1, height_ratios=[3, 1])

    # Graphique à colonnes empilées
    graph = fig.add_subplot(gs[0])
    graph.bar(x, cm_y, color='#5D70C1', label='CM', edgecolor="#575757", linewidth=0.6)
    graph.bar(x, tp_y, bottom=cm_y, color='#2A2E46', label='TP', edgecolor="#575757", linewidth=0.6)
    graph.bar(x, td_y, bottom=tp_y, color='#E84E0F', label='TD', edgecolor="#575757", linewidth=0.6)
    graph.bar(x, proj_y, bottom=td_y + tp_y, color='#FFE6DF', label='Projets', edgecolor="#575757", linewidth=0.6)
    graph.legend()
    graph.set_title("Volumes horaires au S1")

    table_data = [["", x[0], x[1], x[2]],
                  ["Proj", proj_y[0], proj_y[1], proj_y[2]],
                  ["TD", td_y[0], td_y[1], td_y[2]],
                  ["TP", tp_y[0], tp_y[1], tp_y[2]],
                  ["CM", cm_y[0], cm_y[1], cm_y[2]]]

    # Ajoute le tableau EN DESSOUS du graph
    tableau = fig.add_subplot(gs[1])
    table = tableau.table(cellText=table_data, loc="center")

    # Enlever les bords de la 1ère cellule + minor changes
    table[0, 0].visible_edges = "BR"
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.5)
    tableau.axis("off")

    # Couleurs des entêtes + couleur police
    table[0, 1].set_facecolor("#8C8C8C")
    table[0, 1].set_text_props(color="white")
    table[0, 2].set_facecolor("#8C8C8C")
    table[0, 2].set_text_props(color="white")
    table[0, 3].set_facecolor("#8C8C8C")
    table[0, 3].set_text_props(color="white")

    # Couleurs des modalités + couleur police
    table[1, 0].set_facecolor("#FFE6DF")  # Proj
    table[2, 0].set_facecolor("#E84E0F")  # TD
    table[3, 0].set_facecolor("#2A2E46")  # TP
    table[3, 0].set_text_props(color="white")
    table[4, 0].set_facecolor("#5D70C1")  # CM
    table[4, 0].set_text_props(color="white")

    # Pour suivre un ordre logique sur la légende
    clrs, titles = graph.get_legend_handles_labels()
    graph.legend(reversed(clrs), reversed(titles))

    # Rajouter les lignes des ordonnées
    for y_value in np.array([0, 50, 100, 150, 200, 250, 300]):
        graph.axhline(y_value, color='#CCCCCC', linestyle='--', linewidth=0.8)

    mp.savefig("figure.png")
    mp.show()

# Programme principal
def main():
    calendrier = tools_sae.lecture_fichier_evenements("data/all.csv")

    resultats = traitement(calendrier)

    export_markdown(resultats, ["COMPETENCES", "CM", "TD", "TP", "Projet"])
    export_png(resultats)


if __name__ == '__main__':
    main()
# Fin
