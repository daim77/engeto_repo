# Cenik
mercedes    = 150
rolls_royce = '400'

# welcome
print('=' * 50)
print("Welcome in our e-show room price calculation :-)")
print('=' * 50)
print('=' * 50)
# question for additional eqiupment
add_price = int(input('Insert your maximum price for additionl car equipment: '))
print('=' * 50)
# price calculation
print('Price for two Mercedes is', mercedes * 2)
print('Price for 2M and 2RR is', mercedes + int(rolls_royce))
print('Price for 2RR with 2AE is', (int(rolls_royce)+add_price) * 2)
print('Price for one Mercedes wit one AE is', mercedes + add_price)