print("Esse programa vai mostrar a tabuada do número escolhido!!")
tabuada = int(input("Insira um número para ver sua tabuada de 1 a 10: "))

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")