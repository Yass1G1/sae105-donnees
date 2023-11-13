import inspect

import pytest

import tools_constantes
import tools_introspection
import tools_tests

# Import du sphinx_projet
try:
    import projet3
except:
    pass
MODULE = "projet3"

@pytest.mark.echeance4
class TestCalculeSemestreModule:
    FONCTION = "calcule_semestre_module"

    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet3)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet3)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet3.calcule_semestre_module("R107-Python1")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("module, attendu", [
        pytest.param("R107-Python1", "S1", id="R107-Python1"),
        pytest.param("R206-Codage", "S2", id="R206-Codage"),
        pytest.param("SAÉ303-MultiSites", "S3", id="SAÉ303-MultiSites"),
        pytest.param("SAÉ4Alternance", "S4", id="SAÉ4Alternance"),
        pytest.param("R5dc09-DevOps", "S5", id="R5dc09-DevOps"),
        pytest.param("SAÉ6cy01-Cyberattaque", "S6", id="SAÉ6cy01-Cyberattaque")
    ])
    def test_valeur_retour(self, module, attendu):
        resultat = projet3.calcule_semestre_module(module)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte")

    def test_valeur_retour_autre(self):
        resultat = projet3.calcule_semestre_module("Autre")
        assert resultat is None, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte lorsque le module est 'Autre'")


@pytest.mark.echeance4
class TestSelectionneCreneauxSalleParSemestre:
    FONCTION = "selectionne_creneaux_salle_par_semestre"

    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet3)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet3)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["quelques_salles.csv"])
        res = projet3.selectionne_creneaux_salle_par_semestre(events, "IUT1_T25 info1", "S1")
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être une liste")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être une liste de chaine de caractères")

    @pytest.mark.parametrize("data, salle, periode, attendu", [
        pytest.param("quelques_salles", "IUT1_T25 info1", "S1", "T25_S1", id="IUT1_T25 info1 S1"),
        pytest.param("quelques_salles", "IUT1_119", "S1", "119_S1", id="IUT1_119 S1"),
        pytest.param("quelques_salles", "IUT1_119", "S3", "119_S3", id="IUT1_119 S3"),
        pytest.param("quelques_salles", "IUT1_119", "S4", "119_S4", id="IUT1_119 S4"),
    ])
    def test_valeur_retour(self, datadir, data, salle, periode, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{attendu}.csv"])
        resultat = projet3.selectionne_creneaux_salle_par_semestre(events, salle, periode)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte")

    def test_valeur_retour_inoccupe(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"quelques_salles.csv"])
        resultat = projet3.selectionne_creneaux_salle_par_semestre(events, "IUT1-AMPHI CHARTREUSE", "S3")
        assert resultat == [], \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte")

    def test_valeur_retour_autre(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"quelques_salles.csv"])
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/autre.csv"])
        resultat = projet3.selectionne_creneaux_salle_par_semestre(events, "IUT1_AMPHI CHARTREUSE", "Autre")
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte")

@pytest.mark.echeance4
class TestFournitListeSalles:
    FONCTION = "fournit_liste_salles"

    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet3)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet3)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet3.fournit_liste_salles("TP")
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("type_salles, attendu", [
            pytest.param('TP', tools_constantes.SALLES_TP_RT, id="TP"),
            pytest.param('TD', tools_constantes.SALLES_TD_RT, id="TD"),
            pytest.param('Amphi', tools_constantes.AMPHI, id="Amphi"),
            pytest.param('Central', tools_constantes.SALLES_BAT_CENTRAL, id="Central"),
        ])
    def test_valeur_retour(self, type_salles, attendu):
        resultat = projet3.fournit_liste_salles(type_salles)
        assert sorted(resultat) == sorted(attendu), \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

    def test_valeur_retour_inexistant(self):
        resultat = projet3.fournit_liste_salles("Sieste")
        assert resultat == [], \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance5
class TestCalculeNbHeuresOccupation:
    FONCTION = "calcule_nb_heures_occupation"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet3)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet3)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["119_S1.csv"])
        res = projet3.calcule_nb_heures_occupation(events)
        assert isinstance(res, float), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type float")

    @pytest.mark.parametrize("data, attendu", [
        pytest.param("119_S1", 4.0, id="119_S1"),
        pytest.param("T25_S1", 7.5, id="119_S1"),
    ])
    def test_valeur_retour(self, datadir, data, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        resultat = projet3.calcule_nb_heures_occupation(events)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte")

    def test_valeur_retour_inoccupee(self, datadir):
        resultat = projet3.calcule_nb_heures_occupation([])
        assert resultat == 0, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte lorsque la salle est inoccupée")

@pytest.mark.echeance5
class TestDecritNbHeuresParSalle:
    FONCTION = "decrit_nb_heures_par_salle"

    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet3)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet3)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["quelques_salles.csv"])
        res = projet3.decrit_nb_heures_par_salle(events, "IUT1_T25 info1")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("data, salle, attendu", [
        pytest.param("quelques_salles", "IUT1_T25 info1", "IUT1_T25 info1;7.50;2.00;4.00;0.00", id="IUT1_T25 info1"),
        pytest.param("all", "IUT1_T22 info2", "IUT1_T22 info2;439.00;140.00;81.00;1.00", id="IUT1_T22 info2"),
    ])
    def test_valeur_retour(self, datadir, data, salle, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        resultat = projet3.decrit_nb_heures_par_salle(events, salle)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour n'est pas correcte")



@pytest.mark.echeance6
class TestTraitement:
    FONCTION = "traitement"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet3)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet3)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["B2G1.csv"])
        res = projet3.traitement(events, "TP")
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("data, type_salles, expected", [
        pytest.param('B2G1.csv', "TP", "B2G1_TP.csv", id="B2G1 TP"),
        pytest.param('B2G1.csv', "Amphi", "B2G1_Amphi.csv", id="B2G1 Amphi"),
        pytest.param('B3cyA.csv', "TP", "B3cyA_TP.csv", id="B3cyA TP"),
        pytest.param('B3cyA.csv', "TD", "B3cyA_TD.csv", id="B3cyA TD"),
        pytest.param('all.csv', "TD", "all_TD.csv", id="all TD"),
    ])
    def test_valeur_retour(self, datadir, data, type_salles, expected):
        fichier_events = datadir[data]
        events = tools_tests.lecture_lignes_fichier_csv(fichier_events)
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{expected}"])
        resultat = projet3.traitement(events, type_salles)
        message = f"""Paramètres testés:
> events: cf. {fichier_events}
> type_salles={type_salles}
La valeur de retour ne correspond pas"""
        assert sorted(resultat) == sorted(attendu), \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")
        message = f"""Paramètres testés:
> events: cf. {fichier_events}
> type_salles={type_salles}
La valeur de retour doit faire état des salles dans le même ordre celui donné par la constante
les décrivant. """
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


