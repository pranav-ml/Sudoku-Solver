def next(x,y):
    if x==8:
        return 0,y+1
    return x+1,y

def subsqare(x,y):
    if y<=2:
        if x<=2:
            return 2,2
        if x <= 5:
            return 5,2
        if x<=8:
            return 8,2

    if y<=5:
        if x <= 2:
            return 2,5
        if x <= 5:
            return 5, 5
        if x <= 8:
            return 8,5

    if y<=8:
        if x <= 2:
            return 2,8
        if x <= 5:
            return 5,8
        if x <= 8:
            return 8, 8

def isPossible(board,x,y,n):
    for row in range(0,9):
        if board[row][x]==n:
            return False
        if board[y][row]==n:
            return False
    Xe,Ye=subsqare(x,y)
    Xs=Xe-2
    Ys=Ye-2
    for xx in range(Xs,Xe+1):
        for yy in range(Ys,Ye+1):
            if board[yy][xx]== n:
                return False
    return True





def solveSudokuHelper(board,x,y):
    if y==9:
        print("-------------------------------------------")
        for bb in board: print(*bb)
        print("-------------------------------------------")
        return True
    if board[y][x]>0:
        xt,yt=next(x,y)
        bools=solveSudokuHelper(board,xt,yt)
        return bools
    for ans in range(1,10):
        if isPossible(board,x,y,ans):
            board[y][x]=ans
            xt,yt=next(x,y)
            bools = solveSudokuHelper(board,xt,yt)
            board[y][x] = 0
    return False


def solveSudoku(board):
    return solveSudokuHelper(board,0,0)

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)

#sudoku examples

# 9 0 0 0 2 0 7 5 0
# 6 0 0 0 5 0 0 4 0
# 0 2 0 4 0 0 0 1 0
# 2 0 8 0 0 0 0 0 0
# 0 7 0 5 0 9 0 6 0
# 0 0 0 0 0 0 4 0 1
# 0 1 0 0 0 5 0 8 0
# 0 9 0 0 7 0 0 0 4
# 0 8 2 0 4 0 0 0 6


# 3 0 6 5 0 8 4 0 0
# 5 2 0 0 0 0 0 0 0
# 0 8 7 0 0 0 0 3 1
# 0 0 3 0 1 0 0 8 0
# 9 0 0 8 6 3 0 0 5
# 0 5 0 0 9 0 6 0 0
# 1 3 0 0 0 0 2 5 0
# 0 0 0 0 0 0 0 7 4
# 0 0 5 2 0 6 3 0 0


# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0


