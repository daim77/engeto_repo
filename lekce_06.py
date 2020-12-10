# opakovani while
# nakuni kosik chci naplnit potravinami

kosik = {}
oddelovac = '=' * 40
potraviny = {
    'mleko': 30,
    'maso': 100,
}
print(oddelovac)
for i in range(3):
    vyber = input('vyber potravinu: ')
    while vyber not in potraviny:
        cena = int(input('zadej cenu: '))
        potraviny.setdefault(vyber)
        potraviny[vyber] = cena
    kosik[vyber] = potraviny[vyber]

print(kosik)
