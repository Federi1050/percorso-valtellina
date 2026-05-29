import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

class DataFrameManager:
    def __init__(self):
        self.__df = None

    def __str__(self):
        return str(self.__df)

    def caricare_dataset(self):
        # fetch dataset
        adult = fetch_ucirepo(id=2)

        # data (as pandas dataframes)
        X = adult.data.features
        y = adult.data.targets

        # metadata
        # print("metadata:")
        # print(adult.metadata)

        # variable information
        # print("variables:")
        # print(adult.variables)

        self.__df = pd.concat([X, y], axis=1)

    def informazioni_dataset(self):
        print(self.__df.shape)
        print(self.__df.head())
        print(self.__df.describe())
        print(self.__df.info())

        print("valori unici")
        print(self.__df["workclass"].value_counts()) # 8 + ?
        print(self.__df["education"].value_counts()) # 16 + ?
        print(self.__df["marital-status"].value_counts())
        print(self.__df["occupation"].value_counts()) # 7 + ?
        print(self.__df["relationship"].value_counts()) # 6 + ?
        print(self.__df["race"].value_counts()) # 5 + ?
        print(self.__df["sex"].value_counts()) # 2 + ?
        print(self.__df["native-country"].value_counts()) # 41 + ?
        print(self.__df["income"].value_counts()) # 2 + ?


    def gestione_valori_strani(self):
        # elimino duplicati
        self.__df.drop_duplicates()

        self.clean_age()
        self.clean_workclass()
        self.clean_fnlwgt()
        self.clean_education()
        self.clean_education_num()
        self.clean_marital_status()
        self.clean_occupation()
        self.clean_relationship()
        self.clean_race()
        self.clean_sex()
        self.clean_capital_gain()
        self.clean_capital_loss()
        self.clean_hours_per_week()
        self.clean_native_country()
        self.clean_income()


    def clean_age(self):
        self.__df["age"] = pd.to_numeric(self.__df["age"], errors="coerce")
        mask = (self.__df["age"] <= 0) | (self.__df["age"] > 122)
        self.__df.loc[mask, "age"] = np.nan

        if self.__df["age"].notna().any():
            self.__df["age"] = self.__df["age"].fillna(self.__df["age"].median())

    def clean_workclass(self):
        self.__df["workclass"] = self.__df["workclass"].str.lower().str.strip()
        self.__df["workclass"] = self.__df["workclass"].replace("?", np.nan)
        if self.__df["workclass"].notna().any():
            self.__df["workclass"] = self.__df["workclass"].fillna("unknown")

    def clean_fnlwgt(self):
        # peso statisctico del campione, indica quante persone della pop rappresenta
        # la eliminamo
        self.__df = self.__df.drop("fnlwgt", axis=1)

    def clean_education(self):
        self.__df["education"] = self.__df["education"].str.lower().str.strip()
        self.__df["education"] = self.__df["education"].replace("?", np.nan)
        if self.__df["education"].notna().any():
            self.__df["education"] = self.__df["education"].fillna("unknown")

    def clean_education_num(self):
        # educazione sotto forma di num
        # ridondante
        self.__df = self.__df.drop("education-num", axis=1)

    def clean_marital_status(self):
        self.__df["marital-status"] = self.__df["marital-status"].str.lower().str.strip()
        self.__df["marital-status"] = self.__df["marital-status"].replace("?", np.nan)
        if self.__df["marital-status"].notna().any():
            self.__df["marital-status"] = self.__df["marital-status"].fillna("unknown")

    def clean_occupation(self):
        self.__df["occupation"] = self.__df["occupation"].str.lower().str.strip()
        self.__df["occupation"] = self.__df["occupation"].replace("?", np.nan)
        if self.__df["occupation"].notna().any():
            self.__df["occupation"] = self.__df["occupation"].fillna("unknown")

    def clean_relationship(self):
        self.__df["relationship"] = self.__df["relationship"].str.lower().str.strip()
        self.__df["relationship"] = self.__df["relationship"].replace("?", np.nan)
        if self.__df["relationship"].notna().any():
            self.__df["relationship"] = self.__df["relationship"].fillna("unknown")

    def clean_race(self):
        self.__df["race"] = self.__df["race"].str.lower().str.strip()
        self.__df["race"] = self.__df["race"].replace("?", np.nan)
        if self.__df["race"].notna().any():
            self.__df["race"] = self.__df["race"].fillna("unknown")

    def clean_sex(self):
        self.__df["sex"] = self.__df["sex"].str.lower().str.strip()
        self.__df["sex"] = self.__df["sex"].replace("?", np.nan)
        if self.__df["sex"].notna().any():
            self.__df["sex"] = self.__df["sex"].fillna("unknown")

    def clean_capital_gain(self):
        self.__df["capital-gain"] = pd.to_numeric(self.__df["capital-gain"], errors="coerce")
        mask = (self.__df["capital-gain"] < 0)
        self.__df.loc[mask, "capital-gain"] = np.nan

        if self.__df["capital-gain"].notna().any():
            self.__df["capital-gain"] = self.__df["capital-gain"].fillna(0)

    def clean_capital_loss(self):
        self.__df["capital-loss"] = pd.to_numeric(self.__df["capital-loss"], errors="coerce")
        mask = (self.__df["capital-loss"] < 0)
        self.__df.loc[mask, "capital-loss"] = np.nan

        if self.__df["capital-loss"].notna().any():
            self.__df["capital-loss"] = self.__df["capital-loss"].fillna(0)

    def clean_hours_per_week(self):
        self.__df["hours-per-week"] = pd.to_numeric(self.__df["hours-per-week"], errors="coerce")
        mask = (self.__df["hours-per-week"] <= 0) | (self.__df["hours-per-week"] > 100)
        self.__df.loc[mask, "hours-per-week"].clip(1,100)

    def clean_native_country(self):
        self.__df["native-country"] = self.__df["native-country"].str.lower().str.strip()
        self.__df["native-country"] = self.__df["native-country"].replace("?", np.nan)
        if self.__df["native-country"].notna().any():
            self.__df["native-country"] = self.__df["native-country"].fillna("unknown")

    def clean_income(self):
        self.__df["income"] = self.__df["income"].str.strip()
        self.__df["income"] = self.__df["income"].replace({
            ">50K." : ">50",
            "<=50K." : "<=50"
        })
        self.__df["income"] = self.__df["income"].replace("?", np.nan)
        if self.__df["income"].notna().any():
            self.__df["income"] = self.__df["income"].fillna("unknown")


    # ----------------------- VECCHIO CODICE ---------------------------------------

    def individua_valori(self):
        # vediamo caratteri strani inseriti
        # colonne scelte guardando il sito che specifica se ci sono mancanze
        ric1 = self.__df["workclass"].value_counts()
        ric2 = self.__df["occupation"].value_counts()
        ric3 = self.__df["native-country"].value_counts()
        print(ric1)
        print(ric2)
        print(ric3)

        ric4 = self.__df["age"]

    def individua_buchi(self):
        # sostituiamo caratteri strani con Nan usando numpy
        self.__df = self.__df.replace("?", np.nan)

        # tutte righe con almeno 1 valore NaN
        df_risposta = self.__df[self.__df.isnull().any(axis=1)]

        return {
            "numero_righe": len(df_risposta),
            "dati": df_risposta
        }

    def gestione_buchi(self):
        # sostituisco tutti i NaN con unknown per le colonne indicare
        self.__df = self.__df[["workclass", "occupation", "native-country"]] = self.__df[["workclass", "occupation", "native-country"]].fillna("unknown")

        # controllo che l eta sia compresa tra 0 a 122
        self.__df = self.__df.replace("?", np.nan)