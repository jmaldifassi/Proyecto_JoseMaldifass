import images_cuarto1
import juegos
from chequaer_tiempo_vidas import chequear_vidas, chequear_tiempo

# import api_cuarto1

def cuarto_1(inventario, objetos, vidas_clues, start, t):
    while True:
        print(images_cuarto1.laboratorio_dentro)
        direccion = input('''
Ingrese el numero de la opcion que deseas realizar
1. <-- Ir al objeto de la izquierda
2. ^ Ir al objeto del medio
3. --> Ir al objeto de la derecha
4. v Volver
>  ''')
        perdiste_t = (chequear_tiempo(start, t))
        perdiste_v = (chequear_vidas(vidas_clues))
        if perdiste_v == False:
            return False
        elif perdiste_t == False:
            return False
        else:
            while direccion != '1' and direccion != '2' and direccion != '3' and direccion != '4' and direccion != '123':
                direccion = input('Por favor ingrese el numero de una opcion valida\n> ')
            if direccion == '2':
                while objetos['obj1_1'] == False:
                    print(images_cuarto1.pizarra_con_vida)
                    play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                    while play != '1' and play != '2':
                        play = input('Por favor ingrese un numero valido\n> ')
                    if play == '1':
                        perdiste_v = (chequear_vidas(vidas_clues))
                        perdiste_t = (chequear_tiempo(start, t))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            ganaste = False
                            ganaste = juegos.sopa_de_letras(vidas_clues)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                if ganaste == True:
                                    print('Ganaste un vida')
                                    vidas_clues['vidas'] += 1
                                    objetos['obj1_1'] = True
                                    break
                                else: 
                                    break
                    else:
                        break
                while objetos['obj1_1'] == True:
                    print(images_cuarto1.pizarra_sin_vida)
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            elif direccion == '1':
                while objetos['obj2_1'] == False:
                    if 'cable_hdmi' not in inventario:
                        print(images_cuarto1.computador1_con_carnet_pantalla)
                        print(images_cuarto1.computador1_sin_hdmi)
                        print('No tengo el cable hdmi')
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                            while afuera != '1' and afuera != '2':
                                afuera = input('Por favor ingrese un numero valido\n> ')
                            if afuera == '1':
                                break
                    elif 'cable_hdmi' in inventario:
                        print(images_cuarto1.computador1_con_hdmi)
                        print(images_cuarto1.computadora1)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            play = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                ganaste = False
                                ganaste = juegos.preguntas_python(vidas_clues)
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    if ganaste == True:
                                        print('\n')
                                        print(images_cuarto1.computadora1_con_carnet)
                                        carnet = 'carnet'
                                        inventario.append(carnet)
                                        objetos['obj2_1'] = True
                                        break
                                    else: 
                                        break
                        else:
                            break
                while objetos['obj2_1'] == True:
                    print(images_cuarto1.computador1_sin_carnet)
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            elif direccion == '3':
                while objetos['obj3_1'] == False:
                    print(images_cuarto1.computadora2_con_llave_sin_clave)
                    if 'contrasena' not in inventario:
                        print('No tengo la clave :(')
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                            while afuera != '1' and afuera != '2':
                                afuera = input('Por favor ingrese un numero valido\n> ')
                            if afuera == '1':
                                break
                    elif 'contrasena' in inventario:
                        print(images_cuarto1.computadora2_con_llave_con_clave)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                ganaste = False
                                ganaste = juegos.adivinanzas(vidas_clues)
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    if ganaste == True:
                                        print(images_cuarto1.computadora2_jugado_con_llave)
                                        print('Bien me gane una llave')
                                        llave = 'llave'
                                        inventario.append(llave)
                                        objetos['obj3_1'] = True
                                        break
                                    else:
                                        break
                        else:
                            break
                while objetos['obj3_1'] == True:
                    print(images_cuarto1.computadora2_jugado_sin_llave)
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            else:
                break
            
import images_cuarto2

