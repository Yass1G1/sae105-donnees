# coding: UTF-8
"""
Script: SAE105/projet3
Création: makoo, le 13/11/2023
"""


# Imports
import tools_constantes

# Fonctions
def fournit_liste_salles(type_salle):
    '''
    :param type_salle: Type de salle choisi
    :return: Liste détaillé des salles du type "type_salle"
    '''
    salles = {
        'TD': tools_constantes.SALLES_TD_RT,
        'TP': tools_constantes.SALLES_TP_RT,
        'Amphi': tools_constantes.AMPHI,
        'Central': tools_constantes.SALLES_BAT_CENTRAL
    }

    return salles.get(type_salle, "Type de salle non répertoriée")

def calcule_semestre_module(module):
    '''
    :param module: Nom du module (Code & Diminutif)
    :return: Semestre associé au module
    '''
    return f'S{module[1]}'

def selectionne_creneaux_salle_par_semestre(calendrier, salle, semestre):


# Programme principal
def main():
    print(fournit_liste_salles('TD'))
    pass


if __name__ == '__main__':
    main()
# Fin
