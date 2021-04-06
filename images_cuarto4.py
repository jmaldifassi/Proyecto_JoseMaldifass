import api_4

space = '\n' * 1

pasillo_laboratorios = f'''
- - - - - - - {api_4.name_cuarto4} - - - - - - -  
|     |     _______________________      |     |
|  /| |    |                       |     | |\  |
| | | |    |                       |     | | | |
| | | |    |                       |     | | | |
| | | |    |                       |     | | | |
| | | |    |                       |     | | | |
| | | |    |                     0 |     | | | |
| | | |    |                     0 |     | | | |
| | | |    |                       |     | | | |
| | | |____|_______________________|_____| | | |
| |/                                        \| |
|/                                            \|
------------------------------------------------
Hacia a donde quiero ir?
''' + space

puerta_con_candado_dentro = f'''
- - - - - {api_4.name_cuarto4} - - - -   
|       _______________________       |
|      |                       |      |
|      |                       |      |
|      |                       |      |
|      |                       |      |
|      |                       |      |
|      |                     0 |      |
|      |                     0 |      |
|      |                       |      |
|______|_______________________|______|
|                                     |
|                                     |
---------------------------------------
Ok, estor en {api_4.name_cuarto4}
y veo una puerta
''' + space

puerta_con_candado = f'''
- - - - - {api_4.name_cuarto4} - - - -   
|       _______________________       |
|      |                       |      |
|      |                       |      |
|      |                       |      |
|      |                       |      |
|      |                       |      |
|      |                     0 |      |
|      |                     0 |      |
|      |                       |      |
|______|_______________________|______|
|                                     |
|                                     |
---------------------------------------
Conchale, esta cerrada con candado, 
para lograr jugar esto necesitare abrir 
la puerta que esta ahi
Para poder abrir necesitare algo
El minijuego que puedo jugar aqui es
{api_4.name_game_obj1}
Las reglas del juego son 
{api_4.rules_game_obj1}
''' + space

puerta_sin_candado_con_libro = f'''
- - - - - - - - - - {api_4.name_cuarto4} - - - - - - - - - - - 
|       ______________________ _______________________       |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      | 0                    |                       |      |
|      | 0                    |         _____         |      |
|      |                      |        |     |        |      |
|______|______________________|________|_____|________|______|
|                                                            |
|                                                            |
-------------------------------------------------------------
Bien, gane el minijuego, ahora podre 
obtener el {api_4.premio_game_obj1} que se 
encuentra ahi y si me devuelvo al pasillo y 
entro de nuevo podre entrar a los laboratorios
''' + space

puerta_sin_candado_sin_libro = f'''
- - - - - - - - - - {api_4.name_cuarto4} - - - - - - - - - - - 
|       ______________________ _______________________       |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      | 0                    |                       |      |
|      | 0                    |                       |      |
|      |                      |                       |      |
|______|______________________|_______________________|______|
|                                                            |
|                                                            |
-------------------------------------------------------------
Ok, ya estuve aqui y ahora no hay nada :(
''' + space

puerta_entrar = f'''
- - - - - - - - - - {api_4.name_cuarto4} - - - - - - - - - - - 
|       ______________________ _______________________       |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      |                      |                       |      |
|      | 0                    |                       |      |
|      | 0                    |                       |      |
|      |                      |                       |      |
|______|______________________|_______________________|______|
|                                                            |
|                                                            |
-------------------------------------------------------------
''' + space