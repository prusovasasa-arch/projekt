import tempo 

while True:
    try:
        cilovy_cas = float(input("Jaký je tvůj cílový čas? (minuty) "))
        vzdalenost = float(input("Jakou vzdálenost poběžíš?(km) ")) 
        vysledek = tempo.vypocitej_tempo(vzdalenost, cilovy_cas)
        break
    except ValueError:
        print("Neplatný vstup!")



#print(vysledek)
zformatovany_vysledek = tempo.formatuj_tempo(vysledek)
print(f"pro dosažení cílového času musíš běžet tempem {zformatovany_vysledek} min/km")