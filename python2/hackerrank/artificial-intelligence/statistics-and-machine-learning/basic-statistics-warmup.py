# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = input()
arr = map(int, raw_input().split())

sarr = arr
sarr.sort()

uarr = list(set(sarr))
uarr.sort()

# Mean
meanVal = sum(arr) / float(n)
print "%.1f" % meanVal

# Median
if n % 2:
    medianVal = sarr[n / 2]
else:
    medianVal = ((sarr[(n / 2) - 1] + sarr[n / 2]) / float(2))
    
print medianVal

# Mode(s)
modeVal = max(uarr)
modeCnt = 0
for curVal in uarr:
    curCnt = uarr.count(curVal)
    if curCnt > modeCnt:
        modeVal = curVal
        modeCnt = curCnt
    elif curCnt == modeCnt:
        if modeVal > curVal:
            modeVal = curVal

print modeVal

# Standard Diviation
sdVal = (sum(map(lambda x: (x - float(meanVal)) ** 2, arr)) / float(n)) ** 0.5

print "%.1f" % sdVal
              
# Lower and Upper Boundary of Confidence Interval
seMean = float(sdVal) / math.sqrt(n)
ciVal = 1.96 * seMean

print "%.1f" % (float(meanVal) - ciVal), "%.1f" % (float(meanVal) + ciVal)