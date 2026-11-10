import gpxpy  # Import knihovny pro načítání a zpracování GPX souborů (GPS tras)
with open("trasa.gpx", "r", encoding = "utf-8") as soubor:
    gpx = gpxpy.parse(soubor) #vezme otevřený gpx soubor, přečte jeho obsah a převede ho do podoby, se kterou umí python pracovat. Díky tomu pak můžu získávat jednotlivé body trasy, souřadnice a nadmořskou výšku.
#print(len(gpx.tracks[0].segments))  #tímto zjištuji kolik  má trasa segmentu, segment je GPS úsek trati, který obsahuje jednotlivé GPS body
body = (gpx.tracks[0].segments[0].points) 

celkovaVzdalenost = 0
vzdalenostUseku = 0
stoupaniUseku = 0
klesaniUseku = 0
useky = []
usekyKm = []
zmenaVysky = 0



for i in range(len(body)-1):
    bod = body[i]
    dalsiBod = body[i+1]
    vzdalenost = bod.distance_2d(dalsiBod)
    celkovaVzdalenost += vzdalenost 
    rozdilNadmorskeVysky = dalsiBod.elevation - bod.elevation 

    if rozdilNadmorskeVysky > 0:
        stoupaniUseku += rozdilNadmorskeVysky

    elif rozdilNadmorskeVysky < 0:
        klesaniUseku -= rozdilNadmorskeVysky

    vzdalenostUseku += vzdalenost
    
    if vzdalenostUseku >= 100:
        zmenaVysky = stoupaniUseku - klesaniUseku
        sklonUseku = (zmenaVysky / vzdalenostUseku) * 100
        if sklonUseku >= -1 and sklonUseku <= 1:
            typUseku = "rovina"
        elif sklonUseku >1:
            typUseku = "stoupání"
        elif sklonUseku < -1:
            typUseku = "klesání"
       
        usek = { 
                "vzdalenost: ":  vzdalenostUseku,
                 "stoupani: ": stoupaniUseku,
                 "klesani: ": klesaniUseku,
                 "sklon: ": sklonUseku,
                 "typ: ": typUseku
                }
        useky.append(usek)

        print("Dokončili jste úsek!")
        print(f"Stoupání: {stoupaniUseku:.2f} m")
        print(f"Klesání: {klesaniUseku:.2f} m")
        print(f"Délka úseku: {vzdalenostUseku:.2f} m")
        print(f"sklon: {sklonUseku:.2f} %")
        print("-----------------------")
        
        vzdalenostUseku = 0
        stoupaniUseku = 0
        klesaniUseku = 0


kilometrovyUsek = 0
stoupaniKilometr = 0
klesaniKilometr = 0
zbyvaDoKilometru = 0



for usek in useky:
        zbyvaDoKilometru = 1000 - kilometrovyUsek

        if usek["vzdalenost: "] <= zbyvaDoKilometru:
            kilometrovyUsek += usek["vzdalenost: "]
            stoupaniKilometr += usek["stoupani: "]
            klesaniKilometr += usek["klesani: "]
        else:
            podil = zbyvaDoKilometru / usek["vzdalenost: "]

            stoupaniKilometr = stoupaniUseku * podil
            klesaniKilometr = klesaniUseku * podil

            kilometrovyUsek = 1000


        while kilometrovyUsek >= 1000:
               usekyKm.append({
            "vzdalenost": 1000,
            "stoupani": stoupaniKilometr,
            "klesani": klesaniKilometr
                })
            
        kilometrovyUsek = kilometrovyUsek - 1000
        stoupaniKilometr = 0
        klesaniKilometr = 0

        if usek["vzdalenost: "] > zbyvaDoKilometru:
            kilometrovyUsek += usek["vzdalenost: "] - zbyvaDoKilometru
            stoupaniKilometr += usek["stoupani: "] * (1 - podil)
            klesaniKilometr += usek["klesani: "] * (1 - podil)
            
            
            
if kilometrovyUsek > 0:
    usekyKm.append(kilometrovyUsek, stoupaniKilometr, klesaniKilometr)


        
       

 

print(f"Celková vzdálenost: {celkovaVzdalenost / 1000:.2f} km")


    
    
