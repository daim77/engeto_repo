# Napiš Python skript, který sečte odděleně všechna sudá a všechna lichá čísla ze seznamu.
# Na konci by měl program vytisknout absolutní hodnotu rozdíu mezi těmito součty.

cisla = [
    386, 462, 47, 418, 907, 344, 236, 375, 823,
    566, 597, 978, 328, 615, 953, 345, 399, 162,
    758, 219, 918, 237, 412, 566, 826, 248, 866,
    950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
    24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
    742, 717, 958, 743, 527
]
soucet_cisla = [0, 0]  # index 0 je licha a index 1 je suda
while cisla:
    my_pop = cisla.pop()
    if my_pop % 2 == 0:
        soucet_cisla[1] = soucet_cisla[1] + my_pop
    else:
        soucet_cisla[0] = soucet_cisla[0] + my_pop
print(abs(soucet_cisla[0] - soucet_cisla[1]))