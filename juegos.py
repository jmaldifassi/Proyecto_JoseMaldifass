import api_1
import api_2
import api_3
import api_4
import api_5
import random
import imagenes_ahorcado

def adivinanzas(vidas_clues):
    while True:
        clues_game1 = [api_1.clue1_questions1_game_obj3,api_1.clue2_questions1_game_obj3, api_1.clue3_questions1_game_obj3]
        clues_game2 = [api_1.clue1_questions2_game_obj3,api_1.clue2_questions2_game_obj3, api_1.clue3_questions2_game_obj3]
        clues_game3 = [api_1.clue1_questions3_game_obj3,api_1.clue2_questions3_game_obj3, api_1.clue3_questions3_game_obj3]
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_1.name_game_obj3)
        print('Reglas del juego', api_1.rules_game_obj3)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print(api_1.question_questions1_game_obj3)
                print('\n')
                respuesta = input('Desea poner su respuesta\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    answer = input('Ingrese su respuesta\n> ')
                    print('\n')
                    if answer in api_1.answer_questions1_game_obj3:
                        print('Respuesta correcta\n\nGanaste')
                        return True
                    elif answer not in api_1.answer_questions1_game_obj3:
                        vidas_clues['vidas'] -= 0.5
                        print('Respuesta Incorrecta')
                        print('\n')
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game1) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1                           
                            print(clues_game1[0])
                            print('\n')
                            clues_game1.pop(0)
                            volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea poner otra respuesta o ver el enunciado de nuevo\n1.Volver al enunciado\n2.Poner otra respuesta\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                while respuesta == '2':
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1
                        print(clues_game1[0])
                        print('\n')
                        clues_game1.pop(0)
                        volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
                    if clue1 == '2':
                        volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
            while numero == '2':
                print(api_1.question_questions2_game_obj3)
                print('\n')
                respuesta = input('Desea poner su respuesta\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    answer = input('Ingrese su respuesta\n> ')
                    print('\n')
                    if answer in api_1.answer_questions2_game_obj3:
                        print('Respuesta correcta\n\nGanaste')
                        return True
                    elif answer not in api_1.answer_questions2_game_obj3:
                        vidas_clues['vidas'] -= 0.5
                        print('Respuesta Incorrecta')
                        print('\n')
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game2) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1                           
                            print(clues_game2[0])
                            print('\n')
                            clues_game2.pop(0)
                            volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea poner otra respuesta o ver el enunciado de nuevo\n1.Volver al enunciado\n2.Poner otra respuesta\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                while respuesta == '2':
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                        if len(clues_game2) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1
                        print(clues_game2[0])
                        print('\n')
                        clues_game2.pop(0)
                        volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
                    if clue1 == '2':
                        volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
            while numero == '3':
                print(api_1.question_questions3_game_obj3)
                print('\n')
                respuesta = input('Desea poner su respuesta\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    answer = input('Ingrese su respuesta\n> ')
                    print('\n')
                    if answer in api_1.answer_questions3_game_obj3:
                        print('Respuesta correcta\n\nGanaste')
                        return True
                    elif answer not in api_1.answer_questions3_game_obj3:
                        vidas_clues['vidas'] -= 0.5
                        print('Respuesta Incorrecta')
                        print('\n')
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game3) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1                           
                            print(clues_game3[0])
                            print('\n')
                            clues_game3.pop(0)
                            volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea poner otra respuesta o ver el enunciado de nuevo\n1.Volver al enunciado\n2.Poner otra respuesta\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                while respuesta == '2':
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                        if len(clues_game3) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1
                        print(clues_game3[0])
                        print('\n')
                        clues_game3.pop(0)
                        volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
                    if clue1 == '2':
                        volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
        else:
            break

def ahorcado(vidas_clues):
    while True:
        clues_game1 = [api_2.clue1_questions1_game_obj1,api_2.clue2_questions1_game_obj1,api_2.clue3_questions1_game_obj1]
        clues_game2 = [api_2.clue1_questions2_game_obj1,api_2.clue2_questions2_game_obj1,api_2.clue3_questions2_game_obj1]
        clues_game3 = [api_2.clue1_questions3_game_obj1,api_2.clue2_questions3_game_obj1,api_2.clue3_questions3_game_obj1]
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_2.name_game_obj1)
        print('Reglas del juego', api_2.rules_game_obj1)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print('La palabra del ahorcado esta relacionada con')
                print(api_2.question_questions1_game_obj1)
                print('Comienza a adivinar')
                palabra = (api_2.answer_questions1_game_obj1).lower()
                tupalabra = ''
                fallas = 0
                while fallas < 5:
                    si = input('Desea empezar a poner letras\n1.Si\n2.No\nIngresa el numero correspondiente a la opcion que desea\n> ')
                    while si != '1' and si != '2':
                        si = input('Por favor ingrese un numero valido\n> ')
                    while si == '1':
                        print('\n')
                        tupalabraOrdenada = ''
                        print('- - - Palabra - - -')
                        for letra in palabra:
                            if letra in tupalabra:
                                print(letra, end = '')
                                tupalabraOrdenada += letra                      
                            else:
                                print('-', end = '')
                                tupalabraOrdenada += '-'
                        if tupalabraOrdenada == palabra:
                            print('\n')
                            print('Ganaste :)')
                            return True
                        if fallas == 0:
                            print(imagenes_ahorcado.fallas0)
                        print('\n')
                        tuletra = input('Introduce una letra\n> ').lower()
                        while len(tuletra) != 1 :
                            tuletra = input('Por favor introduce una sola letra\n> ').lower()
                        tupalabra += tuletra
                        if tuletra not in palabra:
                            vidas_clues['vidas'] -= 0.25
                            fallas += 1
                            print('Te equivocaste')
                            if fallas == 1:
                                print(imagenes_ahorcado.fallas1)
                            elif fallas == 2:
                                print(imagenes_ahorcado.fallas2)
                            elif fallas == 3:
                                print(imagenes_ahorcado.fallas3)
                            elif fallas == 4:
                                print(imagenes_ahorcado.fallas4)
                            elif fallas == 5:
                                print(imagenes_ahorcado.fallas5)
                                print('Perdiste')
                                return False
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            while clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game1) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break
                                vidas_clues['clues'] -= 1
                                print(clues_game1[0])
                                print('\n')
                                clues_game1.pop(0)
                                volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                    while si == '2':
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game1) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1
                            print(clues_game1[0])
                            print('\n')
                            clues_game1.pop(0)
                            volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
            while numero == '2':
                print('La palabra del ahorcado esta relacionada con')
                print(api_2.question_questions2_game_obj1)
                print('Comienza a adivinar')
                palabra = (api_2.answer_questions2_game_obj1).lower()
                tupalabra = ''
                fallas = 0
                while fallas < 5:
                    si = input('Desea empezar a poner letras\n1.Si\n2.No\nIngresa el numero correspondiente a la opcion que desea\n> ')
                    while si != '1' and si != '2':
                        si = input('Por favor ingrese un numero valido\n> ')
                    while si == '1':
                        print('\n')
                        tupalabraOrdenada = ''
                        print('- - - Palabra - - -')
                        for letra in palabra:
                            if letra in tupalabra:
                                print(letra, end = '')
                                tupalabraOrdenada += letra                      
                            else:
                                print('-', end = '')
                                tupalabraOrdenada += '-'
                        if tupalabraOrdenada == palabra:
                            print('\n')
                            print('Ganaste :)')
                            return True
                        if fallas == 0:
                            print(imagenes_ahorcado.fallas0)
                        print('\n')
                        tuletra = input('Introduce una letra\n> ').lower()
                        while len(tuletra) != 1 :
                            tuletra = input('Por favor introduce una sola letra\n> ').lower()
                        tupalabra += tuletra
                        if tuletra not in palabra:
                            vidas_clues['vidas'] -= 0.25
                            fallas += 1
                            print('Te equivocaste')
                            if fallas == 1:
                                print(imagenes_ahorcado.fallas1)
                            elif fallas == 2:
                                print(imagenes_ahorcado.fallas2)
                            elif fallas == 3:
                                print(imagenes_ahorcado.fallas3)
                            elif fallas == 4:
                                print(imagenes_ahorcado.fallas4)
                            elif fallas == 5:
                                print(imagenes_ahorcado.fallas5)
                                print('Perdiste')
                                return False
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            while clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game2) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break
                                vidas_clues['clues'] -= 1
                                print(clues_game2[0])
                                print('\n')
                                clues_game2.pop(0)
                                volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                    while si == '2':
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game2) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1
                            print(clues_game2[0])
                            print('\n')
                            clues_game2.pop(0)
                            volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
            while numero == '3':
                print('La palabra del ahorcado esta relacionada con')
                print(api_2.question_questions3_game_obj1)
                print('Comienza a adivinar')
                palabra = (api_2.answer_questions3_game_obj1).lower()
                tupalabra = ''
                fallas = 0
                while fallas < 5:
                    si = input('Desea empezar a poner letras\n1.Si\n2.No\nIngresa el numero correspondiente a la opcion que desea\n> ')
                    while si != '1' and si != '2':
                        si = input('Por favor ingrese un numero valido\n> ')
                    while si == '1':
                        print('\n')
                        tupalabraOrdenada = ''
                        print('- - - Palabra - - -')
                        for letra in palabra:
                            if letra in tupalabra:
                                print(letra, end = '')
                                tupalabraOrdenada += letra                      
                            else:
                                print('-', end = '')
                                tupalabraOrdenada += '-'
                        if tupalabraOrdenada == palabra:
                            print('\n')
                            print('Ganaste :)')
                            return True
                        if fallas == 0:
                            print(imagenes_ahorcado.fallas0)
                        print('\n')
                        tuletra = input('Introduce una letra\n> ').lower()
                        while len(tuletra) != 1 :
                            tuletra = input('Por favor introduce una sola letra\n> ').lower()
                        tupalabra += tuletra
                        if tuletra not in palabra:
                            vidas_clues['vidas'] -= 0.25
                            fallas += 1
                            print('Te equivocaste')
                            if fallas == 1:
                                print(imagenes_ahorcado.fallas1)
                            elif fallas == 2:
                                print(imagenes_ahorcado.fallas2)
                            elif fallas == 3:
                                print(imagenes_ahorcado.fallas3)
                            elif fallas == 4:
                                print(imagenes_ahorcado.fallas4)
                            elif fallas == 5:
                                print(imagenes_ahorcado.fallas5)
                                print('Perdiste')
                                return False
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            while clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game3) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break
                                vidas_clues['clues'] -= 1
                                print(clues_game3[0])
                                print('\n')
                                clues_game3.pop(0)
                                volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                    while si == '2':
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game3) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1
                            print(clues_game3[0])
                            print('\n')
                            clues_game3.pop(0)
                            volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
        else: 
            break

