import importlib
import inspect
import os
import sys

import mock
import pytest

import tools_introspection
import tools_tests


def import_projet():
    MODULE = "projetX"
    try:
        import projetX as projet
    except:
        sys.path.insert(0, os.path.abspath('.'))
        projet = None
        for i in range(1, 30):
            try:
                projet = importlib.import_module(f"projet{i}")
                MODULE = f"projet{i}"
                return projet, MODULE
            except:
                pass
    return projet, MODULE


projet, MODULE = import_projet()


# ************************************************************************************************
class TestStructure:

    def test_import_module(self):
        """Le module contient-il des erreurs de syntaxes ?"""
        try:
            projet, MODULE = import_projet()
            print(projet)
        except:
            message = """
Votre projet n'a pas pu être importé pour les tests
➔ Vérifiez l'orthographe du nom du script ou sa place dans l'arborescence...
➔ Vérifiez que votre code n'a pas d'erreurs syntaxiques (vaguettes rouges)
"""
            assert False, tools_tests.affiche_message_erreur(message)

    # ---
    def test_declaration_main(self):
        """Le module a-t-il un main ?"""
        FONCTION = "main"
        message = "Le programme principal {}.{} doit être déclaré".format(MODULE, FONCTION)
        liste = inspect.getmembers(projet)
        assert FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance1
class TestCalculeNombreMinutes:
    FONCTION = "calcule_nombre_minutes"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.calcule_nombre_minutes("17:30")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")

    @pytest.mark.parametrize("heure, nb_minutes", [
        pytest.param("00:30", 30),
        pytest.param("01:00", 60),
        pytest.param("01:05", 65),
        pytest.param("02:30", 150),
    ])
    def test_valeur_retour(self, heure, nb_minutes):
        resultat = projet.calcule_nombre_minutes(heure)
        assert resultat == nb_minutes, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance1
class TestCalculeDuree:
    FONCTION = "calcule_duree"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.calcule_duree("17:30", "18:00")
        assert isinstance(res, str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type str")

    @pytest.mark.parametrize("heure_debut, heure_fin, duree", [
        pytest.param("15:30", "17:30", "02:00"),
        pytest.param("08:30", "12:00", "03:30"),
        pytest.param("08:00", "09:00", "01:00"),
        pytest.param("15:30", "16:00", "00:30"),
    ])
    def test_valeur_retour(self, heure_debut, heure_fin, duree):
        resultat = projet.calcule_duree(heure_debut, heure_fin)
        assert resultat == duree, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance2
class TestCompareDates:
    FONCTION = "compare_dates"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.compare_dates("01-01-2021", "02-01-2021")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")

    @pytest.mark.parametrize("date1, date2, attendu", [
        pytest.param("01-01-2021", "01-01-2022", -1),
        pytest.param("05-11-2023", "04-01-2023", 1),
        pytest.param("01-01-2022", "01-01-2021", 1),
        pytest.param("01-01-2021", "01-02-2021", -1),
        pytest.param("01-02-2021", "01-01-2021", 1),
        pytest.param("01-01-2021", "10-01-2021", -1),
        pytest.param("10-01-2021", "01-01-2021", 1),
        pytest.param("01-01-2021", "01-01-2021", 0),
        pytest.param("05-11-2023", "05-11-2023", 0),
    ])
    def test_valeur_retour(self, date1, date2, attendu):
        resultat = projet.compare_dates(date1, date2)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance2
class TestCompareHeures:
    FONCTION = "compare_heures"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet.compare_heures("11:00", "12:00")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")

    @pytest.mark.parametrize("heure1, heure2, attendu", [
        pytest.param("11:00", "11:00", 0),
        pytest.param("12:00", "10:00", 1),
        pytest.param("11:00", "12:00", -1),
        pytest.param("13:30", "09:45", 1),
        pytest.param("10:50", "23:10", -1),
        pytest.param("09:33", "09:33", 0)
    ])
    def test_valeur_retour(self, heure1, heure2, attendu):
        resultat = projet.compare_heures(heure1, heure2)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance2
class TestEstDateDansIntervalle:
    FONCTION = "est_date_dans_intervalle"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 3)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        res = projet.est_date_dans_intervalle("15-01-2021", "01-01-2021", "21-01-2021")
        assert isinstance(res, bool), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type bool")

    @pytest.mark.parametrize("date, resultat", [
        pytest.param("15-01-2021", True),
        pytest.param("15-12-2020", False),
        pytest.param("10-02-2021", False),
        pytest.param("15-01-2022", False)
    ])
    def test_valeur_retour(self, date, resultat):
        actual = projet.est_date_dans_intervalle(date, "01-01-2021", "31-01-2021")
        assert actual == resultat, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

    def test_appel_compare_date(self):
        with mock.patch(f"{MODULE}.compare_dates", return_value=1) as mocked:
            projet.est_date_dans_intervalle("15-01-2021", "01-01-2021", "21-01-2021")
            mocked.assert_called()


