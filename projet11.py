# coding: UTF-8
"""
Script: SAE105/projet11
Création: chouitiy, le 14/11/2023
"""


# Imports
import tools_constantes
import projet11
import tools_date


# Fonctions

def calcule_nombre_minutes(heure):
    '''
    :param heure (str): Heure au format "HH:MM"
    :return (str): Nombre de minutes
    '''
    heures = int(heure.split(":")[0])
    minutes = int(heure.split(":")[1])
    return heures * 60 + minutes

def calcule_duree(heure_debut, heure_fin):
    '''
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

def compare_heure(heure1, heure2):
    '''
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

    Args:
        date1 (str) : la première date
        date2 (str) : la deuxième date

    Returns:
        (int) : Renvoi 1 ou -1 selon si date1 est inférieur à date2

    '''
    if date1 == date2:
        return 0
    else:
        date1_l = date1.split("-")
        date2_l = date2.split("-")
        if date1_l[2] > date2_l[2]:
            return 1
        else:
            if date1_l[1] > date2_l[1]:
                return 1
            else:
                if date1_l[0] > date2_l[0]:
                    return 1
                else:
                    return -1

def est_date_dans_intervalle(date, debut, fin):
    '''

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
        if compare_dates(date, debut) == 1:
            return True
        elif compare_dates(fin, date) == 1:
            return True
        else:
            return False

def recupere_champ_csv(evenement, nom):
    pass


def est_dans_competence_S1(module, competence):
    '''

    Args:
        module:
        competence:

    Returns:

    '''
    pass


# Programme principal
def main():
    heure = "11:00"
    print(calcule_nombre_minutes(heure))

    evenement1 = "31-10-2021"
    evenement2 = "17-01-2022"
    tools_date.get_numero_jour_semaine(evenement1)
    tools_date.get_numero_jour_semaine(evenement2)
    print(compare_dates(evenement1, evenement2))
    pass

if __name__ == '__main__':
    main()
# Fin
