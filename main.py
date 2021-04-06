from solicitardatos import add_user ,ingresar_user
from play import play, reglas, bienvenida, dificultad
import pickle
import os
from Clases import Game

# Funcion para recivir los datos del txt
def recivir_datos_del_txt(nombre_txt,datos):
    lectura_binaria = open(nombre_txt,'rb')
    if os.stat(nombre_txt).st_size != 0:
        datos = pickle.load(lectura_binaria)
    lectura_binaria.close()

    return datos
# Retorna los datos, los cuales van a ser metidos en una lista

# Funcion para cargar datos al txt
def cargar_datos(nombre_txt,datos):
    escritura_binaria = open(nombre_txt,'wb')
    datos = pickle.dump(datos,escritura_binaria)
    escritura_binaria.close()

from Clases import Game
# Funcion de estadisticas, que muestra las estadisticas, con los records
def estadisticas(records):
        # Se sacan los datos del txt de los records
    records.sort(key = lambda record: record.time, reverse = True)
    for n in records:
        result = n.result
        dificultad = n.dificulty
        username = n.get_username()
        cuarto_f = n.cuarto_f
        time = n.time
    for i, j in enumerate(records):
        if result == 'Ganaste':
        # Segun la dificultad se muestran los records de las personas
        #  y se muestra segun el tiempo que obtuvo, tambien se muestra el cuarto 
        # que mas visito en la partida
            if dificultad == 'Extremo':
                if i < 5:
                    print('Leaderbords Modo: Extremo')
                    print(f'- - - {i+1} - - -')
                    print(f'''
Username: {username}
Tiempo de partida: {time} s
Cuarto mas visitado: {cuarto_f}
Dificultad: {dificultad}
    ''')
            elif dificultad == 'Dificil':
                if i < 5:
                    print('Leaderbords Modo: Dificil')
                    print(f'- - - {i+1} - - -')
                    print(f'''
Username: {username}
Tiempo de partida: {time} s
Cuarto mas visitado: {cuarto_f}
Dificultad: {dificultad}
    ''')
            elif dificultad == 'Media':
                if i < 5:
                    print('Leaderbords Modo: Media')
                    print(f'- - - {i+1} - - -')
                    print(f'''
Username: {username}
Tiempo de partida: {time} s
Cuarto mas visitado: {cuarto_f}
Dificultad: {dificultad}
    ''')
            elif dificultad == 'Facil':
                if i < 5:
                    print('Leaderbords Modo: Facil')
                    print(f'- - - {i+1} - - -')
                    print(f'''
Username: {username}
Tiempo de partida: {time} s
Cuarto mas visitado: {cuarto_f}
Dificultad: {dificultad}
    ''')




users = []
users = recivir_datos_del_txt('Users.txt', users)
# Cargo todos los datos de los users que ya estan registrados 
#  a una lista para despues buscar si el user existe
records = []
records = recivir_datos_del_txt('records.txt', records)
# Cargo todos los records de las partidas jugadas, para despues
# sacar las estadisticas

# Chequeo las partidas que ha jugado el usuario para agregarle 1
# partida mas jugada
def chequear_partidas(records):
    for n in range(len(records)):
        partidas = 0
        partidas = records[n].partidas_jugadas
        return partidas

