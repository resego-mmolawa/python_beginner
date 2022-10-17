from math import factorial as fac
from math import sqrt as sq

print( '#' * 20 + ' SQUARE ROOT ' + '#'* 20)
square = sq(81)
print('The square root of 81 is', int(square))

print( '#' * 20 + ' FACTOR 1 ' + '#'* 20)
factor_1 = fac(5)
print('The first factor is', factor_1)

print( '#' * 20 + ' FACTOR 2 ' + '#'* 20)
factor_2 = fac(6)
print('The second factor is', factor_2)

print( '#' * 20 + ' DRAW ' + '#'* 20)
n = 5
k = 3

draw = fac(n) // (fac(k) * fac(n - k))
print('The first draw is', draw)

print( '#' * 20 + ' DRAW 2 ' + '#'* 20)
n = 100
k = 2

draw_02 = fac(n) // (fac(k) * fac(n -k))
print('The second draw is', draw_02)

print( '#' * 20 + ' FACTOR 3 ' + '#'* 20)
n_02 = 100
draw_03 = len(str(fac(n)))
print('The length of the number in the third draw is', draw_03)