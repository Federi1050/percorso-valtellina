import pytest

from Mezzo import Mezzo
from Garage import Garage


# ======================
# TEST CREAZIONE GARAGE
# ======================

def test_creazione_garage():
    g = Garage()

    assert g is not None


# ======================
# TEST IMMISSIONE
# ======================

def test_immissione_valida():
    g = Garage()
    m = Mezzo(2020, "Fiat", "Diesel", 1600)

    posizione = g.immissione(m)

    assert posizione == 0


def test_immissione_doppia():
    g = Garage()
    m = Mezzo(2020, "Fiat", "Diesel", 1600)

    g.immissione(m)
    posizione = g.immissione(m)

    assert posizione == -1


def test_immissione_oggetto_non_mezzo():
    g = Garage()

    posizione = g.immissione("auto")

    assert posizione == -1


# ======================
# TEST GARAGE PIENO
# ======================

def test_garage_pieno():
    g = Garage()

    for i in range(15):
        m = Mezzo(2000 + i, f"Marca{i}", "Diesel", 1000 + i)
        g.immissione(m)

    nuovo_mezzo = Mezzo(2025, "BMW", "Benzina", 2000)

    posizione = g.immissione(nuovo_mezzo)

    assert posizione == -1


# ======================
# TEST ESTRAZIONE
# ======================

def test_estrazione_valida():
    g = Garage()
    m = Mezzo(2020, "Fiat", "Diesel", 1600)

    g.immissione(m)

    estratto = g.estrazione(0)

    assert estratto == m


def test_estrazione_non_valida():
    g = Garage()

    estratto = g.estrazione(0)

    assert estratto is None