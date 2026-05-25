# costruisci serie funzioni:
#genera dataframe
#series (chiedi num elementi) di numeri random

import pandas as pd
import random

class Pandas_generator:
    def __init__(self):
        pass

    def generate_r_series(self, numero_ele):
        if numero_ele <= 0:
            numero_ele = 1
        serie = []
        for i in range(numero_ele):
            serie.append(random.randint(1,100))
        serie = pd.Series(serie)
        return serie

    def generate_r_dataFrame(self, numero_ele):
        if numero_ele <= 0:
            numero_ele = 1
        data = [
            [random.randint(1,100) for j in range(numero_ele)]
            for i in range(numero_ele)
        ]

        colonne = [f"col_{i}" for i in range(numero_ele)]

        return pd.DataFrame(data, columns=colonne)

