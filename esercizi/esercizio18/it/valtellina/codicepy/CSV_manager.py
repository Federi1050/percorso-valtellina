import csv
import io #visto che nei pacchetti non esterni non devi metterli sul requirement
import pandas as pd

class CSV_manager():

    def __init__(self):
        self.__csv_lista = []

    def convert_csv_str_in_json(self, stringa):
        try:
            if not isinstance(stringa, str):
                return {
                    "success": False,
                    "errore": "Input non valido"
                }

            stringa = stringa.replace('\\n', '\n')
            stringa = stringa.replace('\r\n', '\n')

            stream = io.StringIO(stringa)
            reader = csv.DictReader(stream)
            result = [row for row in reader]

            risult_set = self.set_csv(result)
            # lista dove ogni elemento e' una dict -> riga del csv

            if risult_set.get("success") == False:
                return risult_set

            return {
                "success": True,
                "data": result
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def set_csv(self, lista):
        try:
            if not isinstance(lista, list):
                return {
                    "success": False,
                    "errore": "Il parametro deve essere una lista"
                }

            self.__csv_lista = lista
            return {
                "success": True
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def mostra_csv(self):
        try:
            df = self.__get_dataframe()
            if df is None:
                return {
                    "success": False,
                    "errore": "Tabella vuota"
                }

            return {
                "success": True,
                "data": df.to_dict(orient="records")
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def get_head(self):
        # ritorna prime 5 righe tabella
        try:
            df = self.__get_dataframe()
            if df is None:
                return {
                    "success": False,
                    "errore": "Tabella vuota"
                }

            return {
                "success": True,
                "data": df.head(5).to_dict(orient="records")
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def get_tail(self):
        # ritorna ultime 5 righe tabella
        try:
            df = self.__get_dataframe()
            if df is None:
                return {
                    "success": False,
                    "errore": "Tabella vuota"
                }

            return {
                "success": True,
                "data": df.tail(5).to_dict(orient="records")
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def get_dimensioni(self):
        # ritornra dimensioni tabella
        try:
            df = self.__get_dataframe()
            if df is None:
                return {
                    "success": False,
                    "errore": "Tabella vuota"
                }

            righe, colonne = df.shape
            return {
                "success": True,
                "righe": int(righe),
                "colonne": int(colonne)
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def get_info(self):
        #ritorna tutti gli attributi della tabella e il loro tipo
        try:
            df = self.__get_dataframe()
            if df is None:
                return {
                    "success": False,
                    "errore": "Tabella vuota"
                }

            colonne = []
            for colonna in df.columns:
                colonne.append({
                    "attributo": colonna,
                    "tipo": str(df[colonna].dtype)
                })
            return {
                "success": True,
                "colonne": colonne
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def ricerca(self, attributo, filtro):
        # ricerca nella tabella se c è un attributo attributo
        # ritorna tutte le righe con quel attributo settato a filtro
        try:
            df = self.__get_dataframe()
            if df is None:
                return {
                    "success": False,
                    "errore": "Tabella vuota"
                }

            if attributo not in df.columns:
                return {
                    "success": False,
                    "errore": f"Attributo '{attributo}' non trovato"
                }

            risultato = df[
                df[attributo].astype(str) == str(filtro)
                ]
            return {
                "success": True,
                "totale_risultati": int(len(risultato)),
                "data": risultato.to_dict(orient="records")
            }

        except Exception as e:
            return {
                "success": False,
                "errore": str(e)
            }

    def __get_dataframe(self):
        if len(self.__csv_lista) == 0:
            return None
        return pd.DataFrame(self.__csv_lista)