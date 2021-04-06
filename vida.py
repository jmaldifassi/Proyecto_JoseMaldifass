import images_vidas

def mostrar_vidas(vidas_clues):
    if vidas_clues['vidas'] == 5:
        print(images_vidas.vidas_5)
    elif vidas_clues['vidas'] == 4.75:
        print(images_vidas.vidas_5_3cuartos)
    elif vidas_clues['vidas'] == 4.5:
        print(images_vidas.vidas_5_media)
    elif vidas_clues['vidas'] == 4.25:
        print(images_vidas.vidas_5_1cuarto)
    elif vidas_clues['vidas'] == 4:
        print(images_vidas.vidas_4)
    elif vidas_clues['vidas'] == 3.75:
        print(images_vidas.vidas_4_3cuartos)
    elif vidas_clues['vidas'] == 3.5:
        print(images_vidas.vidas_4_media)
    elif vidas_clues['vidas'] == 3.25:
        print(images_vidas.vidas_4_1cuarto)
    elif vidas_clues['vidas'] == 3:
        print(images_vidas.vidas_3)
    elif vidas_clues['vidas'] == 2.75:
        print(images_vidas.vidas_3_3cuartos)
    elif vidas_clues['vidas'] == 2.5:
        print(images_vidas.vidas_3_media)
    elif vidas_clues['vidas'] == 2.25:
        print(images_vidas.vidas_3_1cuarto)
    elif vidas_clues['vidas'] == 2:
        print(images_vidas.vidas_2)
    elif vidas_clues['vidas'] == 1.75:
        print(images_vidas.vidas_2_3cuartos)
    elif vidas_clues['vidas'] == 1.5:
        print(images_vidas.vidas_2_media)
    elif vidas_clues['vidas'] == 1.25:
        print(images_vidas.vidas_2_1cuarto)
    elif vidas_clues['vidas'] == 1:
        print(images_vidas.vidas_1)
    elif vidas_clues['vidas'] == 0.75:
        print(images_vidas.vidas_1_3cuartos)
    elif vidas_clues['vidas'] == 0.5:
        print(images_vidas.vidas_1_media)
    elif vidas_clues['vidas'] == 0.25:
        print(images_vidas.vidas_1_1cuarto)
    elif vidas_clues['vidas'] == 0: 
        print(images_vidas.vidas_0)

import time

# Sacar del json el tiempo del juego

def timer(t):
    if t > 0:
        minuts = t // 60
        seconds = t % 60
        t_corriendo = '{:02d}:{:02d}'.format(minuts, seconds)
        time.sleep(1)
        t -= 1
        return t_corriendo

def show_time(t_corriendo):
    print( t_corriendo) 
        