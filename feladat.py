def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)
    csillagok = '*' * csillagok_szama
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}�C)"
    return sor


def rajzolj_diagram(homersekletek):
    print("Napi �tlagh�m�rs�klet diagram (�C)")
    print("-" * 40)

    for i in range(len(homersekletek)):
        nap = i + 1  # Napok sz�moz�sa 1-t�l indul
        sor = keszit_diagram_sort(nap, homersekletek[i])
        print(sor)


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

rajzolj_diagram(napi_atlaghomersekletek)
