import re
import requests
import os
import pandas as pd


def pridobi_profile():
    with open("shranjene_strani/lestvica.html", "r", encoding="utf-8") as dat:
        lestvica_html = dat.read()

    povezave = re.findall(r'href="(/players/\d+/[a-z-]+)"', lestvica_html)
    povezave_unikatne = list(dict.fromkeys(povezave))

    URL_OSNOVNI = "https://www.wtatennis.com"
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"}

    os.makedirs("shranjene_strani", exist_ok=True)

    for povezava in povezave_unikatne:
        ime_datoteke = povezava.split("/")[-1] + ".html"
        pot_do_datoteke = "shranjene_strani/" + ime_datoteke

        if os.path.exists(pot_do_datoteke):
            continue

        polni_url = URL_OSNOVNI + povezava
        odgovor = requests.get(polni_url, headers=HEADERS)

        with open(pot_do_datoteke, "w", encoding="utf-8") as dat:
            dat.write(odgovor.text)

    seznam_starosti = []
    seznam_visin = []
    seznam_zmag_porazov = []
    seznam_rok = []
    seznam_imen_za_profile = []

    for povezava in povezave_unikatne:
        ime_datoteke = povezava.split("/")[-1] + ".html"
        pot_do_datoteke = "shranjene_strani/" + ime_datoteke

        with open(pot_do_datoteke, "r", encoding="utf-8") as dat:
            profil_html = dat.read()

        datum_rojstva = re.findall(r'data-dob="([\d-]+)"', profil_html)

        visina_vsi = re.findall(r'profile-header__meta-item b-s-sb dt:b-l-sb">([^<]+)<', profil_html)
        visina_prava = None
        for v in visina_vsi:
            v_ocisceno = v.strip()
            if v_ocisceno:
                visina_prava = v_ocisceno
                break

        zmage_porazi = re.findall(r'js-stat-value">(\d+) / (\d+)<', profil_html)
        roka = re.findall(r'profile-bio__info-content">\s*([\w-]+)<', profil_html)

        seznam_imen_za_profile.append(povezava.split("/")[-1])
        seznam_starosti.append(datum_rojstva[0] if datum_rojstva else None)
        seznam_visin.append(visina_prava)
        seznam_zmag_porazov.append(zmage_porazi[0] if zmage_porazi else None)
        seznam_rok.append(roka[0] if roka else None)

    zmage = [par[0] for par in seznam_zmag_porazov]
    porazi = [par[1] for par in seznam_zmag_porazov]

    df_profili = pd.DataFrame({
        "PovezavaIme": seznam_imen_za_profile,
        "DatumRojstva": seznam_starosti,
        "Visina": seznam_visin,
        "Zmage": zmage,
        "Porazi": porazi,
        "Roka": seznam_rok
    })

    df_profili.to_csv("profili.csv", index=False)
    print("Podatki shranjeni v profili.csv")
    return df_profili


if __name__ == "__main__":
    pridobi_profile()