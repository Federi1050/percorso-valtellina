class Mezzo:
    def __init__(self, annoImm, marca, tipoAli, cilindrata):
        self.set_anno_imm(annoImm)
        self.set_marca(marca)
        self.set_tipo_ali(tipoAli)
        self.set_cilindrata(cilindrata)

    def set_anno_imm(self, intero):
        if isinstance(intero,int) and intero > 1900:
            self.__anno_imm = intero
        else:
            self.__anno_imm = 1901

    def set_marca(self, stringa):
        if isinstance(stringa,str) and len(stringa) > 0:
            self.__marca = stringa
        else:
            self.__marca = "sconosciuta"

    def set_tipo_ali(self, stringa):
        if isinstance(stringa,str) and len(stringa) > 0:
            self.__tipo_alim = stringa
        else:
            self.__tipo_alim = "sconosciuta"

    def set_cilindrata(self, intero):
        if isinstance(intero,int) and intero > 0:
            self.__cilindrata = intero
        else:
            self.__cilindrata = 1

    def get_anno_imm(self):
        return self.__anno_imm

    def get_marca(self):
        return self.__marca

    def get_tipo_alim(self):
        return self.__tipo_alim

    def get_cilindrata(self):
        return self.__cilindrata
    
    def __str__(self):
        ris = (
            f"anno immatricolazione:{self.__anno_imm}\n"
            f"marca:{self.__marca}\n"
            f"tipo alimentazione:{self.__tipo_alim}\n" 
            f"cilindrata:{self.__cilindrata}\n"
        )
        return ris

class Automobile(Mezzo):
    def __init__(self, annoImm, marca, tipoAli, cilindrata, nporte):
        super().__init__(annoImm, marca, tipoAli, cilindrata)
        self.set_n_porte(nporte)

    def set_n_porte(self, intero):
        if isinstance(intero, int) and intero > 2:
            self.__n_porte = intero
        else:
            self.__n_porte = 2

    def get_n_porte(self):
        return self.__n_porte
    
    def __str__(self):
        return super().__str__() + f"numero porte:{self.__n_porte}\n"

class Furgone(Mezzo):
    def __init__(self, annoImm, marca, tipoAli, cilindrata, capacitaCari):
        super().__init__(annoImm, marca, tipoAli, cilindrata)
        self.set_cap_cari(capacitaCari)

    def set_cap_cari(self, intero):
        if isinstance(intero, int) and intero > 0:
            self.__cap_carico = intero
        else:
            self.__cap_carico = 1

    def get_cap_cari(self):
        return self.__cap_carico
    
    def __str__(self):
        return super().__str__() + f"capacita' carico:{self.__cap_carico}\n"

class Moto(Mezzo):
    def __init__(self, annoImm, marca, tipoAli, cilindrata, tipologia, tMotore):
        super().__init__(annoImm, marca, tipoAli, cilindrata)
        self.set_tipologia(tipologia)
        self.set_tempi_moto(tMotore)

    def set_tipologia(self, stringa):
        if isinstance(stringa,str) and len(stringa) > 0:
            self.__tipologia = stringa
        else:
            self.__tipologia = "sconosciuta"
    
    def set_tempi_moto(self, intero):
        if isinstance(intero, int) and intero > 0:
            self.__tempi_motore = intero
        else:
            self.__tempi_motore = 1

    def get_tipologia(self):
        return self.__tipologia
    
    def get_tempi_mot(self):
        return self.__tempi_motore
    
    def __str__(self):
        ris = super().__str__() + (
            f"tipologia:{self.__tipologia}\n"
            f"tempi motore:{self.__tempi_motore}\n"
        )
        return ris
    
    def get_num_porte(self):
        return 0