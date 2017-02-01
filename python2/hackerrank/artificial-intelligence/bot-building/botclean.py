#!/usr/bin/python
def next_move(posr, posc, board):
    rT = -1
    cT = -1
    if board[posr][posc] == 'd':
        print "CLEAN"
    else:
        search = 1
        curr = posr
        curc = posc
        while search >= 0:
            if ((posr - search < 0) and (posr + search > 4) and
                (posc - search < 0) and (posc + search > 4)):
                break
               
            for i in xrange(posr - search, posr + search + 1):
                for j in xrange(posc - search, posc + search + 1):
                    if (i < 0) or (i > 4) or (j < 0) or (j > 4) or ((i == posr) and (j == posc)):
                        continue
                    if board[i][j] == 'd':
                        rT = i
                        cT = j
                        break

                if rT != -1:
                    break
            if rT != -1:
                break    
                    
            search += 1
            
        if rT != -1:
            if posr < rT:
                print "DOWN"
            elif posr > rT:
                print "UP"
            elif posc < cT:
                print "RIGHT"
            elif posc > cT:
                print "LEFT"
            
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    #board = [[j for j in raw_input().strip()] for i in range(5)]
    board = []
    for i in range(5):
        board.append([j for j in raw_input().strip()])
    next_move(pos[0], pos[1], board)
