# Naším úkolem je vytvořit program, který vezme vstup v 24hodinovém formátu a převede jej do anglického času,
# který bude zahrnovat zkratky PM a AM.
#
# Tvé úkoly:
#
# Získej vstup uživatele do proměnné time

# Rozděl do listu vstup od uživatele do proměnné hours a mins.

# Uprav proměnou 'hours' tak, aby se do proměnné adjusted_hours místo 24 hodinového formátu (např.: 17) uložil
# formát anglický (např.: 5).

# Do proměnné daytime vyber odpovídající string z dvojčlenného listu ['AM', 'PM']
# ======================================================================================

# Získej vstup uživatele do proměnné `time`
time = input('Insert time for conversion in format hh:mm :  ')

# Rozděl do listu vstup od uživatele do proměnné `hours` a `mins`.
time = time.partition(':')
hours = time[0]
mins = time[2]


# Uprav proměnou `hours` tak, aby se do proměnné `adjusted_hours` místo
# 24 hodinového formátu (např.: 17) uložil formát anglický (např.: 5).
if int(hours) > 12:
    adjusted_hours = [str(int(hours) - 12), ':', mins, ' PM']
else:
    adjusted_hours = [hours, ':', mins, ' AM']

# Do proměnné `daytime` vyber odpovídající string z dvojčlenného listu ['AM', 'PM']

# Vytiskni převedený čas.
print('converted to eng format: ' + ''.join(adjusted_hours))
