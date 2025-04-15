print("Esse programa vai encontar os números perfeitos entre 1 e 10000!!")
for num1 in range(1, 10001):
    soma_divisores = 0

    for i in range(1, num1):

        if num1 % i == 0:
            soma_divisores += i

    if soma_divisores == num1:
        print(num1)