import random

def criptograma(vidas_clues):
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_2.name_game_obj3)
        print('Reglas del juego', api_2.rules_game_obj3)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print('Debe desifrar lo que dice la frase')
                respuesta_1 = (api_2.question_questions1_game_obj3).lower()
                respuesta = respuesta_1.replace('á', 'a')
                r1 = respuesta.replace('u', 'w')
                r2 = r1.replace('i', 'k')
                r3 = r2.replace('t', 'v')
                r4 = r3.replace('g', 'i')
                r5 = r4.replace('e', 'g')
                r6 = r5.replace('r', 't')
                r7 = r6.replace('a', 'c')
                r8 = r7.replace('d', 'f')
                r9 = r8.replace('s', 'u')
                r10 = r9.replace('p', 'r')
                r11 = r10.replace('n', 'p')
                r12 = r11.replace('m', 'o')
                r13 = r12.replace('l', 'n')
                print(r13)
                answer = input('Ingrese su respuesta\n> ')
                print('\n')
                if answer == respuesta:
                    print('Respuesta correcta')
                    return True
                else:
                    print('Respuesta incorrecta')
                    print('Partida perdida')
                    vidas_clues['vidas'] -= 1
                    break
            while numero == '2':
                print('Debe desifrar lo que dice la frase')
                respuesta_1 = (api_2.question_questions2_game_obj3).lower()
                respuesta = respuesta_1.replace('á', 'a')
                r1 = respuesta.replace('u', 'y')
                r2 = r1.replace('m', 'q')
                r3 = r2.replace('t', 'x')
                r4 = r3.replace('g', 'k')
                r5 = r4.replace('i', 'm')
                r6 = r5.replace('r', 'v')
                r7 = r6.replace('e', 'i')
                r8 = r7.replace('d', 'h')
                r9 = r8.replace('s', 'w')
                r10 = r9.replace('p', 't')
                r11 = r10.replace('n', 'r')
                r12 = r11.replace('a', 'e')
                r13 = r12.replace('l', 'p')
                print(r13)
                answer = input('Ingrese su respuesta\n> ')
                print('\n')
                if answer == respuesta:
                    print('Respuesta correcta')
                    return True
                else:
                    print('Respuesta incorrecta')
                    print('Partida perdida')
                    vidas_clues['vidas'] -= 1
                    break
            while numero == '3':
                print('Debe desifrar lo que dice la frase')
                respuesta_1 = (api_2.question_questions2_game_obj3).lower()
                respuesta = respuesta_1.replace('á', 'a')
                r1 = respuesta.replace('u', 'z')
                r2 = r1.replace('r', 'w')
                r3 = r2.replace('t', 'y')
                r4 = r3.replace('l', 'q')
                r5 = r4.replace('s', 'x')
                r6 = r5.replace('m', 'r')
                r7 = r6.replace('e', 'j')
                r8 = r7.replace('n', 's')
                r9 = r8.replace('i', 'n')
                r10 = r9.replace('p', 'u')
                r11 = r10.replace('d', 'i')
                r12 = r11.replace('a', 'f')
                r13 = r12.replace('g', 'l')
                print(r13)
                answer = input('Ingrese su respuesta\n> ')
                print('\n')
                if answer == respuesta:
                    print('Respuesta correcta')
                    return True
                else:
                    print('Respuesta incorrecta')
                    print('Partida perdida')
                    print('\n')
                    vidas_clues['vidas'] -= 1
                    break
        else:
            break

def logica(vidas_clues):
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_3.name_game_obj1)
        print('Reglas del juego', api_3.rules_game_obj1)
        print('\n')
        listo = input('Estas listo para jugar? (Si dices que no saldras del saman y al volver a entrar perderas otra vida)\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2'))
            while numero == '1':
                print('Resuelva el sistema con logica')
                respuesta = '67'
                print(api_3.question_questions1_game_obj1)
                answer = input('Ingrese su respuesta\n> ')
                print('\n')
                if answer == respuesta:
                    print('Respuesta correcta')
                    return True
                else:
                    vidas_clues['vidas'] -= 1
                    print('Respuesta incorrecta')
                    print('\n')
                    print('Partida perdida')
                    break
            while numero == '2':
                print('Resuelva el sistema con logica')
                respuesta = '41'
                print(api_3.question_questions2_game_obj1)
                answer = input('Ingrese su respuesta\n> ')
                print('\n')
                if answer == respuesta:
                    print('Respuesta correcta')
                    return True
                else:
                    vidas_clues['vidas'] -= 1
                    print('Respuesta incorrecta')
                    print('\n')
                    print('Partida perdida')
                    break
        else:
            break

def crear_tablero():
    tablero = [
        [" X "," X "," X "," X "],
        [" X "," X "," X "," X "],
        [" X "," X "," X "," X "],
        [" X "," X "," X "," X "]]
    for i in tablero:
        for j in i:
            print(j," ",end="")
        print()
    return tablero

def mostrar(a, b, tablero, matriz):
    tablero[b-1][a-1] = matriz[a-1][b-1]
    for i in tablero:
        print()
        for j in i:
            print(j," ",end="")
        print()
    return tablero[b-1][a-1]

def limpiar(a1, b1, a2, b2, tablero):
    tablero[b1-1][a1-1] = " X "
    tablero[b2-1][a2-1] = " X "
    for i in tablero:
        for j in i:
            print(j," ",end="")
        print()
    
def validar(a, b, a2, b2, tablero):
    if a<1 or a>4 or b<1 or b>4 or tablero[b-1][a-1] != " X ":
        print('Posición inválida')
        return False
    elif a == a2 and b == b2:
        print('Esa posicion ya se uso')
        return False
    else:
        return True

def chequear_movimientos(tablero):
    guiones = 0
    for i in tablero:
        for j in i:
            if j == " X ":
                guiones += 1
    return guiones


