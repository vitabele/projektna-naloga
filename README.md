# ANALIZA TRENUTNIH PETDESETIH NAJBOLJŠIH TENIŠKIH IGRALK

## OPIS
Program zajame podatke o 50 najboljših igralkah iz uradne spletne strani WTA [wtatennis.com](https://www.wtatennis.com/players). Za vsako igralko pridobi osnovne podatke, npr. ime, država, točke. Obenem pa tudi dodatne podatke iz profila posamezne igralke npr. starost, višina, delež zmag/porazov... Podatki so analizirani in predstavljeni v Juptyer Notebooku z grafi. 

## Struktura 
- `prenos.py` - prenese in shrani HTML stran z lestvico igralk
- `luščenje.py` - izvleče ime, državo in točke iz shranjene lestvice
- `profili.py` - prenese profile vseh igralk in izvleče starost, višino, zmage/poraze, roko
- `zdruzevanje.py` - združi vse podatke v eno tabelo (`wta_podatki_koncni.csv`)
- `main.py` - glavna datoteka, ki po vrsti zažene vse zgornje datoteke
- `analiza_podatkov.ipynb` - Jupyter Notebook z analizo in vizualizacijo podatkov
- `shranjene_strani/` - lokalno shranjene HTML strani (cache)

## Zagon
Projekt se zažene preko glavne datoteke main.py, ki zaporedno izvede vse potrebne ukaze. 

## Rezultati
Rezultati in ugotovitve so zabeležen v zaključku datoteke analiza_podatkov.ipynb. 