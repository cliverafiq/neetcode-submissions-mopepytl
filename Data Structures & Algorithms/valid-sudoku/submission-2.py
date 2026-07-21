class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for c in range(9):
            for r in range(9):
                val = board[c][r]
                if val == ".":
                    continue
                
                b = (r//3) * 3 + (c//3)
                if val in col[c] or val in row[r] or val in box[b]:
                    return False
                
                col[c].add(val)
                row[r].add(val)
                box[b].add(val)
        return True
            


        