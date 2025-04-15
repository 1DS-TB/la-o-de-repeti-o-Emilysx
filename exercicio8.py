print("Esse programa vai calcular a soma da série harmônica!!")
n = int(input("Digite o valor de N: "))
soma = 0
for i in range(1, n + 1):
    soma += 1 / i

print(f"Soma da série harmônica até {n} termos: {soma:.2f}")