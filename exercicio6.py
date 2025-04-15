print("Esse programa vai gerar uma sequências de números de Fibonacci!!")
n = int(input("Insira um número de termos da sequência de Fibonacci que você deseja gerar: "))
a = 0
b = 1
print("Sequência de Fibonacci: ")
for _ in range(n):
    print(a)
    a, b = b, a + b
