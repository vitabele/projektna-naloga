from prenos import prenesi_lestvico
from luščenje import osnovni_podatki
from profili import pridobi_profile
from zdruzevanje import zdruzi_podatke


def main():
    print("1/4 Prenos lestvice.")
    prenesi_lestvico()

    print("2/4 Prenos osnovnih podatkov.")
    osnovni_podatki()

    print("3/4 Prenos profilov igralk.")
    pridobi_profile()

    print("4/4 Združevanje podatkov.")
    zdruzi_podatke()

    print("Uspešno opravljeno.")

if __name__ == "__main__":
    main()