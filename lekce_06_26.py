# Napiš program, který tiskne celá čísla od 1 do 100 (včetně).
# Ale:
# pro násobky 3 vytiskni Fizz (namísto čísla)
# pro násobky 5 vytiskni Buzz (namísto čísla)
# pro násobky 3 a 5 zároveň vytiskni FizzBuzz (namísto čísla)

for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
