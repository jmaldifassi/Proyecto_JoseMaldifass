import images_cuarto1
import images_cuarto2 
import images_cuarto3
import images_cuarto4
import images_cuarto5
import cuartos
import json

def bienvenida():
    print('''
 - - - - - - - - - - - - Escapemet - - - - - - - - - - - - 
|                                                         |
|    Bienvenido a Escapemet:                              |
|    - Ingresa con tu cuenta para poder jugar.            |
|                                                         |
|    - Este es un Video juego de un escape room           |
|      en el que podras jugar individualmente             |
|      para lograr los objetivos, esto se                 |
|      explica mejor al iniciar el juego.                 |
|                                                         |
|    - Esperemos que te guste y lo disfrutes, las         |
|      reglas se explican mejor despues                   |
|                                                         |
|                                                         |
-----------------------------------------------------------
    ''')

def reglas():
    print('''
Antes de jugar deberias primero conocer la reglas, 
las cuales son las siguientes.

- Tienes un tiempo limitado para ganar el juego o perderas. 
(El tiempo dado cambia segun la dificultad)

- El tiempo empezara como un temporizador cuando comienzes
la partida.

- Tienes una cierta cantidad de vidas para ganar el juego,
las vidas se van perdiendo si pierdes en alguno de los mini
juegos, al acabaerse tus vidas (es decir 0 vidas) perderas.
No importa con cuantas vidas termines no cambia el resultado.
(La cantidad de vidas varia segun la dificultad)

- Tienes una cierta cantidad de pistas, las cuales si usas una
en cualquier juego se gastaran para la partida, estas pistas te 
ayudaran a ganar los videojuegos con mas facilidad, en cada mini
juego podras usar un maximo de trs pistas.
(La cantidad de pistas varian segun la dificultad)

- Podras ver el tiempo y las vidas que te quedan al salir de 
una habitacion.

- Los objetos de las habitaciones tienen cada uno un minijuego
del cual si lo logras ganar se te ofrecera una recompensa.

- Para jugar algunos de los minijuegos de los objetos se te 
solicitara algun requisito los cuales, obtendras ganando 
algun minijuego de otro objeto, sin este requisito no podras
jugar el minijuego del objeto.

- Las recompensas obtenidas por los minijuegos tienen un solo
uso para la partida. (Cuando las uses no podras volverlas a usar)

- El tiempo y las vidas, los podras ver unicamente si estas 
fuera de los cuartos. (En la pantalla de moverse de habitacion)

- Dentro de los minijuegos, hasta no ganarlo no podras salir
(Si decides jugar un jugo podrias perder todas las vidas)

- NO SE PERMITEN HACKS

Gracias por leer las reglas (Se que es mucho texto), estas te
ayudara a entender y jugar mejor a este scaperoom.
''')

