# Algorithmus

import math
import random

class SchemaPunkt:
    def __init__(self, x, y, wert) -> None:
        self.x = x
        self.y = y
        self.wert = wert

# (breite_hoehe, ist_links, ist_oben, [(x, y, wert), ...])
def erstelle_falle(fenster_groesse: int) -> tuple[int, bool, bool, list[SchemaPunkt]]:
    schema_breite_hoehe = 4
    schema = [
        SchemaPunkt(0, 0, 1),
        SchemaPunkt(3, 1, 1),
        SchemaPunkt(3, 0, 2),
        SchemaPunkt(1, 2, 2)
    ]

    ist_oben = True
    ist_links = False

    # Spiegeln in x-Richtung
    if random.getrandbits(1):
        ist_links = not ist_links

        for eintrag in schema:
            eintrag.x = (schema_breite_hoehe - 1) - eintrag.x
            
    # Spiegeln in y-Richtung
    if random.getrandbits(1):
        ist_oben = not ist_oben

        for eintrag in schema:
            eintrag.y = (schema_breite_hoehe - 1) - eintrag.y
            
    # Drehen um 90°
    if random.getrandbits(1):
        temp = ist_oben
        ist_oben = ist_links
        ist_links = not temp

        for eintrag in schema:
            temp = eintrag.y
            eintrag.y = eintrag.x
            eintrag.x = (schema_breite_hoehe - 1) - temp

    # an Position bewegen

    x_position_falle = 0 if ist_links else fenster_groesse - schema_breite_hoehe
    y_position_falle = 0 if ist_oben else fenster_groesse - schema_breite_hoehe

    for eintrag in schema:
        eintrag.x += x_position_falle
        eintrag.y += y_position_falle

    return (schema_breite_hoehe, ist_links, ist_oben, schema)

def erstelle_arukone(n: int) -> list[list[int]]:
    arukone = [[0 for _ in range(n)] for _ in range(n)]
    paare = math.ceil(n / 2)

    # Falle übertragen

    falle_groesse, falle_links, falle_oben, falle_schema = erstelle_falle(n)

    for eintrag in falle_schema:
        arukone[eintrag.y][eintrag.x] = eintrag.wert

    # mit restlichen Paaren auffüllen

    for i in range(3, paare + 1):
        y_position_start = random.randint(0, n - 3)
        y_position_ende = random.randint(y_position_start + 2, n - 1)

        x_position = (falle_groesse if falle_links else 0) + i - 3

        arukone[y_position_start][x_position] = i
        arukone[y_position_ende][x_position] = i

    return arukone


# Testen

def arukone_anzeigen(arukone: list[list[int]]):
    n = len(arukone)
    paare = max([max(zeile) for zeile in arukone])
    daten = "\n".join([" ".join([str(feld) for feld in zeile]) for zeile in arukone])

    print(n)
    print(paare)
    print(daten)
    print()


try:
    while True:
        n = int(input("n: "))
        arukone = erstelle_arukone(n)
        arukone_anzeigen(arukone)


except KeyboardInterrupt:
    exit()
