import requests
import os


def prenesi_lestvico():
    URL = 'https://www.wtatennis.com/players'
    HEADERS ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"}
#(pridobljeno: https://www.geeksforgeeks.org/python/user-agent-in-python-request/)
    odgovor = requests.get(URL, headers=HEADERS)
    os.makedirs("shranjene_strani", exist_ok= True) 
    pot_do_datoteke = "shranjene_strani/lestvica.html"

    if not os.path.exists(pot_do_datoteke):
        odgovor = requests.get(URL, headers=HEADERS)
        with open("shranjene_strani/lestvica.html", "w", encoding="utf-8") as dat:
            dat.write(odgovor.text)
        print('napisano')
    else:
        print("Lestvica že obstaja.")

if __name__ == "__main__":
    prenesi_lestvico()