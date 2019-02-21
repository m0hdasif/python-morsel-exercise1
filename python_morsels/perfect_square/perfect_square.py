import cmath
import decimal

def is_whole_num(x):
    return x % 1 == 0

def is_perfect_square(x, *, complex=False):
    try:
        if complex:
            c_num = cmath.sqrt(x)
            return all([is_whole_num(n) for n in (c_num.real, c_num.imag)])
        else:
            decimal.getcontext().prec = 100
            return False if x < 0 else is_whole_num(decimal.Decimal(x).sqrt())
    except:
        raise TypeError()
