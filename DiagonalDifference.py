ef diagonalDifference(arr):
    return abs(sum([arr[i][i] for i in range(len(arr))]) - sum([arr[i][len(arr)-i-1] for i in range(len(arr))]))
