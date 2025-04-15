print("Esse programa vai imprimir um número no seguinte poadrão: *")
n = int(input("Insira um número para gerar o padrão: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()