def busca_binaria(data, target, low, high):
    if low > high:
        print("O limite inferior eh maior que o limite superior.")
        return False
    if (data[(low + high) // 2]) == target:
        print("Encontramos o target no index ", (low + high) // 2)
        return True
    if (target > data[(low + high) // 2]):
        print("O target esta acima de ", data[(low + high) // 2])
        print("Vou procurar entre ", data[((low + high) // 2) + 1], " ", data[high])
        return busca_binaria(data, target, ((low + high) // 2) + 1, high)
    if (target < data[(low + high) // 2]):
        print("O target esta abaixo de ", data[(low + high) // 2])
        print("Vou procurar entre ", data[low], " ", data[((low + high) // 2) - 1])
        return busca_binaria(data, target, low, ((low + high) // 2) - 1)

lista = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37] 

print(busca_binaria(lista, 22, 0, len(lista) - 1))