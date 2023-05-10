def Laplace(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    determinante = 0

    for coluna in range(len(matriz)):

        submatriz = [linha[0:coluna] + linha[coluna + 1:] for linha in matriz[1:]]

        cofator = (-1) ** coluna * matriz[0][coluna]

        pre_determinante = Laplace(submatriz)

        determinante += cofator * pre_determinante

    return determinante


matriz = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]

determinante = Laplace(matriz)
print("O resultado da matriz 1:", determinante)

matriz = [[2, 1, 1, 1], [1, 3, 1, 1], [-1, 2, 2, -1], [1, 1, -1, 3]]

determinante = Laplace(matriz)
print("O resultado da matriz 2:", determinante)
