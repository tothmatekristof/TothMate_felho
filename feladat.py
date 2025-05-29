#Ezzel diagrammot keszitek napok számával és csillagok számával
def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)
    csillagok = '*' * csillagok_szama
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor

#Ezzel diagrammot rajzolok az átlag hõmérsékletekkel
def rajzolj_diagram(homersekletek):
    print("Napi átlaghõmérséklet diagram (°C)")
    print("-" * 40)

    for i in range(len(homersekletek)):
        nap = i + 1  # Napok számozása 1-tõl indul
        sor = keszit_diagram_sort(nap, homersekletek[i])
        print(sor)


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

rajzolj_diagram(napi_atlaghomersekletek)