def cuarto_2(inventario, objetos, vidas_clues, start, t):
    while True:
        print(images_cuarto2.biblioteca_dentro)
        direccion = input('''
Ingrese el numero de la opcion que deseas realizar
1. <-- Ir al objeto de la izquierda
2. ^ Ir al objeto del medio
3. --> Ir al objeto de la derecha
4. v Volver
>  ''')
        perdiste_t = (chequear_tiempo(start, t))
        perdiste_v = (chequear_vidas(vidas_clues))
        if perdiste_v == False:
            return False
        elif perdiste_t == False:
            return False
        else:
            while direccion != '1' and direccion != '2' and direccion != '3' and direccion != '4' and direccion != '123':
                direccion = input('Por favor ingrese el numero de una opcion valida\n> ')
            if direccion == '1':
                while objetos['obj2_2'] == False:
                    if 'libro_mate' not in inventario:
                        print(images_cuarto2.silla)
                        print('No tengo el libro de matematicas')
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                            while afuera != '1' and afuera != '2':
                                afuera = input('Por favor ingrese un numero valido\n> ')
                            if afuera == '1':
                                break
                    elif 'libro_mate' in inventario:
                        print(images_cuarto2.silla_juego)
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                            while play != '1' and play != '2':
                                play = input('Por favor ingrese un numero valido\n> ')
                            if play == '1':
                                ganaste = False
                                ganaste = juegos.preguntas_mate(vidas_clues)
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    if ganaste == True:
                                        print(images_cuarto2.silla_conHDMI)
                                        print('Bien gane una vida extra')
                                        vidas_clues['vidas'] += 1
                                        objetos['obj2_2'] = True
                                        break
                                    else:
                                        break
                            else:
                                break
                while objetos['obj2_2'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto2.silla_sinHDMI)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            elif direccion == '2':
                while objetos['obj1_2'] == False:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto2.estanterias)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            play = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            ganaste = False
                            ganaste = juegos.ahorcado(vidas_clues)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                if ganaste == True:
                                    print(images_cuarto2.estanteria_conHDMI)
                                    print('Bien gane un cable hdmi')
                                    cable_hdmi = 'cable_hdmi'
                                    inventario.append(cable_hdmi)
                                    objetos['obj1_2'] = True
                                    break
                                else:
                                    break
                        else:
                            break
                while objetos['obj1_2'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto2.estanteria_sinHDMI)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            elif direccion == '3':
                while objetos['obj3_2'] == False:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto2.mueble)
                        gabeta = input('Puedo abrir estas gabetas cual abrire, o puedo volver (0)\n Ingrese el numero de la gabeta que desea abrir\n>')
                        while gabeta != '0' and gabeta != '1' and gabeta != '2' and gabeta != '3' and gabeta != '4':
                            gabeta = input('Por favor ingrese un numero valido (1-4)\n> ')
                        if gabeta == '1':
                            if 'llave' not in inventario:
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    print(images_cuarto2.mueble_cerrado)
                                    afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                                    while afuera != '1' and afuera != '2':
                                        afuera = input('Por favor ingrese un numero valido\n> ')
                                    if afuera == '1':
                                        break
                            elif 'llave' in inventario:
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    print(images_cuarto2.mueble_abierto_)
                                    play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                                    while play != '1' and play != '2':
                                        play = input('Por favor ingrese un numero valido\n> ')
                                    if play == '1':
                                        ganaste = False
                                        ganaste = juegos.criptograma(vidas_clues)
                                        perdiste_t = (chequear_tiempo(start, t))
                                        perdiste_v = (chequear_vidas(vidas_clues))
                                        if perdiste_v == False:
                                            return False
                                        elif perdiste_t == False:
                                            return False
                                        else:
                                            if ganaste == True:
                                                print(images_cuarto2.mueble_abierto)
                                                print('Bien gane un Mensaje que dice: Si estas graduado pisas el saman')
                                                mensaje_graduarte = 'mensaje_graduarte'
                                                inventario.append(mensaje_graduarte)
                                                objetos['obj3_2'] = True
                                                break
                                            else:
                                                break
                                    else:
                                        break
                        elif gabeta == '2':
                            print(images_cuarto2.mueble_gaveta2_abiera)
                        elif gabeta == '3':
                            print(images_cuarto2.mueble_gaveta3_abiera)
                        elif gabeta == '4':
                            print(images_cuarto2.mueble_gaveta4_abiera)
                        else:
                            break
                while objetos['obj3_2'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto2.mueble_abiertos)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            else:
                break

import images_cuarto3

