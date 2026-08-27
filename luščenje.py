import re
import pandas as pd


def osnovni_podatki():
    with open("shranjene_strani/lestvica.html", "r", encoding="utf-8") as dat:
        html = dat.read()

    imena = re.findall(r'data-player-name="([^"]+)"', html)
    imena_unikatna = list(dict.fromkeys(imena))

    tocke = re.findall(r'players-list__points[^>]*>\s*(\d+)', html)
    drzave = re.findall(r'players-list__country--([A-Z]+)', html)

    df = pd.DataFrame({
        "Ime": imena_unikatna,
        "Drzava": drzave,
        "Tocke": tocke
    })

    df.to_csv("igralke.csv", index=False)
    print("Osnovni podatki shranjeni v igralke.csv")
    return df


if __name__ == "__main__":
    osnovni_podatki()