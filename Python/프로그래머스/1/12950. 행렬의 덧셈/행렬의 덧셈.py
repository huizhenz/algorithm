def solution(arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2):
        row = []
        for col1, col2 in zip(row1, row2):
            row.append(col1+col2)
        answer.append(row)
    return answer