from math import isqrt
enter_numbers = int('5')
for a in range(1, isqrt(enter_numbers)+1):
    bb = enter_numbers - a * a
    b = isqrt(bb)
    if bb == b*b:
        print(True)
        break
    else:
        print(False)



