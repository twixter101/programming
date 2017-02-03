import sys

def gcd(a, b):
    '''
    Find the greatest common denominator of two numbers.
    '''
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print gcd(int(sys.argv[1]), int(sys.argv[2]))
