def nth_triangular_number(n):
    if n == 1:
        return 1
    else:
        return n + nth_triangular_number(n - 1)

def print_triangular_triangle(n, current_row=1, current_number=1):
    if current_row > n:
        return
    else:
        if current_number <= current_row:
            print(current_number, end=" ")
            print_triangular_triangle(n, current_row, current_number + 1)
        else:
            print()
            print_triangular_triangle(n, current_row + 1, 1)

try:
    N = int(input("Digite um número natural (N): "))
    if N <= 0:
        print("Por favor, insira um número natural positivo.")
    else:
        nth_triangular = nth_triangular_number(N)
        print(f"O {N}-ésimo número triangular é {nth_triangular}.")
        print(f"Triângulo equivalente a {nth_triangular}:\n")
        print_triangular_triangle(N)
except ValueError:
    print("Entrada inválida. Por favor, insira um número natural válido.")
