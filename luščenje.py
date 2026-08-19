#import requests
#import re
#import os
#import pandas as pd
#
#with open("shranjene_strani/lestvica.html", "r", encoding="utf-8") as dat:
#    podatki_html = dat.read()
#
#
#imena = re.findall(r'data-player-name="([^"]+)"', podatki_html)
#print("stevilo_imen:", len(imena)) #ker napiše 100 se vrjetno vsako ime podvoji zato s spodnjimi pregledamo in res dvakrat vsa imena
##print(imena[:5])
##print(imena[50:55])
##popravimo
#unikatna_imena = list(dict.fromkeys(imena))#list da pretvorimo nazaj v seznam, dict.fromkeys slovarji po definiciji nimajo ponavljanj, zato usako ime enkrat
#print("stevilo unikatnih imen:", len(unikatna_imena))
#print(unikatna_imena[:5])
#
#
#tocke = re.findall(r'players-list__points[^>]*>\s*(\d+)', podatki_html)
#print("Število točk:", len(tocke))
#print(tocke[:5])
#
#drzave = re.findall(r'players-list__country--([A-Z]+)', podatki_html)
#print("Število držav:", len(drzave))
#print(drzave[:5])
#
#df = pd.DataFrame({
#    "Ime": unikatna_imena,
#    "Drzava": drzave,
#    "Tocke": tocke
#}) #data frame je tabela, vsebino podamo kot slovar
#
#print(df)
#df.to_csv("igralke.csv", index=False) #csv - comma separeted values, index =false je to da ne sprinta nteksa
#print("Shranjeno v igralke.csv")

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