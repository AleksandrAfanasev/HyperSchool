index_of_synthesis = float(input())

if index_of_synthesis < 2:
    print('Analytic ')
elif 2 <= index_of_synthesis <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
