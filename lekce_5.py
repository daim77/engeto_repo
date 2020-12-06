# Co se naučíš v tomto kurzu
# Datový typ Range,
# smyčka For,
# základy funkcí,
# formátování string,

print('0-19:    ', list(range(20)))
print('15-19:   ', tuple(range(15,20)))
print('10-19:   ', tuple(range(10,20,3)))

# Do proměnné nums vytvoř list pomocí range, který bude obsahovat každé číslo,
# které je dělitelné 5 v rozmezí od 1-100.
nums = list(range(5,101,5))
print(nums)