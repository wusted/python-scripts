def greatest_common_divisor(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

print(greatest_common_divisor(12,16))
