#import re
#import requests
#import os
#
#with open("shranjene_strani/lestvica.html", "r", encoding="utf-8") as dat:
#    lestvica_html = dat.read()
#
## vzamemo eno profilno povezavo za test samo da smo preverili
#prva_povezava = re.findall(r'href="(/players/\d+/[a-z-]+)"', lestvica_html)[0] #poiščemo vs epovezave do profilov in vzamemo samo prvega, \d pomeni aterakoli številak + pa eno al več takih zaporedoma (to je za ID igralke), /[a-z-]+ to pomeni katerokoli črko ali vezaj +  pa eno ali več zaporedoma (torej najde players/številke/ime z vezajem)
#print("Testiram na:", prva_povezava) #da vidimo če je ok
#
#URL_OSNOVNI = "https://www.wtatennis.com"
#HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
#
#URL_KONCNI = URL_OSNOVNI + prva_povezava
#odgovor = requests.get(URL_KONCNI, headers=HEADERS)
#profil_html = odgovor.text
#print("status:", odgovor.status_code)
#
#
#povezave = re.findall(r'href="(/players/\d+/[a-z-]+)"', lestvica_html)
#print("Število najdenih profilov:", len(povezave))
#print("Prvih 5:", povezave[:5])
#povezave_unikatne = list(dict.fromkeys(povezave))
##odstranimo podvojene povezave 
#
#print("Število unikatnih profilov:", len(povezave_unikatne))
#
#os.makedirs("shranjene_strani", exist_ok=True)
#
#for povezava in povezave_unikatne:
#    ime_datoteke = povezava.split("/")[-1] + ".html"
#    pot_do_datoteke = "shranjene_strani/" + ime_datoteke
#
#    if os.path.exists(pot_do_datoteke):
#        print(ime_datoteke, "že shranjeno")
#        continue
#
#    with open(pot_do_datoteke, "w", encoding="utf-8") as dat:
#        dat.write(odgovor.text)
#
#    print(ime_datoteke, "- preneseno in shranjeno.")
#
#seznam_starosti = []
#seznam_visin = []
#seznam_zmag_porazov = []
#seznam_rok = []
#seznam_imen_za_profile = []
#
#for povezava in povezave_unikatne:
#    ime_datoteke = povezava.split("/")[-1] + ".html"
#    pot_do_datoteke = "shranjene_strani/" + ime_datoteke
#    with open(pot_do_datoteke, "r", encoding="utf-8") as dat:
#        profil_html = dat.read()
#
#    datum_rojstva = re.findall(r'data-dob="([\d-]+)"', profil_html)
#    visina = re.findall(r'profile-header__meta-item b-s-sb dt:b-l-sb">([^<]+)<', profil_html)
#    zmage_porazi = re.findall(r'js-stat-value">(\d+) / (\d+)<', profil_html)
#    roka = re.findall(r'profile-bio__info-content">\s*([\w-]+)<', profil_html)
#
#    seznam_imen_za_profile.append(povezava.split("/")[-1])
#    seznam_starosti.append(datum_rojstva[0] if datum_rojstva else None)
#    seznam_visin.append(visina[0] if visina else None)
#    seznam_zmag_porazov.append(zmage_porazi[0] if zmage_porazi else None)
#    seznam_rok.append(roka[0] if roka else None)
#
#print("Končano. Primer prvih 3 vrstic:")
#print(seznam_imen_za_profile[:3])
#print(seznam_starosti[:3])
#print(seznam_visin[:3])
#print(seznam_zmag_porazov[:3])
#print(seznam_rok[:3])

import re
import requests
import os
import pandas as pd

with open("shranjene_strani/lestvica.html", "r", encoding="utf-8") as dat:
    lestvica_html = dat.read()

povezave = re.findall(r'href="(/players/\d+/[a-z-]+)"', lestvica_html)
povezave_unikatne = list(dict.fromkeys(povezave))
print("Število unikatnih profilov:", len(povezave_unikatne))

URL_OSNOVNI = "https://www.wtatennis.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

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

    print(ime_datoteke, "- preneseno in shranjeno.")

print("Vsi profili so shranjeni.")

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

print("Končano. Primer prvih 3 vrstic:")
print(seznam_imen_za_profile[:3])
print(seznam_starosti[:3])
print(seznam_visin[:3])
print(seznam_zmag_porazov[:3])
print(seznam_rok[:3])



zmage = [par[0] for par in seznam_zmag_porazov] 
#zmage = []
#for par in seznam_zmag_porazov:
#    zmage.append(par[0])
porazi = [par[1] for par in seznam_zmag_porazov]

df_profili = pd.DataFrame({
    "PovezavaIme": seznam_imen_za_profile,
    "DatumRojstva": seznam_starosti,
    "Visina": seznam_visin,
    "Zmage": zmage,
    "Porazi": porazi,
    "Roka": seznam_rok
})

print(df_profili)
#moremo shranit v csv da mamo igralke in profile ker je potrebno sedaj družit obe tabeli probelm ker so drugače zapisana imena
df_profili.to_csv("profili.csv", index=False)
print("Shranjeno v profili.csv")