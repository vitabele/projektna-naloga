from prenos import prenesi_lestvico
from luščenje import osnovni_podatki
from profili import pridobi_profile
from zdruzevanje import zdruzi_podatke


def main():
    print("1/4 Prenašam lestvico...")
    prenesi_lestvico()

    print("2/4 Izvlečem osnovne podatke...")
    osnovni_podatki()

    print("3/4 Prenašam in obdelam profile igralk...")
    pridobi_profile()

    print("4/4 Združujem podatke...")
    zdruzi_podatke()

    print("Končano! Podatki so pripravljeni v wta_podatki_koncni.csv")
    print("Odpri analiza_podatkov.ipynb za ogled analize.")


if __name__ == "__main__":
    main()