def dificultad():
    vidas = 0
    clues = 0
    t = 0
    with open('informacion.json') as file:
        informacion = json.load(file)
    dificultad = informacion['dificultad']
    dif_facil = dificultad[0]
    vidas_facil = dif_facil['Vidas']
    clues_facil = dif_facil['Clues']
    t_facil = dif_facil['t']

    dif_media = dificultad[1]
    vidas_media = dif_media['Vidas']
    clues_media = dif_media['Clues']
    t_media = dif_media['t']

    dif_dificil = dificultad[2]
    vidas_dificil = dif_dificil['Vidas']
    clues_dificil = dif_dificil['Clues']
    t_dificil = dif_dificil['t']

    dif_extremo = dificultad[3]
    vidas_extremo = dif_extremo['Vidas']
    clues_extremo = dif_extremo['Clues']
    t_extremo = dif_extremo['t']

    print(f'''
Para jugar necesita selecionar una dificultad, segun la dificutad que escojas tendras un cierto tiempo para terminar el juego, una cantidad de vidas y una cantidad de pistas diferentes, mientras la dificultad sea mas dificil mas facil va a ser perder el scaperoom. Entres las dificultades disponibles estan:

1. Facil (Noob)
El modo facil, es un modo para jugar tranqulamente sin preocupacion de perder facilmente, suelen usarlo los noobs para aprender a jugar. (Si juegas aqui eres malo)
En esta dificltad se te brindaran:
- Tiempo: {t_facil} s
- Vidas: {vidas_facil}
- Pistas: {clues_facil}

2. Medio (Ok)
El modo intermedio(Medio), es un modo que se suele utilizar para practicar y mejorar en el juego, suelen usarlos los jugadores ok que nos son ni buenos ni malos.
En esta dificltad se te brindaran:
- Tiempo: {t_media} s
- Vidas: {vidas_media}
- Pistas: {clues_media}

3. Dificil (Wow)
El modo dificil, es un modo para jugadores experimentados los cuales son buenos en el juego y saben que van a lograr completar el juego con una vida y pocas pistas, suelen jugar los jugadores buenos que los ves y dices Woow.
En esta dificltad se te brindaran:
- Tiempo: {t_dificil} s
- Vidas: {vidas_dificil}
- Pistas: {clues_dificil}

4. Extremo (Try Hard)
En el modo extremo, es un modo de juego que es poco posible que pases, este modo esta creado para jugadores pro los cuales conocen el juego completo y no tienen miedo a perder, suelen jugar los jugadores Try Hards o los profesionales, si lo seleccionas lo ma probable es que pierdas.
En esta dificltad se te brindaran:
- Tiempo: {t_extremo} s
- Vidas: {vidas_extremo}
- Pistas: {clues_extremo}
''')
    dificultad = input('Ingrese el numero correspondiente a la dificultad en la que desea jugar\n1.Facil\n2.Medio\n3.Dificil\n4.Extremo\n> ')
    while dificultad != '1' and dificultad != '2' and dificultad != '3' and dificultad != '4':
        dificultad = input('Por favor ingrese el numero correspondiente a una dificultad valida\n> ')
    if dificultad == '1':
        print(f'''
Ok, jugaras en dificultad Facil y dispondras de
- Tiempo: {t_facil} s
- Vidas: {vidas_facil}
- Pistas: {clues_facil}
''')
        vidas = vidas_facil
        clues = clues_facil
        t = t_facil
        deficultad = 'Facil'
        return vidas, clues, t, dificultad

    elif dificultad == '2':
        print(f'''
Bien, jugaras en dificultad media y dispondras de
- Tiempo: {t_media} s
- Vidas: {vidas_media}
- Pistas: {clues_media}
''')
        vidas = vidas_media
        clues = clues_media
        t = t_media
        dificultad = 'Media'
        return vidas, clues, t, dificultad

    elif dificultad == '3':
        print(f'''
Perfecto, jugaras en dificultad dificil y dispondras de
- Tiempo: {t_dificil} s
- Vidas: {vidas_dificil}
- Pistas: {clues_dificil}
''')
        vidas = vidas_dificil
        clues = clues_dificil
        t = t_dificil 
        dificultad = 'Dificil'
        return vidas, clues, t, dificultad

    elif dificultad == '4':
        print(f'''
Wao, jugaras en dificultad extrema y dispondras de
- Tiempo: {t_extremo} s
- Vidas: {vidas_extremo}
- Pistas: {clues_extremo}
''')
        vidas = vidas_extremo
        clues = clues_extremo
        t = t_extremo
        dificultad = 'Extremo'
        return vidas, clues, t, dificultad

from chequaer_tiempo_vidas import chequear_vidas, chequear_tiempo
import vida
import time

