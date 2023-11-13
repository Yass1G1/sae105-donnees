"""
Module listant toutes les constantes pouvant être utilisées pour
faciliter l'écriture du code de la SAE1.05
"""

# *****************************************************************************
# Les enseignants
#: Constante donnant les enseignants permanents
ENSEIGNANTS_PERMANENTS = ["BARAS CLEO",
                          "BERGER AURELIE",
                          "DUCHAMP JEAN-MARC",
                          "GOEURIOT LORRAINE",
                          "MORAND ALAIN",
                          "SICLET CYRILLE",
                          "BENECH PHILIPPE",
                          "NOVAKOV EMIL",
                          "THIRIET JEAN MARC",
                          "CHOLLET REMY",
                          "DELNONDEDIEU YVES",
                          "DESPINASSE BRUNO",
                          "DUPONT BELRHALI KARINE",
                          "FAYOLLE GERARD",
                          "KASPER KEVIN",
                          "LUBINEAU DENIS",
                          "ROYER SANDRA",
                          "VEDEL FRANCK",
                          "ESCANDE ERIC",
                          "MARTIN JEROME"]

# *********************************************************
#: Constante donnant les modalités d'enseignement
MODALITES = ["CM", "TD", "TP","Proj"]


#: Constante donnant le code des intervention sans module
SANS_CODE = "Autre"



# *******************************************************************************
# Les salles regroupées par fonction pour le département
#: Constante donnant les types de salles
TYPES_SALLES = ["TD", "TP", "Amphi", "Central"]

#: Constante donnant les salles de TD appartenant au département RT
SALLES_TD_RT = ["IUT1_010", "IUT1_06", "IUT1_08",
                "IUT1_112B", "IUT1_119", "IUT1_120",
                "IUT1_120b", "IUT1_121_RT", "IUT1_T23_24"]

#: Constante donnant les salles de TP appartenant au département RT
SALLES_TP_RT = ["IUT1_126", "IUT1_T14 tel", "IUT1_T16 tel2",
                "IUT1_T22 info2", "IUT1_T25 info1", "IUT1_T26 proj",
                "IUT1_T27 res3", "IUT1_T32 res2", "IUT1_T33 res1"]

#: Constante donnant les amphis pour les CM partagés/mutualisés entre plusieurs départements de l'IUT
AMPHI = ["IUT1_AMPHI BELLEDONNE", "IUT1_AMPHI CHARTREUSE"]

#: Constante donnant les autres salles mutualisées/partagées entre plusieurs départements de l'IUT
SALLES_BAT_CENTRAL = ["IUT1_C003", "IUT1_C007", "IUT1_C011",
                      "IUT1_C103", "IUT1_C104", "IUT1_C105",
                      "IUT1_C201", "IUT1_C202", "IUT1_C215"]

# **********************************************************************
# Les groupes (de TD) d'étudiants

#: Constante donnant les groupes de TD de BUT1
GROUPES_BUT1 = ["B1G1", "B1G2", "B1G3", "B1G4"]

#: Constante donnant les groupes de TD de BUT2
GROUPES_BUT2 = ["B2G1", "B2G2", "B2GA"]

#: Constante donnant les groupes de TD de BUT3
GROUPES_BUT3 = ["B3cy1", "B3dc2", "B3cyA", "B3cyB", "B3dcC"]

#: Constante donnant les groupes de TD toutes années confondues
GROUPES = GROUPES_BUT1 + GROUPES_BUT2 + GROUPES_BUT3

# ***********************************************************************
# L'année universitaire 2021-2022

#: Constante donnant le début de l'année universitaire pour les étudiants de S1 et de S3
DEBUT_ANNEE = "01-09-2023"
DEBUT_ANNEE_PROCHAINE = "01-09-2024"

#: Constante donnant la fin d'année universitaire (correspondant à la fin des semestres S2 et S4)
FIN_ANNEE = "31-07-2024"

#: Constante donnant l'heure de début des cours (le matin)
HEURE_DEBUT = "08:00"

#: Constante donnant l'heure de fin (l'après-midi)
HEURE_FIN = "17:30"

#: Constante donnant les heures des créneaux usuels d'ADE
# (chaque créneau étant de la forme ``"<heure_debut>|<heure_fin>"``
CRENEAUX_POSSIBLES = ["08:00|10:00", "10:00|12:00", "13:30|15:30", "15:30|17:30"]

