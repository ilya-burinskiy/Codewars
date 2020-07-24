def read_matrix(n):
    A = []
    for _ in range(n):
        s = list(input().split())
        s = list(map(int, s))
        A.append(s)
    return A


def read_row(start_coords, 
             A, A_snailed,
             elements_to_read, 
             reverse_reading):

    i = start_coords[0]
    j = start_coords[1]
    result = False
    k = 0

    start = j
    if not reverse_reading:
        end = j + elements_to_read[0]
        for k in range(start, end):
            A_snailed.append(A[i][k])
        start_coords[0] = i + 1
    else:
        end = j - elements_to_read[0]
        for k in range(start, end, -1):
            A_snailed.append(A[i][k])
        start_coords[0] = i - 1
        result = True
     
    start_coords[1] = k
    elements_to_read[0] -= 1

    return result

def read_colunm(start_coords, 
                A, A_snailed,
                elements_to_read,
                reverse_reading):

    i = start_coords[0]
    j = start_coords[1]
    result = True 
    k = 0
    start = i

    if not reverse_reading:
        end = i + elements_to_read[0]
        for k in range(start, end):
            A_snailed.append(A[k][j])
        start_coords[1] = j - 1
    else:
        end = i - elements_to_read[0]
        for k in range(start, end, -1):
            A_snailed.append(A[k][j])
        start_coords[1] = j + 1
        result = False

    start_coords[0] = k

    return result


def snail_sort(A, n):
    reverse_row_reading = False
    reverse_column_reading = False

    elements_to_read = [n]
    start_coords = [0, 0]
    snailed_A = []
    while elements_to_read[0] > 0:
        reverse_column_reading = read_row(start_coords, 
                                          A, snailed_A,
                                          elements_to_read,
                                          reverse_row_reading)

        reverse_row_reading = read_colunm(start_coords,
                                           A, snailed_A, 
                                           elements_to_read,
                                           reverse_column_reading)

    return snailed_A    


def main():
    n = int(input())
    A = read_matrix(n)
    snailed_A = snail_sort(A, n)
    print(snailed_A)


if __name__ == '__main__':
    main()