# Poner el usuario como parametro
def play(vidas, clues, t, user_plaiyng, cuartos_visitados, avatar_plaiyng, tiempo_final):
    start = time.monotonic()
    for i in range(t):
        while vidas > 0:
            objetos = {'obj1_1' : False, 'obj2_1' : False, 'obj3_1' : False, 'obj1_2' : False, 'obj2_2' : False, 'obj3_2' : False, 'obj1_3' : False, 'obj2_3' : False, 'obj3_3' : False, 'obj1_4' : False, 'obj1_5' : False, 'obj2_5' : False, 'obj3_5' : False}
            vidas_clues = {'vidas': vidas, 'clues': clues}
            inventario = []
            print('\n')
            print(f'Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {t} segundos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?')
            print('\n')
            aceptas = input('Ingresa el numero de lo que deseas \n1.Aceptas\n2.Rechazas\n> ')
            print('\n')
            while aceptas != '1' and aceptas != '2':
                aceptas = input('Por favor ingrese el numero correspondiente a una opcion valida\n> ')
            if aceptas == '1':
                print('\n')
                print(f'Bienvenido {avatar_plaiyng}, gracias por tu disposición a ayudarnos a resolver este inconveniente, te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.')
                while True:
                    print('\n')
                    print(images_cuarto2.biblioteca)
                    print('\n')
                    direccion = input('''
Ingrese el numero de la opcion que deseas realizar
1. <-- Habitacion de la izquierda
2. ^ Entrar en la habitacion 
3. --> Habitacion de la derecha
4. Ver vidas y tiempo
>  ''')
                    perdiste_t = (chequear_tiempo(start, t))
                    perdiste_v = (chequear_vidas(vidas_clues))
                    if perdiste_v == False:
                        return False
                    elif perdiste_t == False:
                        return False
                    else:
                        print('\n')
                        while direccion != '1' and direccion != '2' and direccion != '3' and direccion != '4':
                            direccion = input('Por favor ingrese el numero de una opcion valida\n> ')
                        while direccion == '2':
                            cuartos_visitados['Biblioteca'] += 1
                            perdiste = cuartos.cuarto_2(inventario, objetos, vidas_clues, start, t)
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            elif perdiste == False:
                                return False
                            else:
                                break
                        while direccion == '4':
                            print('\n')
                            vida.mostrar_vidas(vidas_clues)
                            print('\n')
                            end = time.monotonic()
                            t_transcurrido = int(end - start)
                            print(t_transcurrido, 's')
                            print('\n')
                            salir = input('Desea volver\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                            while salir != '1' and salir != '2':
                                salir = input('Por favor ingrese un numero valido\n> ')
                            if salir == '1':
                                break
                        while direccion == '1':
                            print('\n')
                            print(images_cuarto3.plaza_rectorado)
                            print('\n')
                            direccion_1 = input('''
Ingrese el numero de la opcion que deseas realizar
1. ^ Entrar en la habitacion 
2. --> Habitacion de la derecha
3. Ver vidas y tiempo
>  ''')
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                while direccion_1 != '1' and direccion_1 != '2' and direccion_1 != '3':
                                    direccion_1 = input('Por favor ingrese el numero de una opcion valida\n> ')
                                if direccion_1 == '2':
                                    break
                                while direccion_1 == '1':
                                    cuartos_visitados['Plaza_rectorado'] += 1
                                    perdiste = cuartos.cuarto_3(inventario, objetos, vidas_clues, start, t)
                                    perdiste_t = (chequear_tiempo(start, t))
                                    perdiste_v = (chequear_vidas(vidas_clues))
                                    if perdiste_v == False:
                                        return False
                                    elif perdiste_t == False:
                                        return False
                                    elif perdiste == False:
                                        return False
                                    else:
                                        break
                                    break
                                while direccion_1 == '3':
                                    print('\n')
                                    vida.mostrar_vidas(vidas_clues)
                                    print('\n')
                                    end = time.monotonic()
                                    t_transcurrido = int(end - start)
                                    print(t_transcurrido, 's')
                                    print('\n')
                                    salir = input('Desea volver\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                                    while salir != '1' and salir != '2':
                                        salir = input('Por favor ingrese un numero valido\n> ')
                                    if salir == '1':
                                        break
                        while direccion == '3':
                            print(images_cuarto4.pasillo_laboratorios)
                            direccion_2 = input('''
Ingrese el numero de la opcion que deseas realizar
1. ^ Entrar en la habitacion 
2. <-- Habitacion de la izquierda
3. Ver vidas y tiempo
>  ''')
                            perdiste_t = (chequear_tiempo(start, t))
                            perdiste_v = (chequear_vidas(vidas_clues))
                            if perdiste_v == False:
                                return False
                            elif perdiste_t == False:
                                return False
                            else:
                                while direccion_2 != '1' and direccion_2 != '2' and direccion_2 != '3' and direccion_2 != '4':
                                    direccion_2 = input('Por favor ingrese el numero de una opcion valida\n> ')
                                while direccion_2 == '3':
                                    print('\n')
                                    vida.mostrar_vidas(vidas_clues)
                                    print('\n')
                                    end = time.monotonic()
                                    t_transcurrido = int(end - start)
                                    print(t_transcurrido, 's')
                                    print('\n')
                                    salir = input('Desea volver\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                                    while salir != '1' and salir != '2':
                                        salir = input('Por favor ingrese un numero valido\n> ')
                                    if salir == '1':
                                        break
                                if direccion_2 == '2':
                                    break
                                while direccion_2 == '1':
                                    if objetos['obj1_4'] == False:
                                        cuartos_visitados['Pasillo_laboratorios'] += 1
                                        perdiste = cuartos.cuarto_4(inventario, objetos, vidas_clues, start, t)
                                        perdiste_t = (chequear_tiempo(start, t))
                                        perdiste_v = (chequear_vidas(vidas_clues))
                                        if perdiste_v == False:
                                            return False
                                        elif perdiste_t == False:
                                            return False
                                        elif perdiste == False:
                                            return False
                                        else:
                                            break
                                    elif objetos['obj1_4'] == True:
                                        print(images_cuarto4.puerta_entrar)
                                        print('\n')
                                        d = input('Ingrese el numero de la opcion que desea realizar\n1. ^ Inspeccionar la puerta\n2. ^^ Entrar al cuarto\n3. v Volver al pasillo\n> ')
                                        while d != '1' and d != '2' and d != '3':
                                            d = input('Por favor ingrese un numero valido\n> ')
                                        if d == '1':
                                            cuartos_visitados['Pasillo_laboratorios'] += 1
                                            perdiste = cuartos.cuarto_4(inventario, objetos, vidas_clues, start, t)
                                            perdiste_t = (chequear_tiempo(start, t))
                                            perdiste_v = (chequear_vidas(vidas_clues))
                                            if perdiste_v == False:
                                                return False
                                            elif perdiste_t == False:
                                                return False
                                            elif perdiste == False:
                                                return False
                                            else:
                                                break
                                        elif d == '3':
                                            break
                                        else: 
                                            while True:
                                                print(images_cuarto1.laboratorio)
                                                direccion_3 = input('''
Ingrese el numero de la opcion que deseas realizar
1. <-- Volver al pasillo
2. ^ Entrar en la habitacion 
3. --> habitacion de la derecha
4. Ver vidas y tiempo
>  ''')
                                                perdiste_t = (chequear_tiempo(start, t))
                                                perdiste_v = (chequear_vidas(vidas_clues))
                                                if perdiste_v == False:
                                                    return False
                                                elif perdiste_t == False:
                                                    return False
                                                else:
                                                    while direccion_3 != '1' and direccion_3 != '2' and direccion_3 != '3' and direccion_3 != '4':
                                                        direccion_3 = input('Por favor ingrese el numero de una opcion valida\n> ')
                                                    if direccion_3 == '1':
                                                        break
                                                    while direccion_3 == '2':
                                                        cuartos_visitados['Laboratorio_SL001'] += 1
                                                        perdiste = cuartos.cuarto_1(inventario, objetos, vidas_clues, start, t)
                                                        perdiste_t = (chequear_tiempo(start, t))
                                                        perdiste_v = (chequear_vidas(vidas_clues))
                                                        if perdiste_v == False:
                                                            return False
                                                        elif perdiste_t == False:
                                                            return False
                                                        elif perdiste == False:
                                                            return False
                                                        else:
                                                            break
                                                    while direccion_3 == '4':
                                                        print('\n')
                                                        vida.mostrar_vidas(vidas_clues)
                                                        print('\n')
                                                        end = time.monotonic()
                                                        t_transcurrido = int(end - start)
                                                        print(t_transcurrido, 's')
                                                        print('\n')
                                                        salir = input('Desea volver\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                                                        while salir != '1' and salir != '2':
                                                            salir = input('Por favor ingrese un numero valido\n> ')
                                                        if salir == '1':
                                                            break
                                                    while direccion_3 == '3':
                                                        print(images_cuarto5.cuarto_de_servidores)
                                                        direccion_4 = input('''
Ingrese el numero de la opcion que deseas realizar
1. ^ Entrar en la habitacion 
2. <-- Habitacion de la izquierda
3. Ver vidas y tiempo
>  ''')
                                                        perdiste_t = (chequear_tiempo(start, t))
                                                        perdiste_v = (chequear_vidas(vidas_clues))
                                                        if perdiste_v == False:
                                                            return False
                                                        elif perdiste_t == False:
                                                            return False
                                                        else:
                                                            while direccion_4 != '1' and direccion_4 != '2' and direccion_4 != '3':
                                                                direccion_4 = input('Por favor ingrese el numero de una opcion valida\n> ')
                                                            while direccion_4 == '1':
                                                                cuartos_visitados['Cuarto_de_servidores'] += 1
                                                                perdiste = cuartos.cuarto_5(inventario, objetos, vidas_clues, start, t, tiempo_final)
                                                                if perdiste == True:
                                                                    return True
                                                                elif perdiste == False:
                                                                    return False
                                                                else:
                                                                    break
                                                            if direccion_4 == '2':
                                                                break
                                                            while direccion_4 == '3':
                                                                print('\n')
                                                                vida.mostrar_vidas(vidas_clues)
                                                                print('\n')
                                                                end = time.monotonic()
                                                                t_transcurrido = int(end - start)
                                                                print(t_transcurrido, 's')
                                                                print('\n')
                                                                salir = input('Desea volver\n1.Si\n2.No\nIngrese el numero de la opcion que desea\n> ')
                                                                while salir != '1' and salir != '2':
                                                                    salir = input('Por favor ingrese un numero valido\n> ')
                                                                if salir == '1':
                                                                    break
            else:
                print('Gracias a ti, y tu falta de valor la universiadad fue destruida')
                break
        
        if vidas <= 0:
            print('El juego no puede empezar con menos de 0 vidas')
            return False
