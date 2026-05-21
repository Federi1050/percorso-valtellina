import pytest
from esercizio14 import *

def test_saluta(capsys):
    saluta("Luca")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Benvenuto Luca"


def test_somma():
    assert somma(2, 3) == 5
    assert somma(-1, 1) == 0


def test_massimo():
    assert massimo(10, 5) == 10
    assert massimo(2, 8) == 8
    assert massimo(4, 4) == 4


def test_pari_o_dispari():
    assert pai_o_dispari(4) == "Pari"
    assert pai_o_dispari(7) == "Dispari"


def test_area_rettangolo():
    assert area_reattangolo(5, 2) == 10
    assert area_reattangolo(0, 4) == 0


def test_celsius_fahrenheit():
    assert celsius_fahrenheit(0) == 32
    assert celsius_fahrenheit(100) == 212


def test_conta_lettere():
    assert conta_lettere("ciao") == 4
    assert conta_lettere("") == 0


def test_quadrato():
    assert quadrato(4) == 16
    assert quadrato(-3) == 9


def test_media():
    assert media(3, 3, 3) == 3
    assert media(1, 2, 3) == 2


def test_inverti_stringa():
    assert inverti_stringa("ciao") == "oaic"
    assert inverti_stringa("") == ""


def test_fattoriale():
    assert fattoriale(0) == 1
    assert fattoriale(1) == 1
    assert fattoriale(3) == 6
    assert fattoriale(5) == 120


def test_conta_vocali():
    assert conta_vocali("ciao") == 3
    assert conta_vocali("python") == 1
    assert conta_vocali("") == 0


def test_numero_primo():
    assert numero_primo(3) is True
    assert numero_primo(9) is False
    assert numero_primo(1) is False
    assert numero_primo(2) is False
    assert numero_primo(10) is False

def test_somma_lista():
    assert somma_lista([1, 2, 3, 4]) == 10
    assert somma_lista([]) == 0
    assert somma_lista([-1, 1]) == 0


def test_massimo_lista():
    assert massimo_lista([1, 5, 3]) == 5
    assert massimo_lista([-10, -2, -30]) == -2
    assert massimo_lista([7]) == 7


def test_minimo_lista():
    assert minimo_lista([1, 5, 3]) == 1
    assert minimo_lista([-10, -2, -30]) == -30
    assert minimo_lista([7]) == 7


def test_palindroma():
    assert palindroma("anna") is True
    assert palindroma("ciao") is False
    assert palindroma("radar") is True
    assert palindroma("") is True
    assert palindroma("a") is True


def test_moltiplica_lista():
    assert moltiplica_lista([1, 2, 3, 4]) == 24
    assert moltiplica_lista([5]) == 5
    assert moltiplica_lista([]) == 1  # comportamento attuale della tua funzione


def test_conta_pari():
    assert conta_pari([1, 2, 3, 4, 6]) == 3
    assert conta_pari([1, 3, 5]) == 0
    assert conta_pari([2, 4, 6, 8]) == 4


def test_tabellina(capsys):
    tabellina(2)
    captured = capsys.readouterr()

    output = captured.out.strip().split("\n")

    expected = [str(i * 2) for i in range(1, 10)]

    assert output == expected