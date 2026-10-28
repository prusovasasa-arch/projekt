import gpxpy  # Import knihovny pro načítání a zpracování GPX souborů (GPS tras)
with open("trasa.gpx", "r", encoding = "utf-8") as soubor:
    gpx = gpxpy.parse(soubor) #vezme otevřený gpx soubor, přečte jeho obsah a převede ho do podoby, se kterou umí python pracovat. Díky tomu pak můžu získávat jednotlivé body trasy, souřadnice a nadmořskou výšku.
#print(len(gpx.tracks[0].segments))  #tímto zjištuji kolik  má trasa segmentu, segment je GPS úsek trati, který obsahuje jednotlivé GPS body
body = (gpx.tracks[0].segments[0].points) 
#bod = gpx.tracks[0].segments[0].points[0]
#bod2 = gpx.tracks[0].segments[0].points[1]
#print(bod2.elevation)
#print(bod.elevation)
for i in range(len(body)-1):
    bod = body[i]
    dalsiBod = body[i+1]
    if bod.elevation < dalsiBod.elevation:
        rozdil = dalsiBod.elevation - bod.elevation
        print(f"Čeká tě stoupání o {rozdil:.2f} m")
    elif bod.elevation > dalsiBod.elevation:
        rozdil = bod.elevation - dalsiBod.elevation
        print(f"čeká tě klesání o {rozdil:.2f} m")
    elif bod.elevation == dalsiBod.elevation:
        print("poběžíš po rovince")

