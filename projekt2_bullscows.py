import random
import time

nahodne_cislo = []
zadane_cislo = []

def main():
    print("Ahoj, vitej ve hre bulls and cows!")
    print("Generuji nahodne ctyrciferne cislo (muze zacinat nulou).")
    vytvor_nahodne_cislo()
    t0 = time.time()
    pokus = 0
    while nahodne_cislo != zadane_cislo:
        pokus += 1
        print(16 * "=")
        print("Pokus cislo: {} .".format(pokus))
        print(16 * "=")
        zadane_cislo.clear()
        zadej_cislo()
        print(41 * "=")
        porovnej_cisla(nahodne_cislo, zadane_cislo)
        print(41 * "=")
        if nahodne_cislo == zadane_cislo:
            break
        ukonceni = input("Pro ukonceni zadej 'exit',pro pokracovani zadej cokoli jineho a stiskni ENTER : ")
        if ukonceni == 'exit':
            break
        else:
            continue
    if zadane_cislo == nahodne_cislo:
        t1 = time.time() - t0
        casy.append(t1)
        pokusy.append(pokus)
        print("Vyborne, uhodl jsi na pocet pokusu: {} , za cas {} vterin.".format(pokus, t1))
    else:
        t1 = time.time() - t0
        casy.append(-t1)
        pokusy.append(-pokus)
        print("Nevadi, snad nekdy priste.")

def vytvor_nahodne_cislo():
    while len(nahodne_cislo) < 4:
        x = random.randint(0, 9)
        if x not in nahodne_cislo:
            nahodne_cislo.append(x)

def zadej_cislo():
    cislo_str = input("Vloz ctyrciferne cislo! : ")
    while len(cislo_str) != 4 or cislo_str.isalpha():
        cislo_str = input("Neplatne zadani! Vloz ctyrciferne cislo! : ")
    for i in range(4):
        zadane_cislo.append(int(cislo_str[i]))

def porovnej_cisla(nahodne_cislo, zadane_cislo):
    bulls = 0
    dohromady = 0
    for i in range(0, 4):
        if nahodne_cislo[i] == zadane_cislo[i]:
            bulls += 1
    for i in nahodne_cislo:
        if i in zadane_cislo:
            dohromady += 1
    cows = dohromady - bulls
    print("Trefil jsi pocet BULLS: {} a pocet COWS: {} ".format(bulls, cows))

pokusy = []
casy = []

while True:
    nahodne_cislo.clear()
    zadane_cislo.clear()
    main()
    konec_hry = input("Pro UKONCENI zadej 'exit', pro NOVOU HRU zadej cokoli : ")
    if konec_hry == 'exit':
        break
    else:
        continue
print("Znamenko minus [-] indikuje NEDOHRANOU hru!")
print("POCET pokusu v jednotlivych hrach: {}.".format(pokusy))
print("CASY jednotlivych her [vteriny]: {}.".format(casy))
print("Ukoncuji, nashledanou...")