import pandas as pd

# servono ultimpo punto
def aggiungi_seniority(df):
    df = df.copy()
    df["seniority"] = df["eta"]>30
    return df

def normalizza(df):
    df = df.copy()
    df["eta_norm"] = (df["eta"]-df["eta"].min())/(df["eta"].max()-df["eta"].min())
    return df

print("crea dataframe")
df_or = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco"],
    "eta": [23,31,27],
    "citta": ["Milano","Roma","Torino"]
})
print(df_or)
print("######################")

print("leggi csv")
df = pd.read_csv('dataframe_esempio.csv')
print(df.head())
print("######################")

print("visualizza info + shape")
# df.info(verbose=True)
print(df.shape)
print("######################")

print("seleziona colonna eta e calcola media min max")
stats = df["eta"].agg(["mean","min","max"])
print(stats)
print("######################")

print("rinomina colonna citta in city")
df = df.rename(columns={"citta":"city"})
print(df)
print("######################")

print("aggiungi colonna seniority dinamicamente")
df["seniority"] = df["eta"] > 30
print(df)
print("######################")

print("elimina colonna seniority")
df = df.drop(columns=["seniority"])
print(df)
df["seniority"] = df["eta"] > 30 # serve per un passo dopo
print("######################")

print("set index nome")
print("teniamo commentato in modo che non venga rinominato index")
# df = df.set_index("nome")
print(df)
print("######################")

print("salva dataframe su csv")
df.to_csv("risultato.csv", index=False)
print("######################")

print("serie con indice personalizzato")
dati = [10,20,30,40,50,60,70,80,90,100]
s = pd.Series(dati, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(s)
print("######################")

print("filtra righe eta > 28")
print(df[df["eta"] > 28])
print("######################")

print("filtra citta mialno o roma")
print(df[(df["city"] == 'Milano') | (df["city"] == 'Roma')])
print("######################")

print("filtra eta tra un range")
s = df.query("eta>25 and eta<35")
print(s)
print("######################")

print("seleziona 2 colonna con loc, primi 2 elem")
s = df.loc[:3, ["nome","eta"]]
print(s)
print("######################")

print("seleziona ultime 2 righe con iloc")
s = df.iloc[df.index[-2:],[0]]
print(s)
print("######################")

print("righe dove nome contiene 'a'")
s = df.query("nome.str.contains('a',case=False,na=False)",engine='python')
print(s)
print("######################")

print("prendi 2 eta maggiore")
s = df.nlargest(2,"eta")
print(s)
print("######################")

print("solo eta non nulli")
s = df[df["eta"].notna()]
print(s)
print("######################")

print("query eta > 25 e citta = Roma")
s = df.query("eta > 25 and city == 'Roma'")
print(s)
print("######################")

print("no citta Roma -> meglio farlo con != che con ~")
s = df.query("~(city == 'Roma')")
print(s)
print("######################")

print("eta media per citta")
s = df.groupby("city")["eta"].mean()
print(s)
print("######################")

print("conteggio persone per citta")
s = df.groupby("city").count()
print(s)
print("######################")

print("su eta e citta calcola media min max")
print("fuso es 23 24")
s = df.groupby("city")["eta"].agg(["mean","min","max"])
print(s)
print("#####################")

print("aggiungi con trasform")
df["eta_media-citta"] = df.groupby("city")["eta"].transform("mean")
print(df)
print("######################")

print("nome persona + giovane per eta")
s = df.loc[df.groupby("city")["eta"].idxmin()]
print(s)
print("######################")

print("fai funzione personalizzata")
s = df.groupby("city").apply(
    lambda x: x["eta"].max() - x["eta"].min()
)
print(s)
print("######################")

print("pivot tabella")
pivot = pd.pivot_table(df, index="city", values="eta", aggfunc="mean")
print(pivot)
print("######################")

print("ordina tabella per eta + utilizzo cumsum")
df_ordinato = df.sort_values("eta")
df_ordinato["eta_comul"] = df_ordinato["eta"].cumsum()
print(df_ordinato)
print("######################")

print("groupby con più colonne")
s = df.groupby(["city", "seniority"]).size()
print(s)
print("######################")

print("innser join")
df1 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["Anna", "Luca", "Marco", "Giulia"]
})
df2 = pd.DataFrame({
    "id": [3, 4, 5, 6],
    "nome": ["Marco", "Giulia", "Paolo", "Elena"]
})
df_merged = pd.merge(df2, df1, on="id", how="inner")
print(df_merged)
print("######################")

