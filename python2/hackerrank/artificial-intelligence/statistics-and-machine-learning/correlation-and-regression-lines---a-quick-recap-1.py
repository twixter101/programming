# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

pScores = [15, 12, 8,  8, 7, 7, 7, 6, 5, 3]
hScores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

l = len(pScores)
nu = (l * sum(map(lambda x, y: x * y, pScores, hScores))) - ((sum(pScores) * sum(hScores)))
de = math.sqrt(((l * sum(map(lambda x: x ** 2, pScores))) - ((sum(pScores) ** 2))) * ((l * sum(map(lambda x: x ** 2, hScores))) - ((sum(hScores) ** 2))))

print "%.3f" % (nu / float(de))