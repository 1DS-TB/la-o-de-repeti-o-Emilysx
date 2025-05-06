import random

while True:
    print("----Joguinho----")
    print('1. Iniciar Game')
    print('2.Sair')
    opcao = input('Escolha: ')
    if opcao == '2':
        print('Até mais...1')
        break
    elif opcao == '1':
        hp = random.randint(200, 1000)
        ataque_jogador = random.randint(1,50)
        ataque_inimigo = random.randint(1,50)
        defesa_jogador = random.randint(1, ataque_inimigo)
        defesa_inimigo = random.randint(5, ataque_jogador)

        jogador = {
            "hp": hp,
            "ataque": ataque_jogador,
            "defesa": defesa_jogador
        }
        inimigo = {
            "hp": hp,
            "ataque": ataque_inimigo,
            "defesa": defesa_inimigo
        }
        while jogador['hp'] > 0 and inimigo ['hp'] > 0:
            print(f'Se o HP: {jogador['hp']} ')
            print(f'Seu ataque {jogador['ataque']}')
            print(f'Sua defesa {jogador['defesa']}')

            print(f'Se o HP: {inimigo['hp']} ')
            print(f'Seu ataque {inimigo['ataque']}')
            print(f'Sua defesa {inimigo['defesa']}')

            escolha = input('[1] Atacar [2] Curar ')

            if escolha == '1':
                dano = jogador['ataque'] - inimigo['defesa']
                inimigo ['hp'] = inimigo['hp'] - dano
                print(f'Você causou {dano} de dano')
                print(f'O inimigo ficou com {inimigo['hp']} de vida')
            elif escolha == '2':
                cura = 20
                if jogador['hp'] + cura > hp:
                    jogador['hp'] = hp
                else:
                    jogador['hp'] += cura
                print(f'Você ficou com {jogador['hp']} de vida')
            else:
                print('opção inválida')

            if inimigo['hp'] <= 0:
                print('Você venceu!')
                break

            escolha = random.choice(['1','2'])
            if escolha == '1':
                dano = inimigo['ataque'] - jogador['defesa']
                jogador['hp'] -= dano
                print(f'Você causou {dano} de dano')
                print(f'O jogador ficou com {jogador['hp']} de vida')
            elif escolha == '2':
                cura = 20
                if inimigo['hp'] + cura > hp:
                    inimigo['hp'] = hp
                else:
                    inimigo['inimigo'] += cura
            if inimigo['hp'] <= 0:
                print('Você perdeu')
                break