print("left join + identifica righe no corr")
df_merged = pd.merge(df1, df2, on="id", how="left")
print(df_merged)
senza_match = df_merged["nome_y"].isna()
print(senza_match)
print("######################")

print("concatena 2 dataframe")
df_concat = pd.concat([df1, df2])
print(df_concat)
print("######################")

print("trasforma in formato long")
df_long = pd.melt(df,
                  id_vars=["nome"],
                  var_name = "variabile",
                  value_name = "valore")
print(df_long)
print("######################")

print("trasforma in formato wide")
df_wide = df_long.pivot(
                  index=["nome"],
                  columns = "variabile",
                  values = "valore")
print(df_wide)
print("######################")

print("dataframe stacked")
df_stacked = df.stack()
print(df_stacked)
print("######################")

print("unstack un dataframe")
df_unstack = df_stacked.unstack()
print(df_unstack)
print("######################")

print("facciamo esplodere")
df_unexploded = pd.DataFrame({
    "nome": ["Anna", "Luca"],
    "hobby": [["calcio","pittura"],["musica"]]
})
print(df_unexploded)
df_exploded = df_unexploded.explode("hobby")
print(df_exploded)
print("######################")

print("cross join tra 2 dataframe")
df1 = pd.DataFrame({"nome": ["Anna", "Luca"]})
df2 = pd.DataFrame({"città": ["Roma", "Milano"]})
df_cross = df1.merge(df2, how="cross")
print(df_cross)
print("######################")

print("riorganizza colonne")
# al posto di mettere nome come primas colonna mettiamo citta
# nome è gia prima
df_riordinata = df[["city"] + [col for col in df.columns if col != "city"]]
print(df_riordinata)
print("######################")

print("individua e conta val None")
df_null = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Giulia"],
    "citta": ["Milano",None, "Torino", None],
    "eta": [None, 77, None, 67]
})
null_counts = df_null.isna().sum()
print(null_counts)
print("######################")

print("riempi i valori None")
df_null["eta"] = df_null["eta"].fillna(df_null["eta"].median())
print(df_null)
print("######################")

print("Elimina righe con val None")
df_null_2 = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Giulia"],
    "citta": ["Milano",None, "Torino", None],
    "eta": [12, 77, None, 67]
})
print(df_null_2)
df_clean = df_null_2.dropna()
print(df_clean)
print("######################")

print("rimuovi duplicati")
df_duplo = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Giulia", "Anna"],
    "citta": ["Milano","Bergamo", "Torino", "Varese", "Milano"],
    "eta": [12, 77, 14, 67, 12]
})
print(df_duplo)
df_duplo = df_duplo.drop_duplicates()
print(df_duplo)
print("######################")

print("estrai giorno mese anno da data")
df_data = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco"],
    "data": ["2023-01-15", "2022-07-10", "2021-12-25"]
})
print(df_data)
df_data["data"] = pd.to_datetime(df_data["data"])
df_data["anno"] = df_data["data"].dt.year
df_data["mese"] = df_data["data"].dt.month
df_data["giorno"] = df_data["data"].dt.day
print(df_data)
print("######################")

print("normalizza colonna numerica")
df_norm = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Giulia"],
    "eta": [12, 77, 14, 67]
})
df_norm["eta_norm"] = (df_norm["eta"] - df_norm["eta"].min()) / (df_norm["eta"].max() - df_norm["eta"].min())
print(df_norm)
print("######################")

print("creare saluto personalizzato")
df["saluto"] = df["nome"].apply(lambda x: f"Ciao {x}")
print(df)
print("######################")

print("calcola rolling mean su 7")
data = pd.Series(
    [10,12,14,13,15,18,20,22,21,19],
    index = pd.date_range(start="2022-01-15", periods=10)
)
rolling_mean = data.rolling(7).mean()
print(rolling_mean)
print("######################")

print("crea multiindex")
df_multi_ind = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Giulia", "Paolo"],
    "citta": ["Roma", "Milano", "Roma", "Napoli", "Milano"],
    "eta": [12, 77, 14, 67, 12]
})
df_multi_ind = df_multi_ind.set_index(["citta", "nome"])
print(df_multi_ind)
print("#####################")

print("usare pipe con 2 trasformazioni")
df_double_transf = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Giulia"],
    "eta": [12, 77, 14, 67]
})
df_double_transf = df_double_transf.pipe(aggiungi_seniority).pipe(normalizza)
print(df_double_transf)