def cuarto_3(inventario, objetos, vidas_clues, start, t):
    while True:
        print(images_cuarto3.plaza_rectorado_dentro)
        direccion = input('''
Ingrese el numero de la opcion que deseas realizar
1. <-- Ir al objeto de la izquierda
2. ^ Ir al objeto del medio
3. --> Ir al objeto de la derecha
4. v Volver
>  ''')
        perdiste_t = (chequear_tiempo(start, t))
        perdiste_v = (chequear_vidas(vidas_clues))
        if perdiste_v == False:
            return False
        elif perdiste_t == False:
            return False
        else:
            while direccion != '1' and direccion != '2' and direccion != '3' and direccion != '4' and direccion != '123':
                direccion = input('Por favor ingrese el numero de una opcion valida\n> ')
            if direccion == '1':
                while objetos['obj2_3'] == False:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto3.banco1)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            play = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            ganaste = True 
                            ganaste = juegos.quiz_cultura_unimetana(vidas_clues)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                if ganaste == True:
                                    print(images_cuarto3.banco1_con_libro)
                                    print('Bien gane un libro de matematicas')
                                    libro_mate = 'libro_mate'
                                    inventario.append(libro_mate)
                                    objetos['obj2_3'] = True
                                    break
                                else:
                                    break
                        else:
                            break
                while objetos['obj2_3'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto3.banco1_sin_libro)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            elif direccion == '2':
                perdiste_t = (chequear_tiempo(start, t))
                perdiste_v = (chequear_vidas(vidas_clues))
                if perdiste_v == False:
                    return False
                elif perdiste_t == False:
                    return False
                else:
                    pisar = input('Deseas pisar el saman, si lo pisas perderas una vida\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                    while pisar != '1' and pisar != '2':
                        pisar = input('Por favor ingrese un numero valido')
                    if pisar == '1':
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            vidas_clues['vidas'] -= 1
                            while objetos['obj1_3'] == False:
                                if ('titulo_universitario' and 'mensaje_graduarte' not in inventario) and ('titulo_universitario' or 'mensaje_graduarte' not in inventario):
                                    perdiste_t = (chequear_tiempo(start, t))
                                    perdiste_v = (chequear_vidas(vidas_clues))
                                    if perdiste_v == False:
                                        return False
                                    elif perdiste_t == False:
                                        return False
                                    else:
                                        print(images_cuarto3.saman)
                                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                                        while afuera != '1' and afuera != '2':
                                            afuera = input('Por favor ingrese un numero valido\n> ')
                                        if afuera == '1':
                                            break
                                elif 'titulo_universitario' and 'mensaje_graduarte' in inventario:
                                    perdiste_t = (chequear_tiempo(start, t))
                                    perdiste_v = (chequear_vidas(vidas_clues))
                                    if perdiste_v == False:
                                        return False
                                    elif perdiste_t == False:
                                        return False
                                    else:
                                        print(images_cuarto3.saman)
                                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                                        while play != '1' and play != '2':
                                            play = input('Por favor ingrese un numero valido\n> ')
                                        if play == '1':
                                            ganaste = False
                                            ganaste = juegos.logica(vidas_clues)
                                            perdiste_t = (chequear_tiempo(start, t))
                                            perdiste_v = (chequear_vidas(vidas_clues))
                                            if perdiste_v == False:
                                                return False
                                            elif perdiste_t == False:
                                                return False
                                            else:
                                                if ganaste == True:
                                                    print(images_cuarto3.saman_con_disco_duro)
                                                    disco_duro = 'disco_duro'
                                                    inventario.append(disco_duro)
                                                    objetos['obj1_3'] = True
                                                    break
                                                else:
                                                    break
                                        else:
                                            break
                        while objetos['obj1_3'] == True:
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                print(images_cuarto3.saman_sin_disco_duro)
                                afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                                while afuera != '1' and afuera != '2':
                                    afuera = input('Por favor ingrese un numero valido\n> ')
                                if afuera == '1':
                                    break
            elif direccion == '3':
                while objetos['obj3_3'] == False:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto3.banco2)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            play = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            ganaste = False
                            ganaste = juegos.memoria(vidas_clues)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                if ganaste == True:
                                    print(images_cuarto3.banco2_con_martillo)
                                    martillo = 'martillo'
                                    inventario.append(martillo)
                                    objetos['obj3_3'] = True
                                    break
                                else:
                                    break
                        else:
                            break
                while objetos['obj3_3'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto3.banco2_sin_martillo)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            else:
                break


import images_cuarto4

def cuarto_4(inventario, objetos, vidas_clues, start, t):
    obj1 = False
    while True:
        print(images_cuarto4.puerta_con_candado_dentro)
        direccion = input('''
Ingrese el numero de la opcion que deseas realizar
1. ^ Ir al objeto del medio
2. v Volver
>  ''')
        perdiste_t = (chequear_tiempo(start, t))
        perdiste_v = (chequear_vidas(vidas_clues))
        if perdiste_v == False:
            return False
        elif perdiste_t == False:
            return False
        else:
            while direccion != '1' and direccion != '2' and direccion != '3' and direccion != '4' and direccion != '123':
                direccion = input('Por favor ingrese el numero de una opcion valida\n> ')
            if direccion == '1':
                while objetos['obj1_4'] == False:
                    if 'martillo' not in inventario:
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            print(images_cuarto4.puerta_con_candado)
                            afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                            while afuera != '1' and afuera != '2':
                                afuera = input('Por favor ingrese un numero valido\n> ')
                            if afuera == '1':
                                break
                    elif 'martillo' in inventario:
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            print(images_cuarto4.puerta_con_candado)
                            play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                            while play != '1' and play != '2':
                                play = input('Por favor ingrese un numero valido\n> ')
                            if play == '1':
                                ganaste = False
                                ganaste = juegos.logicab(vidas_clues)
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    if ganaste == True:
                                        print(images_cuarto4.puerta_sin_candado_con_libro)
                                        libro_fisica = 'libro_fisica'
                                        inventario.append(libro_fisica)
                                        objetos['obj1_4'] = True
                                        break
                                    else:
                                        break
                            else:
                                break
                while objetos['obj1_4'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto4.puerta_sin_candado_sin_libro)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            else:
                break

