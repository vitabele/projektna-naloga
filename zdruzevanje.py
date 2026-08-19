#import pandas as pd
#
#df = pd.read_csv("igralke.csv")
#df_profili = pd.read_csv("profili.csv")
#
#print(df.head()) #.head je samo prvih nekaj profilov v oklepaju bi lahk dodali tudi koliko vrstice želimo
#print(df_profili.head())
#
#df["PovezavaIme"] = df["Ime"].str.lower().str.replace(" ", "-")
#
#print(df[["Ime", "PovezavaIme"]].head(2))
#
#df_koncni = df.merge(df_profili, left_on="PovezavaIme", right_on="PovezavaIme", how="left") #how lweft da obdži levi stolpec
#
#df_koncni = df_koncni.drop(columns=["PovezavaIme"]) #odstranimo stolpec povezava ime 
#
#
#print(df_koncni.head(2))
#print("Število vrstic:", len(df_koncni))
#
#
#df_koncni.to_csv("wta_podatki_koncni.csv", index=False)
#print("Shranjeno v wta_podatki_koncni.csv")

import pandas as pd


def zdruzi_podatke():
    df = pd.read_csv("igralke.csv")
    df_profili = pd.read_csv("profili.csv")

    df["PovezavaIme"] = df["Ime"].str.lower().str.replace(" ", "-")

    df_koncni = df.merge(df_profili, left_on="PovezavaIme", right_on="PovezavaIme", how="left")
    df_koncni = df_koncni.drop(columns=["PovezavaIme"])

    df_koncni.to_csv("wta_podatki_koncni.csv", index=False)
    print("Končni podatki shranjeni v wta_podatki_koncni.csv")
    return df_koncni


if __name__ == "__main__":
    zdruzi_podatke()
    