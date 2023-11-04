'''
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

'''
i=[0,1,2,3,4,5,6,7,8]
j=[0,1,2,3,4,5,6,7,8]
    ith
jth 00 01 02 03 04 05 06 07 08
    10 11 12 13 14 15 16 17 18
    20 21 22 23 24 25 26 27 28
    30 31 32 33 34 35 36 37 38
    40 41 42 43 44 45 46 47 48
    50 51 52 53 54 55 56 57 58
    60 61 62 63 64 65 66 67 68
    70 71 72 73 74 75 76 77 78
    80 81 82 83 84 85 86 87 88


logic:
ith loop
jth loop
need to check:
row wise i,j combination
column wise j,i combination
box wise first,second combination

ex:
i=0, 
j=[
0,1,2,
3,4,5,
6,7,8
]

need to get:
00 01 02
10 11 12
20 21 22

first=   3 * (i // 3)   +     j // 3
second=  3 * (i % 3)    +     j % 3

cell = board[first][second]

for checking duplicate values, use set
'''

from ast import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_row = set()
            seen_col = set()
            seen_subgrid = set()
            
            for j in range(9):
                # Check rows
                if board[i][j] != ".":
                    if board[i][j] in seen_row:
                        return False
                    seen_row.add(board[i][j])
                
                # Check columns
                if board[j][i] != ".":
                    if board[j][i] in seen_col:
                        return False
                    seen_col.add(board[j][i])
                
                # Check subgrids
                row_start, col_start = 3 * (i // 3), 3 * (i % 3)
                cell = board[row_start + j // 3][col_start + j % 3]
                if cell != ".":
                    if cell in seen_subgrid:
                        return False
                    seen_subgrid.add(cell)
        
        return True
