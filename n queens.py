def isPossible(row, col, board, n):
    # Check-1 --> same row, left cols
    prevCol = col - 1
    while prevCol >= 0:
        if board[row][prevCol] == 1:
            return False
        prevCol -= 1

    # Check-2 --> left upper diagonal
    prevRow, prevCol = row - 1, col - 1
    while prevRow >= 0 and prevCol >= 0:
        if board[prevRow][prevCol] == 1:
            return False
        prevRow -= 1
        prevCol -= 1

    # Check-3 --> left lower diagonal
    nextRow, prevCol = row + 1, col - 1
    while nextRow < n and prevCol >= 0:
        if board[nextRow][prevCol] == 1:
            return False
        nextRow += 1
        prevCol -= 1

    return True


def solveThis(col, n, board, result):
    if col == n:
        # append to result
        currResult = []
        for i in range(n):
            word = ""
            for j in range(n):
                if board[i][j] == 1:
                    word += "Q"
                else:
                    word += "."
            currResult.append(word)
        result.append(currResult)
        return

    for row in range(n):
        if isPossible(row, col, board, n):
            board[row][col] = 1
            solveThis(col + 1, n, board, result)
            board[row][col] = 0


def solveNQueens(n):
    result = []
    board = [[0] * n for _ in range(n)]

    solveThis(0, n, board, result)
    return result

# Example usage:
print(solveNQueens(4))
