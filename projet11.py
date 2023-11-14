# coding: UTF-8
"""
Script: SAE105/projet11
Création: chouitiy, le 14/11/2023
"""


# Imports
import tools_constantes
import projetX

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
    return f'{temps_en_minute // 60}:{temps_en_minute % 60}'

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
        (int) : Renvoi 1 ou -1 selon si date1 et inférieur à date2

    '''
    pass

def est_dans_competence_S1(module, competence):
    '''
    :param module (str): Un module (code & diminutif)
    :param competence (str): Une compétence
    :return (bool): Si le module fait partie de compétence
    '''


# Programme principal
def main():
    print(calcule_nombre_minutes("10:12"))
    print(calcule_duree("10:12", "14:30"))
    print(compare_heure("10:12", "09:45"))
    print(tools_constantes.MODALITES)
    print(tools_constantes.GROUPES_BUT1)
    print(tools_constantes.COMPETENCES)
    print(tools_constantes.COEFFS_S1)
    pass

if __name__ == '__main__':
    main()
# Fin
