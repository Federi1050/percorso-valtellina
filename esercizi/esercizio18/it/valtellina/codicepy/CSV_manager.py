import csv
import io #visto che nei pacchetti non esterni non devi metterli sul requirement

class CSV_manager():

    def convert_csv_str_in_json(self, stringa):
        stringa = stringa.replace('\\n', '\n')
        stringa = stringa.replace('\r\n', '\n')

        stream = io.StringIO(stringa)
        reader = csv.DictReader(stream)

        result = [row for row in reader]

        # lista dove ogni elemento e' una dict -> riga del csv

        return result

    def set_csv(self, lista):
        if isinstance(lista, list) and len(lista)>0:
            self.__csv_lista = lista
        else:
            self.__csv_lista = []

