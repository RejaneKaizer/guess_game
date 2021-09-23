#Palavras secretas

secreta = 'horizonte'
digitadas = []
chances = 6

while True :
    if chances <= 0 :
        print ('Que pena! Você perdeu!')
        break

    letra = input (f'Digite uma letra (você pode errar mais {chances} vezes): ')

    if len(letra) > 1:
        print ('Ahhh, isso não vale, ein? Digite apenas 1 letra!')
        continue

    #digitadas.append(letra)

    if letra in secreta :
        print (f'UHULLLL. A letra "{letra}" ESTÁ na palavra!!')
        digitadas.append(letra)

    else :
        print (f'Que pena! A letra "{letra}" NÃO ESTÁ na palavra!')
        #digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreta :
        if letra_secreta in digitadas :
            secreto_temporario += letra_secreta

        else :
            secreto_temporario += '*'

    #print (secreto_temporario)

    if secreto_temporario == secreta :
        print (f'PARABÉNS, VOCÊ ACERTOU!!! A palavra era {secreta}')
        break

    else:
        print (f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreta:
        chances -= 1

    print()