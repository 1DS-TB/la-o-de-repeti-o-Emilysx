print("Esse programa verifica se o número é primo!!")
numero = int(input("Insira um número inteiro para verificar se ele é primo: "))

if numero <= 1:
    print("INVALIDO")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"Esse número não é primo.")
        break
    else:
        print(f"Esse número é primo.")



if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")