def memoria(vidas_clues):
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_3.name_game_obj3)
        print('Reglas del juego', api_3.rules_game_obj3)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            while True:
                matriz = [
                ['😀', '🙄', '🤮', '🥰'], 
                ['🤮', '😨', '🤓', '😷'], 
                ['😨', '🤓', '🥰', '😷'], 
                ['🤑', '🤑', '🙄', '😀']]
                random.shuffle(matriz)
                guiones = 0
                print('''
- - - Memoria con Emojis 🤓 - - -
Binvenido a memoria, para jugar deberas indicar las coordenadas de la X que deseas voltar,
primero colocando la fila en la que se encuentra y despues la columna, esto para dos X, 
si estas son igual se quedaran volteadas, si no se pondran de nuevo las X, si acertas todas 
las parejas de emojis ganaras.
''')
                tablero = crear_tablero()
                while True:
                    valido1 = False
                    valido2 = False
                    while valido1 == False:
                        print('\n')
                        a1 = input('Ingrese el numero de la fila del primer emoji que desea voltear\n> ')
                        while not (a1.isnumeric()) or (int(a1) not in range(1,5)):
                            a1 = input('Por favor, ingrese un numero corresponiente a una fila valido (1-4)\n> ')
                        b1 = (input('Ingrese el numero de la columna del primer emoji que desea voltear\n> '))
                        while not (b1.isnumeric()) or (int(b1) not in range(1,5)):
                            b1 = (input('Por favor, ingrese un numero corresponiente a una columna valido (1-4)\n> '))
                        a1 = int(a1)
                        b1 = int(b1)
                        valido1 = validar(a1, b1, -1, -1, tablero)
                    print('\n')
                    print(f'El emoji de la posicion que escogiste es\n> {matriz[a1-1][b1-1]}')
                    tabla1 = mostrar(a1,b1,tablero,matriz)
                    while valido2 == False:
                        print('\n')
                        a2 = (input('Ingrese el numero de la fila del segundo emoji que desea voltear\n> '))
                        while not (a2.isnumeric()) or (int(a2) not in range(1,5)):
                            a2 = (input('Por favor, ingrese un numero corresponiente a una fila valido (1-4)\n> '))
                        b2 = (input('Ingrese el numero de la columna del segundo emoji que desea voltear\n> '))
                        while not (b2.isnumeric()) or (int(b2) not in range(1,5)):
                            b2 = (input('Por favor, ingrese un numero corresponiente a una columna valido (1-4)\n> '))
                        a2 = int(a2)
                        b2 = int(b2)
                        valido2 = validar(a2, b2, a1, b1, tablero)
                    print('\n')
                    print(f'El emoji de la posicion que escogiste es\n> {matriz[a2-1][b2-1]}')
                    tabla2 = mostrar(a2,b2,tablero,matriz)
                    if tabla1 == tabla2:
                        print('\n')
                        print('Encontraste la pareja de emojis, continua asi')
                    else:
                        vidas_clues['vidas'] -= 0.25
                        print('\n')
                        print('No encontraste, sigue intentando')
                        limpiar(a1, b1, a2, b2, tablero)
                    if chequear_movimientos(tablero) == 0:
                        print('Ganaste, encontraste todas las parjas de emojis')
                        return True
        else:
            break

def numero_entre(vidas_clues):
    clues_game1 = [api_5.clue1_questions3_game_obj3]
    while True:
        errores = 0
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_5.name_game_obj3)
        print('Reglas del juego', api_5.rules_game_obj3)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        while listo == '1':
            print('''
- - - Escoge un numero entre - - - 
Bienvenido a escoge un numero entre, en este juego tendras que
escoger un numero entre 1-15, si aciertas el numero ganaras, tienes
muchas oportunidades, pero por vez que no aciertes se te quitara vida           
''')
            print(api_5.question_questions1_game_obj3)
            num_random = random.randrange(1,16)
            while True:
                print('\n')
                answer = input('Ingrese el numero\n> ')
                while (not answer.isnumeric()) or (int(answer) not in range(1,16)):
                    answer = input('Por favor ingese un numero valido (1-15)\n> ')
                answer = int(answer)
                if answer == num_random:
                    print('Respuesta correcta\nGanaste')
                    return True
                else:
                    errores += 1
                    errores3 = errores / 3
                    if errores3 == 1:
                        vidas_clues['vidas'] -= 0.25
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                            print('Te quedaste sin pistas')
                            break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1                           
                        print('\n')
                        clues_game1.pop(0)
                        num_bajo = num_random - 4
                        num_arriba = num_random + 4
                        if answer in range(num_bajo,num_random):
                            print('Estas cerca un poco abajo')
                        elif answer in range(num_random, num_arriba):
                            print('Estas cerca un poco arriba')
                        elif answer in range (1,num_bajo):
                            print('Estas muy abajo')
                        elif answer in range(num_arriba,16):
                            print('Estas muy arriba')
                        break