import images_cuarto5
import time

def cuarto_5(inventario, objetos, vidas_clues, start, t, tiempo_final):
    while True:
        print(images_cuarto5.cuarto_de_servidores_dentro)
        direccion = input('''
Ingrese el numero de la opcion que deseas realizar
1. <-- Ir al objeto de la izquierda
2. ^ Ir al objeto del medio
3. --> Ir al objeto de la derecha
4. v Volver
>  ''')
        perdiste_t = (chequear_tiempo(start, t))
        perdiste_v = (chequear_vidas(vidas_clues))
        if perdiste_v == False:
            return False
        elif perdiste_t == False:
            return False
        else:
            while direccion != '1' and direccion != '2' and direccion != '3' and direccion != '4' and direccion != '123':
                direccion = input('Por favor ingrese el numero de una opcion valida\n> ')
            if direccion == '1':
                while objetos['obj2_5'] == False:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto5.rack)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            play = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            ganaste = False
                            ganaste = juegos.palabra_mezclada(vidas_clues)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                if ganaste == True:
                                    print(images_cuarto5.rack_con_papel)
                                    contrasena = 'contrasena'
                                    inventario.append(contrasena)
                                    objetos['obj2_5'] = True
                                    break
                                else:
                                    break
                        else:
                            break
                while objetos['obj2_5'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto5.rack_sin_papel)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break           
            elif direccion == '2':
                while objetos['obj1_5'] == False:
                    if ('carnet' and 'disco_duro' not in inventario) and ('carnet' or 'disco_duro' not in inventario):
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            print(images_cuarto5.puerta_cerrada)
                            afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                            while afuera != '1' and afuera != '2':
                                afuera = input('Por favor ingrese un numero valido\n> ')
                            if afuera == '1':
                                break
                    elif 'carnet' and 'disco_duro' in inventario:
                        perdiste_t = (chequear_tiempo(start, t))
                        perdiste_v = (chequear_vidas(vidas_clues))
                        if perdiste_v == False:
                            return False
                        elif perdiste_t == False:
                            return False
                        else:
                            print(images_cuarto5.puerta_cerrada)
                            play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                            while play != '1' and play != '2':
                                play = input('Por favor ingrese un numero valido\n> ')
                            if play == '1':
                                ganaste = True
                                ganaste = juegos.preguntas_de_todo(vidas_clues)
                                perdiste_t = (chequear_tiempo(start, t))
                                perdiste_v = (chequear_vidas(vidas_clues))
                                if perdiste_v == False:
                                    return False
                                elif perdiste_t == False:
                                    return False
                                else:
                                    if ganaste == True:
                                        print(images_cuarto5.puerta_abierta)
                                        print('GANASTEE!!')
                                        end = time.monotonic()
                                        t_partida = end - start
                                        tiempo_final.append(t_partida)
                                        print('Tiempo final', t_partida)
                                        return True
                                    else:
                                        break
                            else:
                                break
            elif direccion == '3':
                while objetos['obj3_5'] == False:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto5.papelera)
                        play = input('Desea jugar el juego correspondeinte a este objeto con la posibilidad de ganar su premio\n1. Si\n2. No\nIngrese el numero de la opcion que desea\n> ')
                        while play != '1' and play != '2':
                            play = input('Por favor ingrese un numero valido\n> ')
                        if play == '1':
                            ganaste = False
                            ganaste = juegos.numero_entre(vidas_clues)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                if ganaste == True:
                                    print(images_cuarto5.papelera_con_titulo)
                                    titulo_universitario = 'titulo_universitario'
                                    inventario.append(titulo_universitario)
                                    objetos['obj3_5'] = True
                                    break
                                else:
                                    break
                        else:
                            break
                while objetos['obj3_5'] == True:
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print(images_cuarto5.papelera_sin_titulo)
                        afuera = input('No puedo hacer nada aqui, me devuelvo\n1.Si\n2. No\nIngresa el numero de la opcion que desea\n> ')
                        while afuera != '1' and afuera != '2':
                            afuera = input('Por favor ingrese un numero valido\n> ')
                        if afuera == '1':
                            break
            else:
                break