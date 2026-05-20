class Dimensione:
    def __init__(self, altezza=1, lunghezza=1, profondita=1):
        self.set_altezza(altezza)
        self.set_lunghezza(lunghezza)
        self.set_profondita(profondita)

    def set_altezza(self, altezza):
        self.__altezza = altezza

    def set_lunghezza(self, lunghezza):
        self.__lunghezza = lunghezza

    def set_profondita(self, profondita):
        self.__profondita = profondita

    def get_altezza(self):
        return self.__altezza

    def get_lunghezza(self):
        return self.__lunghezza

    def get_profondita(self):
        return self.__profondita

    def __str__(self):
        return f"Dimensione(altezza={self.__altezza}, lunghezza={self.__lunghezza}, profondita={self.__profondita})"




class Mobile:
    def __init__(self, materiale = "legno", prezzo = 99, dimensione=None):
        # valori richiesti
        self.set_materiale(materiale)
        self.set_prezzo(prezzo)
        # usa None come default per evitare un'istanza mutabile condivisa
        self.set_dimensione(dimensione if dimensione is not None else Dimensione())

    def set_dimensione(self, dimensione):
        if isinstance(dimensione, Dimensione):
            self.__dimensione = dimensione
        else:
            self.__dimensione = Dimensione()

    def get_dimensione(self):
        return self.__dimensione

    def set_materiale(self, materiale):
        if not isinstance(materiale, str):
            raise TypeError("materiale deve essere una stringa")
        materiale = materiale.strip()
        if materiale == "":
            raise ValueError("materiale non può essere vuoto")
        self.__materiale = materiale

    def get_materiale(self):
        return self.__materiale

    def set_prezzo(self, prezzo):
        try:
            prezzo_val = float(prezzo)
        except (TypeError, ValueError):
            raise TypeError("prezzo deve essere un numero")
        if prezzo_val < 0:
            raise ValueError("prezzo non può essere negativo")
        self.__prezzo = prezzo_val

    def get_prezzo(self):
        return self.__prezzo

    def __repr__(self):
        return (f"Mobile(materiale={self.__materiale!r}, prezzo={self.__prezzo!r}, "
                f"dimensione={self.__dimensione!r})")

    def __str__(self):
        return (f"Materiale: {self.__materiale}, Prezzo: €{self.__prezzo:.2f}, "
                f"Dimensione: {self.__dimensione}")


class Stanza:
  def __init__(self, tipologia = "stanza generica"):
    self.__tipologia = tipologia
    self.__mobili = []

  def add_mobile(self, mobile : Mobile):
    if not isinstance(mobile, Mobile): 
      # lancio un errore
      print("deve inserire un mobile")
      return False
    self.__mobili.append(mobile)
    return True

  def remove_mobile(self , mobile):
    if len(self.__mobili) == 0:
      return None
    
    return self.__mobili.remove(mobile)



  def stampa_mobili(self):
    for mobile in self.__mobili:
      print(mobile)
      print("")
      



stanza = Stanza()
m = Mobile()
stanza.add_mobile( m)
stanza.add_mobile( Mobile())
stanza.add_mobile( Mobile())

stanza.stampa_mobili()

print("##################")
stanza.remove_mobile(m )
stanza.stampa_mobili()