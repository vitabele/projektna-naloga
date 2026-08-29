import pandas as pd


def zdruzi_podatke():
    df = pd.read_csv("igralke.csv")
    df_profili = pd.read_csv("profili.csv")

    df["PovezavaIme"] = df["Ime"].str.lower().str.replace(" ", "-")

    df_koncni = df.merge(df_profili, left_on="PovezavaIme", right_on="PovezavaIme", how="left")
    df_koncni = df_koncni.drop(columns=["PovezavaIme"])

    df_koncni.to_csv("wta_podatki_koncni.csv", index=False)
    print("Podatki so shranjeni v wta_podatki_koncni.csv")
    return df_koncni


if __name__ == "__main__":
    zdruzi_podatke()
    