@pytest.mark.echeance3
class TestRecupereChampCsv:
    FONCTION = "recupere_champ_csv"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("champ, evenement, expected", [
        pytest.param("uid",
                     "ADE000087F;26-04-2023;13:30|17:30;R401-InfraSec;TP;;InfraSéc;IUT1_T33 res1;DESPINASSE BRUNO|VEDEL FRANCK;B2GA",
                     "ADE000087F", id="uid"),
        pytest.param("modules",
                     "ADE00005BB;11-10-2023;13:30|17:30;SAÉ3cy04-Pentesting|SAÉ3dc04-InfraVirtu;Proj;;;IUT1_T27 res3;LUBINEAU DENIS|VEDEL FRANCK;B2G1",
                     "SAÉ3cy04-Pentesting|SAÉ3dc04-InfraVirtu", id="modules"),
        pytest.param("salles",
                     "ADE00005BB;11-10-2023;13:30|17:30;SAÉ3cy04-Pentesting|SAÉ3dc04-InfraVirtu;Proj;;;IUT1_T27 res3;LUBINEAU DENIS|VEDEL FRANCK;B2G1",
                     "IUT1_T27 res3", id="salles"),
        pytest.param("profs",
                     "ADE00005BB;11-10-2023;13:30|17:30;SAÉ3cy04-Pentesting|SAÉ3dc04-InfraVirtu;Proj;;;IUT1_T27 res3;LUBINEAU DENIS|VEDEL FRANCK;B2G1",
                     "LUBINEAU DENIS|VEDEL FRANCK", id="profs"),
        pytest.param("groupes",
                     "ADE000062A;12-10-2022;10:15|11:45;R305-TransNum1;CM;DS;TransAnalogique;IUT1_C201|IUT1_C215;;B2G1|B2G2",
                     "B2G1|B2G2", id="groupes"),
        pytest.param("theme",
                     "ADE000072B;12-10-2022;11:45|12:15;Autre;CM;DS;1/3 temps;IUT1_C201;;B2G1|B2G2",
                     "1/3 temps", id="theme"),
        pytest.param("debut",
                     "ADE000072B;12-10-2022;11:45|12:15;Autre;CM;DS;1/3 temps;IUT1_C201;;B2G1|B2G2",
                     "11:45", id="debut"),
        pytest.param("fin",
                     "ADE000072B;12-10-2022;11:45|12:15;Autre;CM;DS;1/3 temps;IUT1_C201;;B2G1|B2G2",
                     "12:15", id="fin"),
    ])
    def test_valeur_retour(self, champ, evenement, expected):
        res = projet.recupere_champ_csv(evenement, champ)
        assert res == expected, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

    def test_valeur_retour_champ_inexistant(self):
        evenement = "ADE00005BB;11-10-2022;13:30|17:30;SAÉ3cy04-Pentesting|SAÉ3dc04-InfraVirtu;Proj;;;IUT1_T27 res3;LUBINEAU DENIS|VEDEL FRANCK;B2G1"
        res = projet.recupere_champ_csv(evenement, "toto")
        assert res is None, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance3
