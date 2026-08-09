import requests
import os
import re

URL = 'https://www.wtatennis.com/players'
HEADERS ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
#zato da ne mislijo da smo robot (pridobljeno: https://www.geeksforgeeks.org/python/user-agent-in-python-request/)
odgovor = requests.get(URL, headers=HEADERS)
#obisk spletne strani, pošlje get ( The get() method sends a GET request to the specified url.)

print("Status koda:", odgovor.status_code)
#da vidimo če je vse ok, 200 -uspelo, 403/404- ni uspelo
print(odgovor.text[:500])
#da preverimo če je res koda, prvih 500 znakov

#na spletni strani kliknem na prvo igralko, da vidim kako se začne razpored in klikne inspect elements
print("Sabalenka" in odgovor.text ) #preverim, če so se prenesla imena
#ugotovitev: 
#Vsaka igralka je znotraj <div class="players-list__item">
#Ime: <h3 class="players-list__name">
#Država: <div class="players-list__country players-list__country--BLR"> (kratica države je del imena classa - zanimivo, to bova uporabila)
#Točke: <span class="players-list__points">
#Rang (mesto na lestvici): <div class="players-list__rank">
print(odgovor.text.count("players-list__item")) #da vidimo koliko imen je prekopiralo

os.makedirs("shranjene_strani", exist_ok= True) #naredi mapico shranjene strani, ta del exist=ok je zato da ni napake če je mapica že torej lahko večkrat poženemo kodo
with open("shranjene_strani/lestvica.html", "w", encoding="utf-8") as dat:
    dat.write(odgovor.text)
    print('napisano')

imena = re.findall(r'data-player-name="([^"]+)"', odgovor.text)
print("stevilo_imen:", len(imena)) #ker napiše 100 se vrjetno vsako ime podvoji zato s spodnjimi pregledamo in res dvakrat vsa imena
print(imena[:5])
print(imena[50:55])
#popravimo
unikatna_imena = list(dict.fromkeys(imena))#list da pretvorimo nazaj v seznam, dict.fromkeys slovarji po definiciji nimajo ponavljanj, zato usako ime enkrat
print("stevilo unikatnih imen:", len(unikatna_imena))
print(unikatna_imena[:5])