# Période de cours entre deux vacances scolaires sous la forme d'une liste [debut_periode, fin_periode],
# la fin de la période indiquant la date (du vendredi) au soir à partir duquel débute les vacances)
#: Constante donnant la période pédagogique entre la Rentrée et la Toussaint
PERIODE1 = [DEBUT_ANNEE, "27-10-2023"]
#: Constante donnant la période pédagogique entre la Toussaint et Noël
PERIODE2 = ["06-11-2023", "22-12-2023"]
#: Constante donnant la période pédagogque entre Noël et les vacances d'Hiver
PERIODE3 = ["08-01-2024", "23-02-2024"]
#: Constante donnant la période pédagogique entre les vacances d'Hiver et celles de Printemps
PERIODE4 = ["04-03-2024", "12-04-2024"]
#: Constante donnant la période pédagogique entre les vacances de Printemps et celles d'Eté
PERIODE5 = ["29-04-2024", FIN_ANNEE]

#: Constante donnant la liste de toutes les périodes
PERIODES_SCOLAIRES = [PERIODE1, PERIODE2, PERIODE3, PERIODE4, PERIODE5]

#: Constante donnant les noms des temps marquants de l'année
NOMS_PERIODES = ["Rentrée", "Toussaint", "Noël", "Hiver", "Printemps", "Eté"]

#: Constante donnant les fériés de l'année universitaire
JOURS_FERIES = ["11-11-2022",  # Armistice
                "10-04-2023",  # Lundi de Pâques
                "01-05-2023",  # Fête du travail
                "08-05-2023",  # Victoire 1945
                "18-05-2023",  # Ascension
                "19-05-2023"  # Pont de l'ascension
                ]


# *********************************************************************
#: Constante donnant les évènements (donnant lieu à amphi)
EVENEMENTS = ["Conf CyberSécu WatchGuard",
              "Open Day",
              "Réunion partenariale CFA UGA",
              "Infos BUT1",
              "Galette ENEPS",
              "Journée d'intégration",
              "Réunion de rentrée ENEPS",
              "Info Stage",
              "Info mobilités à l'étranger",
              "Réunion de rentrée BUT2-FI",
              "Infos Semestre2",
              "Réunion de rentrée BUT1",
              "Infos - Stages et PE à l'étranger",
              "Infos Stage",
              "Réunion de rentrée BUT3-FI"]


# *****************************************************************************
#: Les compétences
COMPETENCES = ["RT1-Administrer", "RT2-Connecter", "RT3-Programmer"]

# *****************************************************************************
#: Les UE du S1
UEs_S1 = ["UE1.1-Administrer", "UE1.2-Connecter", "UE1.3-Programmer"]


# *****************************************************************************
#: La matrice des coefficients du S1, où chaque ligne est relative à un
# module, et donne (dans l'ordre), le nom du module, le coefficient dans l'UE1,
# le coefficient dans l'UE2 puis le coefficient dans l'UE3.

COEFFS_S1 = [ ["R101-InitRes", 12, 4, 4],
              ["R102-ArchiRes", 0, 10, 0],
              ["R103-LAN", 8, 6, 0],
              ["R104-Eln", 6, 9, 0],
              ["R105-Lignes", 0, 5, 0],
              ["R106-ArchiInfo", 10, 0, 0],
              ["R107-Python1", 0, 0, 20],
              ["R108-Shell", 4, 0, 10],
              ["R109-TechnoWeb", 0, 0, 8],
              ["R110-Anglais", 3, 5, 4],
              ["R111-ExprCom", 4, 5, 4],
              ["R112-PPP", 0, 0, 0],
              ["R113-MathSignal", 5, 5, 4],
              ["R114-MathTX", 5, 5, 4],
              ["R115-GestProj", 2, 3, 2],
              ["SAÉ101-Hygiène", 16, 6, 0],
              ["SAÉ102-InitRes", 30, 0, 0],
              ["SAÉ103-Trans", 0, 22, 0],
              ["SAÉ104-WebCV", 0, 6, 16],
              ["SAÉ105-Données", 0, 0, 28],
              ["SAÉ1Portfolio", 0, 0, 0]
              ]

# **************************************************************
#: Constante listant les parcours de BUT RT possibles
PARCOURS = ["Cyber", "DevCloud"]

# **************************************************************
#: Constante listant les cursus de BUT RT possibles
CURSUS = ["FI", "FA"]