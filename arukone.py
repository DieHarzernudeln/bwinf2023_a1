# Algorithmus

import math
import random

# [[y, x], value]
solver_trap_pattern = [
    [[0, 0], 1],
    [[1, 3], 1],
    [[0, 3], 2],
    [[2, 1], 2]
]

trap_pattern_size = 4

# Ecke für Trap
trap_top = True
trap_left = False

def erstelle_arukone(n: int) -> list[list[int]]:
    global trap_top, trap_left

    arukone = [[0 for _ in range(n)] for _ in range(n)]
    paare = math.ceil(n / 2)

    # Spiegeln in y-Richtung
    if random.getrandbits(1):
        trap_top = not trap_top

        for pattern_entry in solver_trap_pattern:
            pattern_entry[0][0] = 3 - pattern_entry[0][0]
            
    # Spiegeln in x-Richtung
    if random.getrandbits(1):
        trap_left = not trap_left

        for pattern_entry in solver_trap_pattern:
            pattern_entry[0][1] = 3 - pattern_entry[0][1]
            
    # Drehen um 90°
    if random.getrandbits(1):
        old_top = trap_top
        trap_top = trap_left
        trap_left = not old_top

        for pattern_entry in solver_trap_pattern:
            temp = pattern_entry[0][0]
            pattern_entry[0][0] = pattern_entry[0][1]
            pattern_entry[0][1] = 3 - temp

    trap_pattern_x = 0 if trap_left else n - trap_pattern_size
    trap_pattern_y = 0 if trap_top else n - trap_pattern_size

    for pattern_entry in solver_trap_pattern:
        arukone[trap_pattern_y + pattern_entry[0][0]][trap_pattern_x + pattern_entry[0][1]] = pattern_entry[1]

    for i in range(3, paare + 1):
        y_position_start = random.randint(0, n - 3)
        y_position_ende = random.randint(y_position_start + 2, n - 1)

        x_position = (trap_pattern_size if trap_left else 0) + i - 3

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
