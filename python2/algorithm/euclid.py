import sys

def gcd(a, b):
    '''
    Find the greatest common denominator of two numbers.
    '''
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    '''
    Find the least common multiple of two numbers.
    '''
    return (a * b) / gcd(a, b)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print 'The GCD of {} and {} is {}.'.format(sys.argv[1], sys.argv[2], gcd(int(sys.argv[1]), int(sys.argv[2])))
        print 'The LCM of {} and {} is {}.'.format(sys.argv[1], sys.argv[2], lcm(int(sys.argv[1]), int(sys.argv[2])))
