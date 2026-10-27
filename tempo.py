def vypocitej_tempo(vzdalenost: float, cilovy_cas: float) -> float:
    if vzdalenost <= 0:
        raise ValueError("Chyba při zadávání vzdálenosti")
    elif cilovy_cas <=0:
        raise ValueError("Chyba při zadávání cílového času")
    
    tempo = cilovy_cas / vzdalenost
    return tempo

def formatuj_tempo(tempo: float) ->str:
    minuty = int(tempo)
    sekundy = round((tempo - minuty) *60)
    if sekundy == 60:
        minuty += 1 
        sekundy = 0
    prevedene_tempo = f"{minuty}:{sekundy:02d}" #:02d – formátování celého čísla (int) na minimálně 2 číslice. Pokud má číslo méně číslic, doplní se zleva nula
    return prevedene_tempo