class Solution:
    res = 0
    def findR(self,board):
        for i, line in enumerate(board):
            if 'R' in line:
                Rx = i
                Ry = line.index('R')
        return [Rx,Ry]
    
    def checkRight(self,Rpos,board):
        r = Rpos[1]
        resR = 0
        Rx = Rpos[0]
        while 0<=r<=7:
            if board[Rx][r]!='p' and board[Rx][r]!='B': 
                r += 1
            elif board[Rx][r]=='p':
                resR += 1
                break
            else:
                break
        return resR
            
    def checkLeft(self,Rpos,board):
        l = Rpos[1]
        resL = 0
        Rx = Rpos[0]
        while 0<=l<=7:
            if board[Rx][l]!='p' and board[Rx][l]!='B':
                l -= 1
            elif board[Rx][l]=='p':
                resL += 1
                break
            else:
                break
        return resL
        
    def checkUp(self,Rpos,board):
        u = Rpos[0]
        resU = 0
        Ry = Rpos[1]
        while 0<=u<=7:
            if board[u][Ry]!='p' and board[u][Ry]!='B':
                u += 1
            elif board[u][Ry]=='p':
                resU += 1
                break
            else:
                break
        return resU
        
    def checkDown(self,Rpos,board):
        d = Rpos[0]
        resD = 0
        Ry = Rpos[1]
        while 0<=d<=7:
            if board[d][Ry]!='p' and board[d][Ry]!='B':
                d -= 1
            elif board[d][Ry]=='p':
                resD += 1
                break
            else:
                break
        return resD
        
    def numRookCaptures(self, board):
        Rpos = self.findR(board)
        # print(Rpos)
        resR = self.checkRight(Rpos,board)
        resL = self.checkLeft(Rpos,board)
        resU = self.checkUp(Rpos,board)
        resD = self.checkDown(Rpos,board)
        res = resR+resL+resU+resD
        return res
        
if __name__ == '__main__':
    board=[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(Solution().numRookCaptures(board))

''' On an 8 x 8 chessboard, there is one white rook.  There also may be empty
squares, white bishops, and black pawns.  These are given as characters 'R',
'.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal
directions (north, east, west, and south), then moves in that direction until
it chooses to stop, reaches the edge of the board, or captures an opposite
colored pawn by moving to the same square it occupies.  Also, rooks cannot
move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],["
.",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".","."
,".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".","
.",".","."],[".",".",".",".",".",".",".","."]] Output: 3 Explanation:  The
rook can capture the pawns at positions b5, d6 and f5.
'''
        

        