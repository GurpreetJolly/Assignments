import numpy as np;
#from assignment_20260221 import Assignment_2_matrix_multiplication as mm
import Assignment_2_matrix_multiplication as mm

def print_formatted(matrix):
    print("Formatted Result:")
    for row in matrix:
        print("\t".join(f"{value:.4f}" for value in row))

def main():
    print("\n*** Matrix Multiplication with Random numbers ***")
    matrix_a = np.random.rand(1000, 1000)
    matrix_b = np.random.rand(1000, 1000)
    print(f"Matrix A:\n{matrix_a}\n")
    print(f"Matrix B:\n{matrix_b}\n")
    result = mm.multiply_matrices(matrix_a, matrix_b)
    print("Result mutiplication of Matrix A and Matrix B:", result)
    print_formatted(result)

if __name__ == "__main__":
    main()