class TestSelectionneSAE105Groupe:
    FONCTION = "selectionne_SAE105_groupe"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE,
                                                                self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètres".format(MODULE,
                                                                     self.FONCTION,
                                                                     2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION,
                                                           projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    def test_type_valeur_retour(self, datadir):
        """Teste le type de la valeur de retour"""
        fichier_calendrier = datadir["quelques_evenements.csv"]
        calendrier = tools_tests.lecture_lignes_fichier_csv(fichier_calendrier)
        res = projet.selectionne_SAE105_groupe(calendrier, "B1G1")
        message = "La valeur de retour doit être une liste"
        assert isinstance(res, list), tools_tests.affiche_message_erreur(message)
        message = "La valeur de retour doit être une liste de str"
        assert len(res)>0 and isinstance(res[0], str), tools_tests.affiche_message_erreur(message)


    @pytest.mark.parametrize("data,groupe,expected", [
        pytest.param( "quelques_evenements.csv", "B1G1", "B1G1.csv", id="extrait et B1G1"),
        pytest.param( "quelques_evenements.csv", "B1G2", "B1G2.csv", id="extrait et B1G2"),
        pytest.param("all.csv", "B1G4", "B1G4.csv", id="tous et B3cy1")
    ])
    def test_valeur_retour(self, datadir, data, groupe, expected):
        fichier_calendrier = datadir[data]
        calendrier = tools_tests.lecture_lignes_fichier_csv(fichier_calendrier)
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{expected}" ])
        res = projet.selectionne_SAE105_groupe(calendrier, groupe)
        message = f"""Paramètres testés: 
> calendrier: cf. {fichier_calendrier}
> groupe: {groupe}
La valeur de retour n'est pas correcte
"""
        assert sorted(res) == sorted(attendu), tools_tests.affiche_message_erreur(message)
        message = f"""Paramètres testés: 
> calendrier: cf. {fichier_calendrier}
> groupe: {groupe}
La valeur de retour doit être triée par ordre de ressources
"""
        assert res == attendu, tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance6
class TestExportMarkdown:
    FONCTION = "export_markdown"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance7
class TestExportPng:
    FONCTION = "export_png"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance3
class TestDeduitAnneeDuModule:
    FONCTION = "deduit_annee_du_module"

    # ---
    def test_declaration_fonction(self):
        liste = inspect.getmembers(projet)
        message = "La fonction {}.{} doit être déclarée".format(MODULE,
                                                                self.FONCTION)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)


    def test_type_valeur_retour(self):
        res = projet.deduit_annee_du_module("R101")
        message = "Le type renvoyé doit être un int"
        assert isinstance(res, int), tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("module, attendu", [
        pytest.param("R101-InitRes", 1, id="R101-InitRes"),
        pytest.param("R206-Codage", 1, id="R206-Codage"),
        pytest.param("SAÉ103-Trans", 1, id="SAÉ103-Trans"),
        pytest.param("SAÉ2Portfolio", 1, id="SAÉ2Portfolio"),
        pytest.param("R304-Annuaires", 2, id="R304-Annuaires"),
        pytest.param("SAÉ4cy01-Secure", 2, id="SAÉ4cy01-Secure"),
        pytest.param("SAÉ5Alternance", 3, id="SAÉ5Alternance"),
        pytest.param("R504-ProjInf", 3, id="R504-ProjInf"),
        pytest.param("R6dc04-Cloud", 3, id="R6dc04-Cloud"),
        pytest.param("SAÉ6dc01-Pipeline", 3, id="SAÉ6dc01-Pipeline")
    ])
    def test_valeur_retour(self, module, attendu):
        res = projet.deduit_annee_du_module(module)
        message = f"""Paramètre testé: module={module}
La valeur de retour ne correspond pas"""
        assert res == attendu, tools_tests.affiche_message_erreur(message)


    def test_valeur_retour_si_Autre(self):
        res = projet.deduit_annee_du_module("Autre")
        message = f"""Paramètre testé: module=Autre
    La valeur de retour ne correspond pas"""
        assert res == None, tools_tests.affiche_message_erreur(message)


@pytest.mark.echeance3
class TestDeduitAnneeDuGroupe:
    FONCTION = "deduit_annee_du_groupe"

    # ---
    def test_declaration_fonction(self):
        liste = inspect.getmembers(projet)
        message = "La fonction {}.{} doit être déclarée".format(MODULE,
                                                                self.FONCTION)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)


    def test_type_valeur_retour(self):
        res = projet.deduit_annee_du_groupe("B1G1")
        message = "Le type renvoyé doit être un int"
        assert isinstance(res, int), tools_tests.affiche_message_erreur(message)

    @pytest.mark.parametrize("groupe, attendu", [
        pytest.param("B1G1", 1, id="B1G1"),
        pytest.param("B1G4", 1, id="B1G1"),
        pytest.param("B2GA", 2, id="B2GA"),
        pytest.param("B3cy1", 3, id="B3cy1"),
        pytest.param("B3dcC", 3, id="B3dcC")
    ])
    def test_valeur_retour(self, groupe, attendu):
        res = projet.deduit_annee_du_groupe(groupe)
        message = f"""Paramètre testé: groupe={groupe}
La valeur de retour ne correspond pas"""
        assert res == attendu, tools_tests.affiche_message_erreur(message)
