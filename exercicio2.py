print("Esse programa vai somar os do 1 até o número escolhido!!")
numero = int(input("Insira um número inteiro positivo: "))

soma = 0
contador = 1
if numero <= 0:
    print("INVALIDO\n")
elif numero >=1:
    while contador <= numero:
        soma += contador
        contador += 1

print(f"A soma de 1 até {numero} é: {soma}")
