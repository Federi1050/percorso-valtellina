import pytest

from Mezzo import Mezzo, Automobile, Furgone, Moto


# ======================
# TEST CLASSE MEZZO
# ======================

def test_mezzo_valori_validi():
    m = Mezzo(2020, "Fiat", "Diesel", 1600)

    assert m.get_anno_imm() == 2020
    assert m.get_marca() == "Fiat"
    assert m.get_tipo_alim() == "Diesel"
    assert m.get_cilindrata() == 1600


def test_mezzo_valori_non_validi():
    m = Mezzo(1800, "", "", -10)

    assert m.get_anno_imm() == 1901
    assert m.get_marca() == "sconosciuta"
    assert m.get_tipo_alim() == "sconosciuta"
    assert m.get_cilindrata() == 1


# ======================
# TEST CLASSE AUTOMOBILE
# ======================

def test_automobile_valida():
    a = Automobile(2022, "BMW", "Benzina", 2000, 5)

    assert a.get_n_porte() == 5


def test_automobile_porte_non_valide():
    a = Automobile(2022, "BMW", "Benzina", 2000, 1)

    assert a.get_n_porte() == 2


# ======================
# TEST CLASSE FURGONE
# ======================

def test_furgone_valido():
    f = Furgone(2019, "Iveco", "Diesel", 2500, 1200)

    assert f.get_cap_cari() == 1200


def test_furgone_non_valido():
    f = Furgone(2019, "Iveco", "Diesel", 2500, -50)

    assert f.get_cap_cari() == 1


# ======================
# TEST CLASSE MOTO
# ======================

def test_moto_valida():
    m = Moto(2021, "Yamaha", "Benzina", 900, "Sportiva", 4)

    assert m.get_tipologia() == "Sportiva"
    assert m.get_tempi_mot() == 4


def test_moto_non_valida():
    m = Moto(2021, "Yamaha", "Benzina", 900, "", -1)

    assert m.get_tipologia() == "sconosciuta"
    assert m.get_tempi_mot() == 1