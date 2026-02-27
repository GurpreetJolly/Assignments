import numpy as np

def multiply_matrices(matrix_a, matrix_b):
    matrix_a_row1_length = len(matrix_a)
    matrix_b_col1_length = len(matrix_b[0])

    if matrix_a_row1_length != matrix_b_col1_length:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    res = []
    for i in range(len(matrix_a)):
        res.append([])
        for j in range(len(matrix_b[i])):
            sum=0
            for k in range(len(matrix_b)):
                sum += matrix_a[i][k] * matrix_b[k][j]
            res[i].append(sum)

    return res

def main():
    print("\n*** Matrix Multiplication ***")
    print("This program implements it's own matrix multiplication algorithm without using any libraries.")
    print("In addition it checks the result with the built in function of numpy library.")
    matrix_a = [[1, 2, 3], [4, 5, 6]]
    matrix_b = [[7, 8], [9, 10], [11, 12]]
    print(f"Input Matrix A: {matrix_a}")
    print(f"Input Matrix B: {matrix_b}")
    result = multiply_matrices(matrix_a, matrix_b)
    print("Result of multiplying the matrices with our own implementation:")
    for row in result:
        print(row)

    # Check the result with numpy
    np_result = np.dot(matrix_a, matrix_b)
    np_result_1 = np.matmul(matrix_a, matrix_b)
    print("\nResult of multiplying the matrices with numpy Dot product:")
    print(np_result)
    print("\nResult of multiplying the matrices with numpy.matmul:")
    print(np_result_1)

if __name__ == "__main__":
    main()
