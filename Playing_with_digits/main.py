# https://www.codewars.com/kata/5552101f47fc5178b1000050
def dig_pow(n: int, p):
    l = list()
    test = n
    while test >= 1:
        l.append(int(test % 10))
        test /= 10
    l.reverse()
    z = int(0)
    for i in l:
        z += i ** p
        p += 1
    if int(z % n) == 0:
        return int(z/n)
    else:
        return -1


print(dig_pow(46288, 3))