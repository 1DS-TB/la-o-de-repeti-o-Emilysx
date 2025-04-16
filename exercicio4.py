print("Esse programa vai mostrar o fatorial do número escolhido!!")
numero = int(input("Insira um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("INVALIDO")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")