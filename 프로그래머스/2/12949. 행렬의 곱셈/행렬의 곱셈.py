def solution(arr1, arr2):
    # arr1의 행 수와 arr2의 열 수 계산
    rows_arr1 = len(arr1)
    cols_arr1 = len(arr1[0])
    rows_arr2 = len(arr2)
    cols_arr2 = len(arr2[0])

    result = [[0] * cols_arr2 for _ in range(rows_arr1)]

    # 행렬 곱셈
    for i in range(rows_arr1):
        for j in range(cols_arr2):
            for k in range(cols_arr1):  # arr1의 열 수 또는 arr2의 행 수
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result