registrado = False
# Funcion principal en la que se corre todo
# Si se cierra se cierra el programa
def main():
    cuartos_visitados = {'Laboratorio_SL001' : 0, 'Biblioteca' : 0, 'Plaza_rectorado' : 0, 'Pasillo_laboratorios' : 0, 'Cuarto_de_servidores' : 0}
    # Lista que va a guardar los datos del usuario que esta ingresado
    user_plaiyng = []
    bienvenida()
    tiempo_final = []
    while registrado == False:
        seleccion = input('Bienvenido, es usted\n1. Nuevo Usuario\n2. Desea acceder\nIngrese aqui el numero de la opcion que desea\n> ')
        while seleccion != '1' and seleccion != '2':
            seleccion = input('Por favor ingrese el numero de una opcion valida\n> ')
            print('\n')
        if seleccion == '1':
            usuario = add_user(users)
            users.append(usuario)
            user_plaiyng.append(usuario)
            cargar_datos('Users.txt', users)
            registrado == True
            print('Ya esta registrado, ahora ingrese con su cuenta')
            print('\n')
            
        else:
            user = ingresar_user(users)
            while user == False:
                user = ingresar_user(users)
            user_plaiyng.append(user)
            registrado == True
            user = user_plaiyng[0]
            username_plaiyng = user[0]
            pasword_plaiyng = user[1]
            age_plaiyng = user[2]
            avatar_plaiyng = user[3]
            break

    print('Antes de empezar debes leer las reglas')
    while True:
        reglas()
        fuera = input('Ya se leyo las reglas\n1. SI\n2. NO\nIngrese el numero correspondientea la opcion que desea\n> ')
        while fuera != '1' and fuera != '2':
            fuera = input('Por favor ingrese un numero valido\n> ')
        if fuera == '1':
            break
    while True:
        jugar = input('''
1. Jugar
2. Multiplayer (proximamente)
3. Ajustes
4. Estadisticas
5. Salir
- Ingresa el numero de la opcion que desea realizar
> ''')
        while jugar != '1' and jugar != '2' and jugar != '3' and jugar != '4' and jugar != '5':
            jugar = input('Por favor ingrese el numero correspondiente a una opcion valida\n> ')
        while jugar == '1':
            informacion = []
            informacion = dificultad()
            vidas = informacion[0]
            clues = informacion[1] 
            t = informacion[2] 
            dificulty = informacion[3]
            perdiste = play(vidas, clues, t, user_plaiyng, cuartos_visitados, avatar_plaiyng, tiempo_final)
            if perdiste == True:
                salir = input('Ganaste. Deseas salir al menu principal\n1.Si\n\nIngrese el numero de la opcion que desea\n> ')
                result = 'Ganaste'
                t_final = tiempo_final[0]
                partidas = chequear_partidas(records)
                # partidas += 1
                mas_visitas = 0
                for i in cuartos_visitados:
                    visitas = cuartos_visitados[i]
                    if visitas > mas_visitas:
                        if visitas == cuartos_visitados['Laboratorio_SL001']:
                            cuarto_f = 'Laboratorio_SL001'
                        elif visitas == cuartos_visitados['Biblioteca']:
                            cuarto_f = 'Biblioteca'
                        elif visitas == cuartos_visitados['Plaza_rectorado']:
                            cuarto_f = 'Plaza_rectorado'
                        elif visitas == cuartos_visitados['Pasillo_laboratorios']:
                            cuarto_f = 'Pasillo_laboratorios'
                        else:
                             cuarto_f = cuartos_visitados['Cuarto_de_servidores']
                print(cuarto_f)
                record = Game(username_plaiyng, pasword_plaiyng, age_plaiyng, avatar_plaiyng, t_final, result, dificulty, cuarto_f, partidas)
                records.append(record)
                cargar_datos('records.txt', records)
                while salir != '1' :
                    salir = input('Por favor ingresa el numero de una opcion valida\n> ')
                if salir == '1':
                    break
            elif perdiste == False:
                salir = input('PERDISTE. Deseas volver al menu principal\n1.Si\n\nIngrese el numero de la opcion que desea\n> ')
                partidas = chequear_partidas(records)
                result = 'Perdiste'
                # partidas = int(partidas)
                # partidas += 1
                t_final = 0
                mas_visitas = 0
                for i in cuartos_visitados:
                    visitas = cuartos_visitados[i]
                    if visitas > mas_visitas:
                        if visitas == cuartos_visitados['Laboratorio_SL001']:
                            cuarto_f = 'Laboratorio_SL001'
                        elif visitas == cuartos_visitados['Biblioteca']:
                            cuarto_f = 'Biblioteca'
                        elif visitas == cuartos_visitados['Plaza_rectorado']:
                            cuarto_f = 'Plaza_rectorado'
                        elif visitas == cuartos_visitados['Pasillo_laboratorios']:
                            cuarto_f = 'Pasillo_laboratorios'
                        else:
                            cuarto_f = cuartos_visitados['Cuarto_de_servidores']
                record = Game(username_plaiyng, pasword_plaiyng, age_plaiyng, avatar_plaiyng, t_final, result, dificulty, cuarto_f, partidas)
                records.append(record)
                cargar_datos('records.txt', records)
                while salir != '1' :
                    salir = input('Por favor ingresa el numero de una opcion valida\n> ')
                if salir == '1':
                    break
        while jugar == '2':
            print("PROXIMAMENTE")
            print('\n')
            break
        while jugar == '3':
            print('Juega con los ajustes brindados, caprichoso')
            print('\n')
            break
        while jugar == '4':
            seleccion = input('''
Estadisticas
1. Estadisticas Globales
2. Ver partidas jugadas
3. Volver
Ingrese el nimero correspondinte a la opcion que desea            
''')
            while seleccion != '1' and seleccion != '2' and seleccion != '3':
                seleccion = input('Por favor ingrese un numero valido')
            while seleccion == '1':
                estadisticas(records)
                salir = input('Ahi estan las estadisticas cuando desee salir, ingrese 1\n>' )
                while salir != '1':
                    salir = input('Por favor ingrese 1\n> ')
                if salir == '1':
                    break
            while seleccion == '1':
                print('No me dio tiempo de hacer esto :(')
                break
            if seleccion == '3':
                break
        while jugar == '5':
            print('\n')
            print('GRACIAS POR ENTRAR EN ESCAPEMET, HASTA LA PROXIMA\n')
            print('\n')
            return False
        
if __name__ == '__main__':
    main()
    