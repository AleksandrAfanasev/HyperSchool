a = int(input())
chicken = 23
Goat = 678
Pig = 1296
Cow = 3848
Sheep = 6769
animals = (max(a // chicken, a // Goat, a // Pig, a // Cow, a // Sheep))
chicken_q = a // chicken
Goat_q = a // Goat
Cow_q = a // Cow
Sheep_q = a // Sheep
Pig_n = a // Pig
if animals < 1:
    print('None')
elif Sheep_q >= 1:
    print(Sheep_q, 'sheep')
elif Cow_q == 1:
    print(Cow_q, 'cow')
elif Cow_q > 1:
    print(Cow_q, 'cows')
elif Pig_n > 1:
    print(Pig_n, 'pigs')
elif Pig_n == 1:
    print(Pig_n, 'pig')
elif Goat_q > 1:
    print(Goat_q, 'goats')
elif Goat_q == 1:
    print(Goat_q, 'goat')
elif chicken_q > 1:
    print(chicken_q, 'chickens')
elif chicken_q == 1:
    print(chicken_q, 'chicken')