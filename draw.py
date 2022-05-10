n =int(input('Please Inter rows: '))
falg_even = False
m = 1
if n % 2 == 0:
    j = 1
    falg_even = True
else:
    j = 0
for i in range(j, n//2):
    print(' ' * ((n - m) // 2), '*' * m, ' ' * ((n - m) // 2))
    m += 2
if falg_even:
    print(' ' * ((n - m) // 2), '*' * m, ' ' * ((n - m) // 2))
for i in range(-1, n // 2):
    print(' ' * ((n - m) // 2), '*' * m, ' ' * ((n - m) // 2))
    m -= 2