def palabra_mezclada(vidas_clues):
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_5.name_game_obj2)
        print('Reglas del juego', api_5.rules_game_obj2)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print('''
- - - Palabra mezcalda - - - 
Bienvenido a palabra mezcalda, se te va a dar una cartegoria, y 5 palbras
estas palbras no van a estar bien escritas, si no que van a estar mezcladas y 
se te van a mostrar una a una para que intentes responder con la palbra que es.
Si tienes todas las palbaras correctas, Ganas.           
''')            
                lista_palabras = api_5.words_questions1_game_obj2
                mezclar = [''.join(random.sample(palabra, len(palabra))) for palabra in lista_palabras]
                print('Aca esta la lista de palabras\n', mezclar)
                for palabra in mezclar:
                    palabra1 = mezclar[0]
                    palabra2 = mezclar[1]
                    palabra3 = mezclar[2]
                    palabra4 = mezclar[3]
                    palabra5 = mezclar[4]
                print('\n')
                respuesta = input('Desea comenzar a responder\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    print('Primera palabra\n', palabra1)
                    print('\n')
                    palabra_1 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                    print('\n')
                    if palabra_1 == 'sarten':
                        print('Respuesta correcta')
                        print('\n')
                        print('Siguiente palabra\n', palabra2)
                        print('\n')
                        palabra_2 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                        print('\n')
                        if palabra_2 == 'paleta':
                            print('Respuesta correcta')
                            print('\n')
                            print('Siguiente palabra\n', palabra3)
                            print('\n')
                            palabra_3 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                            print('\n')
                            if palabra_3 == 'olla':
                                print('Respuesta correcta')
                                print('\n')
                                print('Siguiente palabra\n', palabra4)
                                print('\n')
                                palabra_4 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                                print('\n')
                                if palabra_4 == 'vaso':
                                    print('Respuesta correcta')
                                    print('\n')
                                    print('Siguiente palabra\n', palabra5)
                                    print('\n')
                                    palabra_5 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                                    print('\n')
                                    if palabra_5 == 'hornilla':
                                        print('Perfecto, acertaste todas, Ganaste')
                                        return True
                                    while palabra_5 != 'hornilla':
                                        print('Respuesta incorrecta')
                                        print('\n')
                                        vidas_clues['vidas'] -= 0.5
                                        print('Intenta de nuevo')
                                        print('\n')
                                        break
                                while palabra_4 != 'vaso':
                                    print('Respuesta incorrecta')
                                    print('\n')
                                    vidas_clues['vidas'] -= 0.5
                                    print('Intenta de nuevo')
                                    print('\n')
                                    break
                            while palabra_3 != 'olla':
                                print('Respuesta incorrecta')
                                print('\n')
                                vidas_clues['vidas'] -= 0.5
                                print('Intenta de nuevo')
                                print('\n')
                                break
                        while palabra_2 != 'paleta':
                            print('Respuesta incorrecta')
                            print('\n')
                            vidas_clues['vidas'] -= 0.5
                            print('Intenta de nuevo')
                            print('\n')
                            break
                    while palabra_1 != 'sarten':
                        print('Respuesta incorrecta')
                        print('\n')
                        vidas_clues['vidas'] -= 0.5
                        print('Intenta de nuevo')
                        print('\n')
                        break
            while numero == '2':
                print('''
- - - Palabra mezcalda - - - 
Bienvenido a palabra mezcalda, se te va a dar una cartegoria, y 5 palbras
estas palbras no van a estar bien escritas, si no que van a estar mezcladas y 
se te van a mostrar una a una para que intentes responder con la palbra que es.
Si tienes todas las palbaras correctas, Ganas.           
''')            
                lista_palabras = api_5.words_questions2_game_obj2
                mezclar = [''.join(random.sample(palabra, len(palabra))) for palabra in lista_palabras]
                print('Aca esta la lista de palabras\n', mezclar)
                for palabra in mezclar:
                    palabra1 = mezclar[0]
                    palabra2 = mezclar[1]
                    palabra3 = mezclar[2]
                    palabra4 = mezclar[3]
                    palabra5 = mezclar[4]
                print('\n')
                respuesta = input('Desea comenzar a responder\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    print('Primera palabra\n', palabra1)
                    print('\n')
                    palabra_1 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                    print('\n')
                    if palabra_1 == 'poceta':
                        print('Respuesta correcta')
                        print('\n')
                        print('Siguiente palabra\n', palabra2)
                        print('\n')
                        palabra_2 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                        print('\n')
                        if palabra_2 == 'cepillo':
                            print('Respuesta correcta')
                            print('\n')
                            print('Siguiente palabra\n', palabra3)
                            print('\n')
                            palabra_3 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                            print('\n')
                            if palabra_3 == 'afeitadora':
                                print('Respuesta correcta')
                                print('\n')
                                print('Siguiente palabra\n', palabra4)
                                print('\n')
                                palabra_4 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                                print('\n')
                                if palabra_4 == 'regadera':
                                    print('Respuesta correcta')
                                    print('\n')
                                    print('Siguiente palabra\n', palabra5)
                                    print('\n')
                                    palabra_5 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                                    print('\n')
                                    if palabra_5 == 'grifo':
                                        print('Perfecto, acertaste todas, Ganaste')
                                        return True
                                    while palabra_5 != 'grifo':
                                        print('Respuesta incorrecta')
                                        print('\n')
                                        vidas_clues['vidas'] -= 0.5
                                        print('Intenta de nuevo')
                                        print('\n')
                                        break
                                while palabra_4 != 'regadera':
                                    print('Respuesta incorrecta')
                                    print('\n')
                                    vidas_clues['vidas'] -= 0.5
                                    print('Intenta de nuevo')
                                    print('\n')
                                    break
                            while palabra_3 != 'afeitadora':
                                print('Respuesta incorrecta')
                                print('\n')
                                vidas_clues['vidas'] -= 0.5
                                print('Intenta de nuevo')
                                print('\n')
                                break
                        while palabra_2 != 'cepillo':
                            print('Respuesta incorrecta')
                            print('\n')
                            vidas_clues['vidas'] -= 0.5
                            print('Intenta de nuevo')
                            print('\n')
                            break
                    while palabra_1 != 'poceta':
                        print('Respuesta incorrecta')
                        print('\n')
                        vidas_clues['vidas'] -= 0.5
                        print('Intenta de nuevo')
                        print('\n')
                        break
            while numero == '3':
                print('''
- - - Palabra mezcalda - - - 
Bienvenido a palabra mezcalda, se te va a dar una cartegoria, y 5 palbras
estas palbras no van a estar bien escritas, si no que van a estar mezcladas y 
se te van a mostrar una a una para que intentes responder con la palbra que es.
Si tienes todas las palbaras correctas, Ganas.           
''')            
                lista_palabras = api_5.words_questions3_game_obj2
                mezclar = [''.join(random.sample(palabra, len(palabra))) for palabra in lista_palabras]
                print('Aca esta la lista de palabras\n', mezclar)
                for palabra in mezclar:
                    palabra1 = mezclar[0]
                    palabra2 = mezclar[1]
                    palabra3 = mezclar[2]
                    palabra4 = mezclar[3]
                    palabra5 = mezclar[4]
                print('\n')
                respuesta = input('Desea comenzar a responder\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    print('Primera palabra\n', palabra1)
                    print('\n')
                    palabra_1 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                    print('\n')
                    if palabra_1 == 'zumba':
                        print('Respuesta correcta')
                        print('\n')
                        print('Siguiente palabra\n', palabra2)
                        print('\n')
                        palabra_2 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                        print('\n')
                        if palabra_2 == 'salsa':
                            print('Respuesta correcta')
                            print('\n')
                            print('Siguiente palabra\n', palabra3)
                            print('\n')
                            palabra_3 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                            print('\n')
                            if palabra_3 == 'flamengo':
                                print('Respuesta correcta')
                                print('\n')
                                print('Siguiente palabra\n', palabra4)
                                print('\n')
                                palabra_4 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                                print('\n')
                                if palabra_4 == 'tango':
                                    print('Respuesta correcta')
                                    print('\n')
                                    print('Siguiente palabra\n', palabra5)
                                    print('\n')
                                    palabra_5 = input('Ingrese la palabra que usted crea que es\n> ').lower()
                                    print('\n')
                                    if palabra_5 == 'perreo':
                                        print('Perfecto, acertaste todas, Ganaste')
                                        return True
                                    while palabra_5 != 'perreo':
                                        print('Respuesta incorrecta')
                                        print('\n')
                                        vidas_clues['vidas'] -= 0.5
                                        print('Intenta de nuevo')
                                        print('\n')
                                        break
                                while palabra_4 != 'tango':
                                    print('Respuesta incorrecta')
                                    print('\n')
                                    vidas_clues['vidas'] -= 0.5
                                    print('Intenta de nuevo')
                                    print('\n')
                                    break
                            while palabra_3 != 'flamengo':
                                print('Respuesta incorrecta')
                                print('\n')
                                vidas_clues['vidas'] -= 0.5
                                print('Intenta de nuevo')
                                print('\n')
                                break
                        while palabra_2 != 'salsa':
                            print('Respuesta incorrecta')
                            print('\n')
                            vidas_clues['vidas'] -= 0.5
                            print('Intenta de nuevo')
                            print('\n')
                            break
                    while palabra_1 != 'zumba':
                        print('Respuesta incorrecta')
                        print('\n')
                        vidas_clues['vidas'] -= 0.5
                        print('Intenta de nuevo')
                        print('\n')
                        break
        else:
            break

import sympy
import math 

def preguntas_mate(vidas_clues):
    clues_game1 = [api_2.clue1_questions3_game_obj2]
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_2.name_game_obj2)
        print('Reglas del juego', api_2.rules_game_obj2)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print(api_2.question_questions1_game_obj2)
                print('\n')
                x = sympy.Symbol('x')
                pi = math.pi
                y = sympy.sin(x)/2
                derivada = y.diff(x)
                derivada_nueva = derivada.replace(x, pi)
                derivada_nueva = round(derivada_nueva, 1)
                derivada_nueva = str(derivada_nueva)
                answer = input('Ingrese su respuesta (En numeros decimales, con 1 decimal y con punto (.))\n> ')
                print('\n') 
                if answer == derivada_nueva:
                    print('Respuesta correcta\nGanaste')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('Respuesta Incorrecta')
                    print('\n')
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                            print('Te quedaste sin pistas')
                            break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1                           
                        print(clues_game1[0])
                        print('\n')
                        clues_game1.pop(0)
                        volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
            while numero == '2':
                print(api_2.question_questions2_game_obj2)
                x = sympy.Symbol('x')
                pi = math.pi
                y = ((sympy.cos(x)/2) - (sympy.tan(x)/5))
                derivada = y.diff(x)
                print('\n') 
                derivada_nueva = derivada.replace(x, pi)
                derivada_nueva = round(derivada_nueva, 1)
                derivada_nueva = str(derivada_nueva)
                answer = input('Ingrese su respuesta (En numeros decimales, con 1 decimal y con punto (.))\n> ')
                print('\n') 
                if answer == derivada_nueva:
                    print('Respuesta correcta\nGanaste')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('Respuesta Incorrecta')
                    print('\n')
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                            print('Te quedaste sin pistas')
                            break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['vidas'] -= 1                           
                        print(clues_game1[0])
                        print('\n')
                        clues_game1.pop(0)
                        volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
            while numero == '3':
                print(api_2.question_questions3_game_obj2)
                x = sympy.Symbol('x')
                pi = math.pi
                y = ((sympy.sin(x)/5) - (sympy.tan(x)))
                derivada = y.diff(x)
                print('\n') 
                derivada_nueva = derivada.replace(x, pi/3)
                derivada_nueva = round(derivada_nueva, 1)
                derivada_nueva = str(derivada_nueva)
                answer = input('Ingrese su respuesta (En numeros decimales, con 1 decimal y con punto (.))\n> ')
                print('\n') 
                if answer == derivada_nueva:
                    print('Respuesta correcta\nGanaste')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('Respuesta Incorrecta')
                    print('\n')
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                            print('Te quedaste sin pistas')
                            break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1                           
                        print(clues_game1[0])
                        print('\n')
                        clues_game1.pop(0)
                        volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
        else:
            break

def preguntas_python(vidas_clues):
    clues_game1 = [api_1.clue1_questions1_game_obj2, api_1.clue2_questions1_game_obj2, api_1.clue3_questions1_game_obj2]
    clues_game1 = [api_1.clue1_questions2_game_obj2]
    answers1 = ['frase_nueva = float(frase[frase.index("5"):frase.index(",")])', 'frase_nueva=float(frase[frase.index("5"):frase.index(",")])', 'frase_nueva= float(frase[frase.index("5"):frase.index(",")])']
    answers2 = ['frase_v = " ".join(w[::-1] for w in frase.split())', 'frase_v=" ".join(w[::-1] for w in frase.split())', 'frase_v= " ".join(w[::-1] for w in frase.split())']
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_1.name_game_obj2)
        print('Reglas del juego', api_1.rules_game_obj2)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2'))
            while numero == '1':
                print(api_1.question_questions1_game_obj2)
                print('A partrir de que tienes esta frase')
                print('frase = "tengo en mi cuenta 50,00 $"')
                answer = input('Ingrese aqui la linea de codigo, separndo las variables por /\n\n> ')
                if answer in answers1:
                    print('\n')
                    print('Respuesta correcta\nGanaste')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('Respuesta incorrecta')
                    print('\n')
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                            print('Te quedaste sin pistas')
                            break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1                           
                        print(clues_game1[0])
                        print('\n')
                        clues_game1.pop(0)
                        volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
            while numero == '2':
                print(api_1.question_questions2_game_obj2)
                print('A partrir de que tienes esta frase')
                print('frase = "oidutse ne al ortem aireinegni ed sametsis"')
                answer = input('Ingrese aqui la linea de codigo y haga que el resultado sea frase_v\nEjemplo: frase_v = float(frase[frase.index("5"):frase.index(",")])\n> ')
                if answer in answers2 :
                    print('Respuesta correcta\nGanaste')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('Respuesta incorrecta')
                    print('\n')
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if vidas_clues['clues'] <= 0:
                            print('Te quedaste sin pistas')
                            break
                        if len(clues_game1) == 0:
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1                           
                        print(clues_game1[0])
                        print('\n')
                        clues_game1.pop(0)
                        volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
        else:
            break

def quiz_cultura_unimetana(vidas_clues):
    clues_game1 = [api_3.clue1_questions1_game_obj2]
    clues_game2 = [api_3.clue1_questions2_game_obj2]
    clues_game3 = [api_3.clue1_questions3_game_obj2]
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_3.name_game_obj2)
        print('Reglas del juego', api_3.rules_game_obj2)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                while True:
                    print(api_3.question_questions1_game_obj2)
                    print('a.', api_3.correctanswer_questions1_game_obj2)
                    print('b.', api_3.answer1_questions1_game_obj2)
                    print('c.', api_3.answer2_questions1_game_obj2)
                    print('d.', api_3.answer3_questions1_game_obj2)
                    print('\n')
                    respuesta = input('Desea poner su respuesta\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while respuesta != '1' and respuesta != '2':
                        respuesta = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while respuesta == '1':
                        answer = input('Ingrese la letra correspondiente a la respuesta que desea\n> ')
                        while answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd':
                            answer = input('Por favor ingrese una letra valida\n> ')
                        print('\n')
                        if answer == 'a':
                            print('Respuesta correcta')
                            return True
                        else:
                            vidas_clues['vidas'] -= 0.5
                            print('Respuesta Incorrecta')
                            print('\n')
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            while clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game1) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break
                                vidas_clues['clues'] -= 1                           
                                print(clues_game1[0])
                                print('\n')
                                clues_game1.pop(0)
                                volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                            if clue1 == '2':
                                volver = input('Desea poner otra respuesta o ver el enunciado de nuevo\n1.Volver al enunciado\n2.Poner otra respuesta\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                    while respuesta == '2':
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game1) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1
                            print(clues_game1[0])
                            print('\n')
                            clues_game1.pop(0)
                            volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
            while numero == '2':
                print(api_3.question_questions2_game_obj2)
                print('a.', api_3.answer2_questions2_game_obj2)
                print('b.', api_3.answer1_questions2_game_obj2)
                print('c.', api_3.correctanswer_questions2_game_obj2)
                print('d.', api_3.answer3_questions2_game_obj2)
                print('\n')
                respuesta = input('Desea poner su respuesta\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                print('\n')
                while respuesta != '1' and respuesta != '2':
                    respuesta = input('Por favor ingrese un numero valido\n> ')
                    print('\n')
                while respuesta == '1':
                    answer = input('Ingrese la letra correspondiente a la respuesta que desea\n> ')
                    while answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd':
                        answer = input('Por favor ingrese una letra valida\n> ')
                    print('\n')
                    if answer == 'c':
                        print('Respuesta correcta')
                        return True
                    else:
                        vidas_clues['vidas'] -= 0.5
                        print('Respuesta Incorrecta')
                        print('\n')
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game2) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1                           
                            print(clues_game2[0])
                            print('\n')
                            clues_game2.pop(0)
                            volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea poner otra respuesta o ver el enunciado de nuevo\n1.Volver al enunciado\n2.Poner otra respuesta\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                while respuesta == '2':
                    clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while clue1 != '1' and clue1 != '2':
                        clue1 = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while clue1 == '1':
                        if len(clues_game2) == 0:
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            print('Te quedaste sin pistas')
                            print('\n')
                            break
                        vidas_clues['clues'] -= 1
                        print(clues_game2[0])
                        print('\n')
                        clues_game2.pop(0)
                        volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
                    if clue1 == '2':
                        volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while volver != '1' and volver != '2':
                            volver = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        if volver == '1':
                            break
            while numero == '3':
                while True:
                    print(api_3.question_questions3_game_obj2)
                    print('a.', api_3.answer3_questions3_game_obj2)
                    print('b.', api_3.answer1_questions3_game_obj2)
                    print('c.', api_3.answer2_questions3_game_obj2)
                    print('d.', api_3.correctanswer_questions3_game_obj2)
                    print('\n')
                    respuesta = input('Desea poner su respuesta\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    while respuesta != '1' and respuesta != '2':
                        respuesta = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while respuesta == '1':
                        answer = input('Ingrese la letra correspondiente a la respuesta que desea\n> ')
                        while answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd':
                            answer = input('Por favor ingrese una letra valida\n> ')
                        print('\n')
                        if answer == 'd':
                            print('Respuesta correcta')
                            return True
                        else:
                            vidas_clues['vidas'] -= 0.5
                            print('Respuesta Incorrecta')
                            print('\n')
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            while clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game3) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break
                                vidas_clues['clues'] -= 1                           
                                print(clues_game3[0])
                                print('\n')
                                clues_game3.pop(0)
                                volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                            if clue1 == '2':
                                volver = input('Desea poner otra respuesta o ver el enunciado de nuevo\n1.Volver al enunciado\n2.Poner otra respuesta\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
                    while respuesta == '2':
                        clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                        print('\n')
                        while clue1 != '1' and clue1 != '2':
                            clue1 = input('Por favor ingrese un numero valido\n> ')
                            print('\n')
                        while clue1 == '1':
                            if vidas_clues['clues'] <= 0:
                                print('Te quedaste sin pistas')
                                break
                            if len(clues_game3) == 0:
                                print('Te quedaste sin pistas')
                                print('\n')
                                break
                            vidas_clues['clues'] -= 1
                            print(clues_gam31[0])
                            print('\n')
                            clues_game3.pop(0)
                            volver = input('Desea ver el enunciado de nuevo o desea otra pista\n1.Volver al enunciado\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                        if clue1 == '2':
                            volver = input('Desea ver el enunciado \n1.Volver al enunciado\n2.Pedir pista\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while volver != '1' and volver != '2':
                                volver = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if volver == '1':
                                break
                pass
        else:
            break

import string
from pprint import pprint

def crear_sopa_de_letras(words_1):
    grid_size = 15
    grid = [ ['_' for _ in range(grid_size)]for _ in range(grid_size)]
    def print_grid():
        for x in range(grid_size):
            print('\t'*4+ ' '.join(grid[x]))
    orintaciones = [ 'izquierda_derecha', 'arriba_abajo', 'diagonal_arriba', 'diagonal_abajo']
    for word in words_1:
        word_length = len(word)
        placed = False
        while not placed:
            orientacion = random.choice(orintaciones)
            if orientacion == 'izquierda_derecha':
                puesto_x = 1
                puesto_y = 0
            elif orientacion == 'arriba_abajo':
                puesto_x = 0
                puesto_y = 1
            elif orientacion == 'diagonal_abajo':
                puesto_x = 1
                puesto_y = 1
            elif orientacion == 'diagonal_arriba':
                puesto_x = 1
                puesto_y = -1
            x_posicion = random.randint(0, grid_size-1)
            y_posicion = random.randint(0, grid_size-1)
            final_x = x_posicion + word_length*puesto_x
            final_y = y_posicion + word_length*puesto_y

            if final_x < 0 or final_y >= grid_size: continue
            if final_y < 0 or final_x >= grid_size: continue

            fail = False

            for i in range(word_length):
                caracter = word[i]
                nueva_pocision_x = x_posicion + i*puesto_x
                nueva_pocision_y = y_posicion + i*puesto_y
                caracter_en_nueva_posicion = grid[nueva_pocision_x][nueva_pocision_y]
                if caracter_en_nueva_posicion != '_':
                    if caracter_en_nueva_posicion == caracter:
                        continue
                    else:
                        fail = True
                        break
            if fail:
                continue
            else:
                for i in range(word_length):
                    caracter = word[i]
                    nueva_pocision_x = x_posicion + i*puesto_x
                    nueva_pocision_y = y_posicion + i*puesto_y
                    grid[nueva_pocision_x][nueva_pocision_y] = caracter
                placed = True
    for x in range(grid_size):
        for y in range(grid_size):
            if (grid[x][y] == '_'):
                grid[x][y] = random.choice(string.ascii_lowercase)
    print_grid()

def crear_sopa_de_letras(words_2):
    grid_size = 15
    grid = [ ['_' for _ in range(grid_size)]for _ in range(grid_size)]
    def print_grid():
        for x in range(grid_size):
            print('\t'*4+ ' '.join(grid[x]))
    orintaciones = [ 'izquierda_derecha', 'arriba_abajo', 'diagonal_arriba', 'diagonal_abajo']
    for word in words_2:
        word_length = len(word)
        placed = False
        while not placed:
            orientacion = random.choice(orintaciones)
            if orientacion == 'izquierda_derecha':
                puesto_x = 1
                puesto_y = 0
            elif orientacion == 'arriba_abajo':
                puesto_x = 0
                puesto_y = 1
            elif orientacion == 'diagonal_abajo':
                puesto_x = 1
                puesto_y = 1
            elif orientacion == 'diagonal_arriba':
                puesto_x = 1
                puesto_y = -1
            x_posicion = random.randint(0, grid_size-1)
            y_posicion = random.randint(0, grid_size-1)
            final_x = x_posicion + word_length*puesto_x
            final_y = y_posicion + word_length*puesto_y

            if final_x < 0 or final_y >= grid_size: continue
            if final_y < 0 or final_x >= grid_size: continue

            fail = False

            for i in range(word_length):
                caracter = word[i]
                nueva_pocision_x = x_posicion + i*puesto_x
                nueva_pocision_y = y_posicion + i*puesto_y
                caracter_en_nueva_posicion = grid[nueva_pocision_x][nueva_pocision_y]
                if caracter_en_nueva_posicion != '_':
                    if caracter_en_nueva_posicion == caracter:
                        continue
                    else:
                        fail = True
                        break
            if fail:
                continue
            else:
                for i in range(word_length):
                    caracter = word[i]
                    nueva_pocision_x = x_posicion + i*puesto_x
                    nueva_pocision_y = y_posicion + i*puesto_y
                    grid[nueva_pocision_x][nueva_pocision_y] = caracter
                placed = True
    for x in range(grid_size):
        for y in range(grid_size):
            if (grid[x][y] == '_'):
                grid[x][y] = random.choice(string.ascii_lowercase)
    print_grid()

def crear_sopa_de_letras(words_3):
    grid_size = 15
    grid = [ ['_' for _ in range(grid_size)]for _ in range(grid_size)]
    def print_grid():
        for x in range(grid_size):
            print('\t'*4+ ' '.join(grid[x]))
    orintaciones = [ 'izquierda_derecha', 'arriba_abajo', 'diagonal_arriba', 'diagonal_abajo']
    for word in words_3:
        word_length = len(word)
        placed = False
        while not placed:
            orientacion = random.choice(orintaciones)
            if orientacion == 'izquierda_derecha':
                puesto_x = 1
                puesto_y = 0
            elif orientacion == 'arriba_abajo':
                puesto_x = 0
                puesto_y = 1
            elif orientacion == 'diagonal_abajo':
                puesto_x = 1
                puesto_y = 1
            elif orientacion == 'diagonal_arriba':
                puesto_x = 1
                puesto_y = -1
            x_posicion = random.randint(0, grid_size-1)
            y_posicion = random.randint(0, grid_size-1)
            final_x = x_posicion + word_length*puesto_x
            final_y = y_posicion + word_length*puesto_y

            if final_x < 0 or final_y >= grid_size: continue
            if final_y < 0 or final_x >= grid_size: continue

            fail = False

            for i in range(word_length):
                caracter = word[i]
                nueva_pocision_x = x_posicion + i*puesto_x
                nueva_pocision_y = y_posicion + i*puesto_y
                caracter_en_nueva_posicion = grid[nueva_pocision_x][nueva_pocision_y]
                if caracter_en_nueva_posicion != '_':
                    if caracter_en_nueva_posicion == caracter:
                        continue
                    else:
                        fail = True
                        break
            if fail:
                continue
            else:
                for i in range(word_length):
                    caracter = word[i]
                    nueva_pocision_x = x_posicion + i*puesto_x
                    nueva_pocision_y = y_posicion + i*puesto_y
                    grid[nueva_pocision_x][nueva_pocision_y] = caracter
                placed = True
    for x in range(grid_size):
        for y in range(grid_size):
            if (grid[x][y] == '_'):
                grid[x][y] = random.choice(string.ascii_lowercase)
    print_grid()

def sopa_de_letras(vidas_clues):
    respuesta_bien = 0 
    clues_game1 = [api_1.clue1_questions1_game_obj1, api_1.clue2_questions1_game_obj1, api_1.clue3_questions1_game_obj1]
    words_1 = [(api_1.answer1_questions1_game_obj1).lower(), (api_1.answer2_questions1_game_obj1).lower(), (api_1.answer3_questions1_game_obj1).lower()]
    clues_game2 = [api_1.clue1_questions2_game_obj1, api_1.clue2_questions2_game_obj1, api_1.clue3_questions2_game_obj1]
    words_2 = [(api_1.answer1_questions2_game_obj1).lower(), (api_1.answer2_questions2_game_obj1).lower(), (api_1.answer3_questions2_game_obj1).lower()]
    clues_game3 = [api_1.clue1_questions3_game_obj1, api_1.clue2_questions3_game_obj1, api_1.clue3_questions3_game_obj1]
    words_3 = [(api_1.answer1_questions3_game_obj1).lower(), (api_1.answer2_questions3_game_obj1).lower(), (api_1.answer3_questions3_game_obj1).lower()]
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_1.name_game_obj1)
        print('Reglas del juego', api_1.rules_game_obj1)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print('''
- - - Sopa de letras - - - 
Bienvenido a sopa de letras, en este juego se generara una sopa de letras
de la cual deberas encontrar 3 palabras, las cuales estan relacionadas con 
la universidad. Suerte                
''')            
                while True:
                    respuesta = input('Desea poner comenzar\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    sopa_de_letras = crear_sopa_de_letras(words_1)
                    print('\n')
                    while respuesta != '1' and respuesta != '2':
                        respuesta = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while respuesta == '1':
                        if respuesta_bien == 3:
                            print('Ganaste')
                            return True
                        answer = input('Ingrese su respuesta (una sola palabra)\n> ').lower()
                        print('\n')
                        while answer in words_1:
                            print('Respuesta correcta')
                            respuesta_bien += 1
                            break
                        while answer not in words_1:
                            vidas_clues['vidas'] -= 0.5
                            print('Respuesta Incorrecta')
                            print('\n')
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if clue1 == '2':
                                break
                            elif clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game1) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break 
                                vidas_clues['clues'] -= 1                         
                                print(clues_game1[0])
                                print('\n')
                                clues_game1.pop(0)
                                volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
            while numero == '2':
                print('''
- - - Sopa de letras - - - 
Bienvenido a sopa de letras, en este juego se generara una sopa de letras
de la cual deberas encontrar 3 palabras, las cuales estan relacionadas con 
la universidad. Suerte                
''')            
                while True:
                    respuesta = input('Desea poner comenzar\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    crear_sopa_de_letras(words_2)
                    print('\n')
                    while respuesta != '1' and respuesta != '2':
                        respuesta = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while respuesta == '1':
                        if respuesta_bien == 3:
                            print('Ganaste')
                            return True
                        answer = input('Ingrese su respuesta (una sola palabra)\n> ').lower()
                        print('\n')
                        while answer in words_2:
                            print('Respuesta correcta')
                            respuesta_bien += 1
                            break
                        while answer not in words_2:
                            vidas_clues['vidas'] -= 0.5
                            print('Respuesta Incorrecta')
                            print('\n')
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if clue1 == '2':
                                break
                            elif clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game2) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break 
                                vidas_clues['clues'] -= 1                         
                                print(clues_game2[0])
                                print('\n')
                                clues_game2.pop(0)
                                volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
            while numero == '3':
                print('''
- - - Sopa de letras - - - 
Bienvenido a sopa de letras, en este juego se generara una sopa de letras
de la cual deberas encontrar 3 palabras, las cuales estan relacionadas con 
la universidad. Suerte                
''')            
                while True:
                    respuesta = input('Desea poner comenzar\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                    print('\n')
                    crear_sopa_de_letras(words_3)
                    print('\n')
                    while respuesta != '1' and respuesta != '2':
                        respuesta = input('Por favor ingrese un numero valido\n> ')
                        print('\n')
                    while respuesta == '1':
                        if respuesta_bien == 3:
                            print('Ganaste')
                            return True
                        answer = input('Ingrese su respuesta (una sola palabra)\n> ').lower()
                        print('\n')
                        while answer in words_3:
                            print('Respuesta correcta')
                            respuesta_bien += 1
                            break
                        while answer not in words_3:
                            vidas_clues['vidas'] -= 0.5
                            print('Respuesta Incorrecta')
                            print('\n')
                            clue1 = input('Desea una pista?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            print('\n')
                            while clue1 != '1' and clue1 != '2':
                                clue1 = input('Por favor ingrese un numero valido\n> ')
                                print('\n')
                            if clue1 == '2':
                                break
                            elif clue1 == '1':
                                if vidas_clues['clues'] <= 0:
                                    print('Te quedaste sin pistas')
                                    break
                                if len(clues_game3) == 0:
                                    print('Te quedaste sin pistas')
                                    print('\n')
                                    break 
                                vidas_clues['clues'] -= 1                         
                                print(clues_game3[0])
                                print('\n')
                                clues_game3.pop(0)
                                volver = input('Desea poner otra respuesta o desea otra pista\n1.Poner otra respuesta\n2.Pedir otra pista\nIngrese el numero de la opcion que desea\n> ')
                                print('\n')
                                while volver != '1' and volver != '2':
                                    volver = input('Por favor ingrese un numero valido\n> ')
                                    print('\n')
                                if volver == '1':
                                    break
        else:
            break

def logicab(vidas_clues):
    while True:
        print('Para ganar necesitaras jugar a este juego y tener la respuesta correcta')
        print('Nombre del juego', api_4.name_game_obj1)
        print('Reglas del juego', api_4.rules_game_obj1)
        print('\n')
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        print('''
- - - Logica booleana - - - 
Bienvenido a logica booleana, en el juego tendras que corrrer en frio
el codigo para la siguiente pregunta.
''')
        if listo == '1':
            numero = random.choice(('1','2'))
            while numero == '1':
                print(api_4.question_questions1_game_obj1)
                print('\n')
                answer = input('Ingrese el resultado del output\n> ')
                print('\n')
                if answer == 'False':
                    print('Respuesta correcta\nGanaste')
                    print('\n')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('\n')
                    print('Respuesta incorrecta\nIntenta de nuevo\n')
                    print('\n')
            while numero == '2':
                print(api_4.question_questions2_game_obj1)
                print('\n')
                answer = input('Ingrese el resultado del output\n> ')
                print('\n')
                if answer == 'True':
                    print('Respuesta correcta\nGanaste')
                    print('\n')
                    return True
                else:
                    vidas_clues['vidas'] -= 0.5
                    print('Respuesta incorrecta\nIntenta de nuevo\n')
                    print('\n')
        else:
            break

def preguntas_de_todo(vidas_clues):
    print('''
- - - Final Boss (Trivia) - - - 
Para recuperar el disco duro, tendras que vencer a la persona que lo robo, 
por medio de responder algunas preguntas de cultura general, se te preguntaran
unas ciertas preguntas y si las respondes bien le quitaras vida a la persona
que robo el disco dura, (Cuidado si te equivocas, el malo no perdona, y perderas)
y al dejarlo sin vida podras quedarte con el premio que es ganar el juego, 
por medio de colocar el disco duro en su lugar, suerte.
''')
    while True:
        listo = input('Estas listo para jugar?\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
        print('\n')
        while listo != '1' and listo != '2':
            listo = input('Por favor ingrese un numero valido\n> ')
            print('\n')
        if listo == '1':
            numero = random.choice(('1','2','3'))
            while numero == '1':
                print('Malo: No me vas a poder vencer')
                print('\n')
                print('Primera pregunta.')
                print('\n')
                pregunta = '¿En qué año el hombre pisó la Luna por primera vez?'
                print(pregunta)
                respuesta = input('''
a. 1950
b. 1969
c. 1967
d. 1971
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()
                while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                    respuesta = input('Por favor ingrese una respuesta valida\n> ')
                if respuesta == 'b':
                    print('\n')
                    print('Respuesta correcta')
                    print('\n')
                    print('Malo: MMM, con que asi es la cosa, a ver si sabes esto')
                    print('\n')
                    pregunta = '¿En que año llego Cristobal colon a Venezuela?'
                    print(pregunta)
                    respuesta = input('''
a. 1513
b. 1456
c. 1517
d. 1498   
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()
                    while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                        respuesta = input('Por favor ingrese una respuesta valida\n> ')    
                    if respuesta == 'd':
                        print('\n')
                        print('Respuesta correcta')
                        print('\n')
                        print('MMM, no esperaba que llegaras tan lejos')
                        print('\n')
                        pregunta = '¿En que año se creo el primer lenguaje de programación?'
                        print(pregunta)
                        respuesta = input('''
a. 1955
b. 1958
c. 1953
d. 1959
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()           
                        while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                            respuesta = input('Por favor ingrese una respuesta valida\n> ') 
                        if respuesta == 'a':
                            print('\n')
                            print('Respuesta Correcta')
                            print('\n')
                            print('No me gusta esto, estas llegando muy lejos, ya me queda menos de mitad de vida')
                            print('\n')
                            pregunta = '¿En que año comenzo a utilizarse python?'
                            print(pregunta)
                            respuesta = input('''
a. 1978
b. 1990
c. 1989
d. 1998
Ingrese la letra correspondiente a la respuesta que desea                          
> ''').lower()
                            while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                                respuesta = input('Por favor ingrese una respuesta valida\n> ')
                            if respuesta == 'c':
                                print('\n')
                                print('Respuesta correcta')
                                print('\n')
                                print('Bueno me impresionaste, no espere tanto de alguien como tu, para ganar respondeme esta ultima pregunta')
                                print('\n')
                                pregunta = '¿En que año se creo la primera computadora que funcionace?'
                                print(pregunta)
                                respuesta = input('''
a. 1941
b. 1950
c. 1943
d. 1946
Ingrese la letra correspondiente a la respuesta que desea                                 
> ''')
                                while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                                    respuesta = input('Por favor ingrese una respuesta valida\n> ')
                                if respuesta == 'a':
                                    print('\n')
                                    print('Malo: NOOOOO, ME LOGRASTE VENCE')
                                    print('\n')
                                    print('FELICIDADES, GANASTE')
                                    return True
                                else:
                                    vidas_clues['vidas'] -= 10
                                    print('\n')
                                    print('El malo te robo el disco duro, PERDISTE')
                                    print('\n')
                                    return False
                            else:
                                vidas_clues['vidas'] -= 10
                                print('\n')
                                print('El malo te robo el disco duro, PERDISTE')
                                print('\n')
                                return False
                        else:
                            vidas_clues['vidas'] -= 10
                            print('\n')
                            print('El malo te robo el disco duro, PERDISTE')
                            print('\n')
                            return False
                    else:
                        vidas_clues['vidas'] -= 10
                        print('\n')
                        print('El malo te robo el disco duro, PERDISTE')
                        print('\n')
                        return False
                else:
                    vidas_clues['vidas'] -= 10
                    print('\n')
                    print('El malo te robo el disco duro, PERDISTE')
                    print('\n')
                    return False
            while numero == '2':
                print('Malo: No me vas a poder vencer')
                print('\n')
                print('Primera pregunta.')
                print('\n')
                pregunta = '¿Quien piso la luna por primera vez?'
                print(pregunta)
                respuesta = input('''
a. Elon Musk
b. Edwin F.
c. Neil Armstrong
d. Aldrin
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()
                while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                    respuesta = input('Por favor ingrese una respuesta valida\n> ')
                if respuesta == 'c':
                    print('\n')
                    print('Respuesta correcta')
                    print('\n')
                    print('Malo: MMM, con que asi es la cosa, a ver si sabes esto')
                    print('\n')
                    pregunta = '¿Cual carabela fue la primera en ver la tierra de america?'
                    print(pregunta)
                    respuesta = input('''
a. La Pinta
b. La Santa Maria
c. La Virgen del Valle
d. La Niña   
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()
                    while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                        respuesta = input('Por favor ingrese una respuesta valida\n> ')    
                    if respuesta == 'a':
                        print('\n')
                        print('Respuesta correcta')
                        print('\n')
                        print('MMM, no esperaba que llegaras tan lejos')
                        print('\n')
                        pregunta = '¿En que año se creo el primer lenguaje de programación?'
                        print(pregunta)
                        respuesta = input('''
a. C
b. FORTRAN
c. LISP
d. COBOL
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()           
                        while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                            respuesta = input('Por favor ingrese una respuesta valida\n> ') 
                        if respuesta == 'b':
                            print('\n')
                            print('Respuesta Correcta')
                            print('\n')
                            print('No me gusta esto, estas llegando muy lejos, ya me queda menos de mitad de vida')
                            print('\n')
                            pregunta = '¿Quien diseño el lenguaje de programacion python?'
                            print(pregunta)
                            respuesta = input('''
a. Guido Van Rossum
b. James Gosling
c. Dennis Ritchie
d. Trump
Ingrese la letra correspondiente a la respuesta que desea                          
> ''').lower()
                            while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                                respuesta = input('Por favor ingrese una respuesta valida\n> ')
                            if respuesta == 'a':
                                print('\n')
                                print('Respuesta correcta')
                                print('\n')
                                print('Bueno me impresionaste, no espere tanto de alguien como tu, para ganar respondeme esta ultima pregunta')
                                print('\n')
                                pregunta = '¿Quien creo la primera computadora?'
                                print(pregunta)
                                respuesta = input('''
a. Charles Babbage
b. Guillermo Marconi
c. Blaise Pascal
d. Konrad Zuse
Ingrese la letra correspondiente a la respuesta que desea                                 
> ''')
                                while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                                    respuesta = input('Por favor ingrese una respuesta valida\n> ')
                                if respuesta == 'a':
                                    print('\n')
                                    print('Malo: NOOOOO, ME LOGRASTE VENCE')
                                    print('\n')
                                    print('FELICIDADES, GANASTE')
                                    return True
                                else:
                                    vidas_clues['vidas'] -= 10
                                    print('\n')
                                    print('El malo te robo el disco duro, PERDISTE')
                                    print('\n')
                                    return False
                            else:
                                vidas_clues['vidas'] -= 10
                                print('\n')
                                print('El malo te robo el disco duro, PERDISTE')
                                print('\n')
                                return False
                        else:
                            vidas_clues['vidas'] -= 10
                            print('\n')
                            print('El malo te robo el disco duro, PERDISTE')
                            print('\n')
                            return False
                    else:
                        vidas_clues['vidas'] -= 10
                        print('\n')
                        print('El malo te robo el disco duro, PERDISTE')
                        print('\n')
                        return False
                else:
                    vidas_clues['vidas'] -= 10
                    print('\n')
                    print('El malo te robo el disco duro, PERDISTE')
                    print('\n')
                    return False
            while numero == '3':
                print('Malo: No me vas a poder vencer')
                print('\n')
                print('Primera pregunta.')
                print('\n')
                pregunta = '¿Cual fue el primer pais en llegar a la luna?'
                print(pregunta)
                respuesta = input('''
a. Venezuela
b. Alemania
c. Estados Unidos
d. Rusia
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()
                while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                    respuesta = input('Por favor ingrese una respuesta valida\n> ')
                if respuesta == 'c':
                    print('\n')
                    print('Respuesta correcta')
                    print('\n')
                    print('Malo: MMM, con que asi es la cosa, a ver si sabes esto')
                    print('\n')
                    pregunta = '¿Donde nacio la persona que descubrio america?'
                    print(pregunta)
                    respuesta = input('''
a. España
b. Portugal
c. Mexico
d. Inglaterra   
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()
                    while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                        respuesta = input('Por favor ingrese una respuesta valida\n> ')    
                    if respuesta == 'b':
                        print('\n')
                        print('Respuesta correcta')
                        print('\n')
                        print('MMM, no esperaba que llegaras tan lejos')
                        print('\n')
                        pregunta = '¿Que compañia creo el primer lenguaje de programación?'
                        print(pregunta)
                        respuesta = input('''
a. IBM
b. CANTV
c. APPLE
d. MICROSOFT
Ingrese la letra correspondiente a la respuesta que desea
> ''').lower()           
                        while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                            respuesta = input('Por favor ingrese una respuesta valida\n> ') 
                        if respuesta == 'a':
                            print('\n')
                            print('Respuesta Correcta')
                            print('\n')
                            print('No me gusta esto, estas llegando muy lejos, ya me queda menos de mitad de vida')
                            print('\n')
                            pregunta = '¿Cual lenguaje se utiliza para la creacion de paginas web?'
                            print(pregunta)
                            respuesta = input('''
a. Python
b. C++
c. HTML
d. SWIFT
Ingrese la letra correspondiente a la respuesta que desea                          
> ''').lower()
                            while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                                respuesta = input('Por favor ingrese una respuesta valida\n> ')
                            if respuesta == 'c':
                                print('\n')
                                print('Respuesta correcta')
                                print('\n')
                                print('Bueno me impresionaste, no espere tanto de alguien como tu, para ganar respondeme esta ultima pregunta')
                                print('\n')
                                pregunta = '¿Donde se creo la primera computadora que funcionara?'
                                print(pregunta)
                                respuesta = input('''
a. Estados Unidos
b. Paraguay
c. Francia
d. Alemania
Ingrese la letra correspondiente a la respuesta que desea                                 
> ''')
                                while respuesta != 'a' and respuesta != 'b' and respuesta != 'c' and respuesta != 'd':
                                    respuesta = input('Por favor ingrese una respuesta valida\n> ')
                                if respuesta == 'd':
                                    print('\n')
                                    print('Malo: NOOOOO, ME LOGRASTE VENCE')
                                    print('\n')
                                    print('FELICIDADES, GANASTE')
                                    return True
                                else:
                                    vidas_clues['vidas'] -= 10
                                    print('\n')
                                    print('El malo te robo el disco duro, PERDISTE')
                                    print('\n')
                                    return False
                            else:
                                vidas_clues['vidas'] -= 10
                                print('\n')
                                print('El malo te robo el disco duro, PERDISTE')
                                print('\n')
                                return False
                        else:
                            vidas_clues['vidas'] -= 10
                            print('\n')
                            print('El malo te robo el disco duro, PERDISTE')
                            print('\n')
                            return False
                    else:
                        vidas_clues['vidas'] -= 10
                        print('\n')
                        print('El malo te robo el disco duro, PERDISTE')
                        print('\n')
                        return False
                else:
                    vidas_clues['vidas'] -= 10
                    print('\n')
                    print('El malo te robo el disco duro, PERDISTE')
                    print('\n')
                    return False
