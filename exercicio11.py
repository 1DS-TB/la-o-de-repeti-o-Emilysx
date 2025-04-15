import random
print("Este programa é um simulador de batalha entre você e um inimigo. Que vença o mais forte!")
print("=== DUELO DE HERÓIS ===")
hp = random.randint(200, 1000)
jogador_hp = hp
inimigo_hp = hp

jogador_atk = random.randint(1, 50)
jogador_def = random.randint(1, 50)

inimigo_atk = random.randint(1, 50)
inimigo_def = random.randint(1, 50)

print(f"Você - HP: {jogador_hp} | ATQ: {jogador_atk} | DEF: {jogador_def}")
print(f"Inimigo - HP: {inimigo_hp} | ATQ: {inimigo_atk} | DEF: {inimigo_def}")

turno = 1

while jogador_hp > 0 and inimigo_hp > 0:
    print(f"\n--- Turno {turno} ---")
    print(f"Seu HP: {jogador_hp} | Inimigo HP: {inimigo_hp}")

    acao = input("Sua vez - [1] Atacar | [2] Curar: ")

    if acao == "1":
        dano = max(0, jogador_atk - inimigo_def)
        inimigo_hp -= dano
        print(f"Você ataca! Inimigo perdeu {dano} HP.")

    elif acao == "2":
        cura = random.randint(15, 30)
        jogador_hp += cura
        print(f"Você se curou em {cura} HP.")

    else:
        print("Opção inválida. Você perdeu o turno.")

    if inimigo_hp <= 0:
        break

    inimigo_acao = random.choice(["atacar", "curar"])

    if inimigo_acao == "atacar":
        dano = max(0, inimigo_atk - jogador_def)
        jogador_hp -= dano
        print(f"Inimigo ataca! Você perdeu {dano} HP.")
    else:
        cura = random.randint(15, 30)
        inimigo_hp += cura
        print(f"Inimigo se curou em {cura} HP.")

    turno += 1

if jogador_hp > 0:
    print("\nVocê venceu o duelo!")
else:
    print("\nVocê perdeu o duelo!")
