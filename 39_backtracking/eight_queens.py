size = 4    # indicate both row and column
results = [0] * size

def cal8queens(row):
    if row == size:
        printQueens(results)
        return

    for column in range(size):
        if isOK(results, row, column):
            results[row] = column
            cal8queens(row+1)

def isOK(results, ocuppied_rows, column):
    for i in range(ocuppied_rows):
        if results[i] == column or results[i] - i == column - ocuppied_rows or \
                results[i] + i == column + ocuppied_rows:

            return False

    return True

def printQueens(results):
    for row in range(size):
        line = ""
        for column in range(size):
            if results[row] == column:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

cal8queens(0)
printQueens(results)
