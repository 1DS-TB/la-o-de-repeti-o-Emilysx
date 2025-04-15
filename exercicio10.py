print("Esse programa vai encontar todos os números de Kaprekar em um intervalo definido pelo usuário!!")
inicio = int(input("Insira o início do intervalo: "))
fim = int(input("Insira o fim do intervalo: "))

print("Números de Kaprekar:")

for k in range(inicio, fim + 1):
    quadrado = str(k ** 2)
    tamanho = len(str(k))

    direita = quadrado[-tamanho:]

    esquerda = quadrado[:-tamanho]

    if direita == "" or int(direita) == 0:
        continue

    if esquerda == "":
        esquerda = "0"

    if int(esquerda) + int(direita) == k:
        print(k)
