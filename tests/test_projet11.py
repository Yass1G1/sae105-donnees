import inspect

import pytest

import tools_introspection
import tools_tests

# Import du sphinx_projet
try:
    import projetX
except:
    pass
MODULE = "projet11"


@pytest.mark.echeance4
class TestEstDansCompetenceS1:
    FONCTION = "est_dans_competence_S1"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet11)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètres".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet11)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        res = projet11.est_dans_competence_S1("R101-InitRes", "RT1-Administrer")
        message = "La valeur de retour doit être un boolean"
        assert isinstance(res, bool), tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("module,competence,attendu", [
        pytest.param("R101-InitRes", "RT1-Administrer", True, id="R101 dans RT1"),
        pytest.param("R109-TechnoWeb", "RT1-Administrer", False, id="R109 dans RT1"),
        pytest.param("R113-MathSignal", "RT2-Connecter", True, id="R113 dans RT2"),
        pytest.param("R106-ArchiInfo", "RT3-Programmer", False, id="R106 dans RT3"),
        pytest.param("SAÉ101-Hygiène", "RT1-Administrer", True, id="SAE101 dans RT1"),
        pytest.param("SAÉ101-Hygiène", "RT2-Connecter", True, id="SAE101 dans RT2"),
        pytest.param("SAÉ105-Données", "RT3-Programmer", True,  id="SAE105 dans RT3"),

    ])
    def test_valeur_retour(self, module, competence, attendu):
        resultat = projet11.est_dans_competence_S1(module, competence)
        message = f"""Paramètres testés : 
> module={module}
> competence={competence}
La valeur de retour n'est pas correcte"""
        assert resultat == attendu, tools_tests.affiche_message_erreur(message)



@pytest.mark.echeance4
class TestSelectionneCreneauxGroupeCompetence:
    FONCTION = "selectionne_creneaux_groupe_competence"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet11)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètres".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet11)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        fichier_events = datadir[f"extrait_ade.csv"]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        res = projet11.selectionne_creneaux_groupe_competence(events, "B1G1", "RT1-Administrer")
        message = f"""Paramètre testé: cf {fichier_events}
La valeur de retour doit être de type list"""
        assert isinstance(res, list), tools_tests.affiche_message_erreur(message)
        message = f"""Paramètre testé: cf {fichier_events}
La valeur de retour doit être une liste de str"""
        assert isinstance(res[0], str), tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("groupe,competence,expected", [
        pytest.param("B1G1", "RT1-Administrer", "B1G1_RT1.csv", id="B1G1 et RT1"),
        pytest.param("B1G2", "RT2-Connecter", "B1G2_RT2.csv", id="B1G2 et RT2"),
        pytest.param("B1G4", "RT3-Programmer", "B1G4_RT3.csv", id="B1G4 et RT3"),
    ])
    def test_valeur_retour(self, datadir, groupe, competence, expected):
        fichier_events = datadir["extrait_ade.csv"]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{expected}"])
        resultat = projet11.selectionne_creneaux_groupe_competence(events, groupe, competence)
        message = f"""Paramètres testés: 
> events : cf. {fichier_events}
> groupe={groupe}
> competence={competence}
La valeur de retour n'est pas correcte"""
        assert resultat == attendu, tools_tests.affiche_message_erreur(message)



@pytest.mark.echeance5
class TestNbHeuresParModalite:
    FONCTION = "nb_heures_par_modalite"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet11)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet11)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        fichier_events = datadir[f"extrait_ade1.csv"]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        res = projet11.nb_heures_par_modalite(events)
        message = f"""Paramètre testé: cf {fichier_events}
La valeur de retour doit être de type list"""
        assert isinstance(res, list), tools_tests.affiche_message_erreur(message)
        message = f"""Paramètre testé: cf {fichier_events}
La valeur de retour doit être une liste de 5 éléments"""
        assert len(res) == 5, tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("data,attendu", [
        pytest.param("extrait_ade2.csv", [4.0, 4.0, 11.0, 6.0, 25.0], id="extrait2"),
        pytest.param("extrait_ade1.csv", [2.0, 32.0, 69.0, 14.0, 117.0], id="extrait1"),
    ])
    def test_valeur_retour(self, datadir, data, attendu):
        fichier_events = datadir[data]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        resultat = projet11.nb_heures_par_modalite(events)
        message = f"""Paramètres testés: cf {fichier_events}
La valeur de retour n'est pas correcte"""
        assert resultat == attendu, tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance5
class repartition_moyenne_volume_horaire_competence:
    FONCTION = "nb_heures_par_modalite"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE,
                                                                self.FONCTION)
        liste = inspect.getmembers(projet11)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE,
                                                                     self.FONCTION,
                                                                     1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION,
                                                           projet11)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        fichier_events = datadir[f"extrait_ade1.csv"]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        res = projet11.nb_heures_par_modalite(events)
        message = f"""Paramètre testé: cf {fichier_events}
    La valeur de retour doit être de type list"""
        assert isinstance(res, list), tools_tests.affiche_message_erreur(
            message)
        message = f"""Paramètre testé: cf {fichier_events}
    La valeur de retour doit être une liste de str"""
        assert isinstance(res[0], str), tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("data,competence,attendu", [
        pytest.param("extrait_ade1.csv", "RT1-Administrer", "RT1-Administrer;0.00;1.50;0.50;0.00;2.00",
                     id="extrait1 et RT1"),
        pytest.param("extrait_ade2.csv", "RT1-Administrer", "RT1-Administrer;1.00;3.50;1.50;0.75;6.75",
                     id="extrait2 et RT1"),
        pytest.param("extrait_ade2.csv", "RT3-Programmer", "RT3-Programmer;0.00;3.50;3.00;0.00;6.50",
                     id="extrait2 et RT3"),
    ])
    def test_valeur_retour(self, datadir, data, competence, attendu):
        fichier_events = datadir[data]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        resultat = projet11.repartition_moyenne_volume_horaire_competence(events, competence)
        message = f"""Paramètres testés: 
> events: cf {fichier_events}
> competence={competence}
La valeur de retour n'est pas correcte"""
        assert resultat == attendu, tools_tests.affiche_message_erreur(message)

@pytest.mark.echeance6
class TestTraitement:
    FONCTION = "traitement"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet11)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet11)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["extrait_ade.csv"])
        res = projet11.traitement(events)
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("data,expected", [
        pytest.param("extrait_ade.csv", "extrait_ade_final.csv", id="extrait1"),
        pytest.param("all.csv", "all_final.csv", id="all"),
    ])
    def test_valeur_retour(self, datadir, data, expected):
        fichier_events = datadir[data]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{expected}"])
        resultat = projet11.traitement(events)
        message = f"""Paramètres testés: cf. {fichier_events}
La valeur de retour ne correspond pas"""
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur(message)
