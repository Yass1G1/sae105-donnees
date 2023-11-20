# coding: UTF-8
"""
Script: SAE105/projet11
Création: chouitiy, le 14/11/2023
"""

# Imports
import tools_constantes
import projet11
import tools_date
import tools_sae


# Fonctions

def calcule_nombre_minutes(heure):
    '''
    Converti un temps donné en heure et minutes, en minutes.
        :param heure (str): Heure au format "HH:MM"
        :return (str): Nombre de minutes
    '''
    heures = int(heure.split(":")[0])
    minutes = int(heure.split(":")[1])
    return heures * 60 + minutes


def calcule_duree(heure_debut, heure_fin):
    '''
    Renvoi la durée d'un événement basé sur son heure de début et de fin; au format HH:MM
        :param heure_debut (str): l'heure de début au format "HH:MM"
        :param heure_fin (str): l'heure de fin au format "HH:MM"
        :return (str):  la durée au format "HH:MM"
    '''
    temps_en_minute = calcule_nombre_minutes(heure_fin) - calcule_nombre_minutes(heure_debut)
    heures = temps_en_minute // 60
    minutes = temps_en_minute % 60
    if heures < 10:
        heures = "0" + str(temps_en_minute // 60)
    if minutes < 10:
        minutes = "0" + str(temps_en_minute % 60)
    return f'{heures}:{minutes}'


def compare_heures(heure1, heure2):
    '''
    Renvoi 1, 0, ou 1 si heure1 est après, avant ou pareil que heure2.
        :param heure1 (str): la première heure
        :param heure2 (str): la seconde heure
        :return (int): Résultat de comparaison
    '''
    heure1_minute = calcule_nombre_minutes(heure1)
    heure2_minute = calcule_nombre_minutes(heure2)

    if heure1_minute < heure2_minute:
        return -1
    elif heure1_minute > heure2_minute:
        return 1
    else:
        return 0


def compare_dates(date1, date2):
    '''
    Vérifie si date1 est après, avant ou pareil que date2
        Args:
            date1 (str) : la première date
            date2 (str) : la deuxième date

        Returns:
            (int) : Renvoi 1, -1 ou 0 selon si date1 est après, avant ou pareil que date2

    '''
    if date1 == date2:
        return 0
    else:
        date1_l = date1.split("-")
        date2_l = date2.split("-")
        if date1_l[2] > date2_l[2]:  # Compare les années
            return 1
        elif date1_l[2] < date2_l[2]:
            return -1
        else:
            if date1_l[1] > date2_l[1]:  # Compare les mois
                return 1
            elif date1_l[1] < date2_l[1]:
                return -1
            else:
                if date1_l[0] > date2_l[0]:  # Compare les jours
                    return 1
                else:
                    return -1


def est_date_dans_intervalle(date, debut, fin):
    '''
    Vérifie si une date est incluse dans une intervalle donnée.
        Args:
            date (str): la date à vérifier
            debut (str): la date de début d'intervalle (incluse)
            fin (str): la date de début d'intervalle (incluse)

        Returns:
            (bool): Si la date est dans l'intervalle
    '''
    if date == debut or date == fin:
        return True
    else:
        if compare_dates(date, debut) == 1 and compare_dates(fin, date) == 1:  # début > date > fin
            return True
        else:
            return False


def recupere_champ_csv(evenement, nom):
    '''
    Renvoi le champ "nom" dans l'évènement spécifié.
        Args:
            evenement (str): évènement au format csv
            nom (str): nom du champ spécifique

        Returns:
                (str): le champ associé à l'évènement

    '''
    event_l = evenement.split(";")
    csv_template = ["uid", "date", "debut|fin", "modules", "modalite", "evaluation", "theme", "salles", "profs",
                    "groupes"]
    if nom == "debut":
        return event_l[2].split("|")[0]
    elif nom == "fin":
        return event_l[2].split("|")[1]
    elif nom not in csv_template:
        return None
    else:
        return event_l[csv_template.index(nom)]


def selectionne_SAE105_groupe(calendrier, groupe):
    '''

    Args:
        calendrier (str): Une liste d'évènements ADE
        groupe (str): Un groupe de TD

    Returns:
        (list of str): liste de ressource suivie par le groupe de TD

    '''
    event_list = []
    for event in calendrier:
        evenement = event.split(";")
        ressource = evenement[3].split("-")[0]
        group_event = evenement[-1]
        if "SAÉ105" == ressource and groupe in group_event:
            event_list.append(event)
    return tools_sae.trie_evenements_par_date(event_list)

def selectionne_ressources_groupe(calendrier, groupe):
    '''

    Args:
        calendrier (str): Une liste d'évènements ADE
        groupe (str): Un groupe de TD

    Returns:
        (list of str): liste de ressource suivie par le groupe de TD

    '''
    event_list = []
    for event in calendrier:
        evenement = event.split(";")
        group_event = evenement[-1]
        if groupe in group_event:
            event_list.append(event)
    return tools_sae.trie_evenements_par_date(event_list)


def deduit_annee_du_module(module):
    '''

    Args:
        module (str): Le module

    Returns:
        (int or None): L'année (1, 2 ou 3) auquel à lieu le module OU None

    '''
    if module == "Autre":
        return None
    elif "R" == module[0]:  # Forme "RXYY" ou "RXcyYY"
        semestre = int(module[1])  # "explicit is better than implicit"
        return (semestre + 1) // 2
    else:  # Forme commençant par "SAÉ"
        semestre = int(module[3])
        return (semestre + 1) // 2

def deduit_annee_du_groupe(groupe):
    '''

    Args:
        groupe (str): Le groupe

    Returns:
        (int or None): L'année (1, 2 ou 3) auquel appartient le groupe

    '''
    return int(groupe[1])

def est_dans_competence_S1(module, competence):
    '''

    Args:
        module (str): Un module (code & diminutif)
        competence (str): Une compétence

    Returns:
        fait_partie (bool): True si le module fait partie de la compétence, False sinon.

    '''
    fait_partie = False
    if competence not in tools_constantes.COMPETENCES:
        return fait_partie
    elif "R" == module[0] and int(module[1]) != 1:  # Forme "RXYY" ou "RXcyYY"
        return fait_partie
    elif "S" == module[1] and int(module[3]) == 1:  # Forme commençant par "SAÉ"
        return fait_partie
    else:
        num_competence = int(competence[2])
        for ressource in tools_constantes.COEFFS_S1:
            if module in ressource[0]:
                if ressource[num_competence] != 0:
                    fait_partie = True

        return fait_partie

def selectionne_creneaux_groupe_competence(calendrier, groupe, competence):
    pass

# Programme principal
def main():
    heure = "11:00"
    print(calcule_nombre_minutes(heure))

    evenement1 = "31-10-2021"
    evenement2 = "17-01-2022"
    event1_l = evenement1.split("-")
    event2_l = evenement2.split("-")
    jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]

    print(
        f'\tJour de {evenement1} : {jours[tools_date.get_numero_jour_semaine(int(event1_l[0]), int(event1_l[1]), int(event1_l[2]))]}')
    print(
        f'\tJour de {evenement2} : {jours[tools_date.get_numero_jour_semaine(int(event2_l[0]), int(event2_l[1]), int(event2_l[2]))]}')

    event1_demain = tools_date.lendemain(evenement1).split("-")
    event2_demain = tools_date.lendemain(evenement2).split("-")

    print(
        f'\tLendemain de {evenement1} : {jours[tools_date.get_numero_jour_semaine(int(event1_demain[0]), int(event1_demain[1]), int(event1_demain[2]))]}')
    print(
        f'\tLendemain de {evenement2} : {jours[tools_date.get_numero_jour_semaine(int(event2_demain[0]), int(event2_demain[1]), int(event2_demain[2]))]}')

    print(est_date_dans_intervalle("15-12-2020", "01-01-2021", "31-01-2021"))
    print(compare_dates(evenement1, evenement2))

    print(tools_date.nombre_jours(evenement1, evenement2))

    evenement = "ADE0000988;05-09-2023;08:00|12:00;R3cy16-Pentesting;TP;;;IUT1_T33 res1;LUBINEAU DENIS|VEDEL FRANCK;B2GA"
    print(evenement.split(";"))
    print(recupere_champ_csv(evenement, "fin"))

    calendrier = tools_sae.lecture_fichier_evenements("data/calendrier.csv")
    print('\n')

    print(selectionne_SAE105_groupe(calendrier, 'B1G4'))
    print('\n')

    print(f'Compétences : {tools_constantes.COMPETENCES}\nCoeffs : {tools_constantes.COEFFS_S1}')


if __name__ == '__main__':
    main()
# Fin
