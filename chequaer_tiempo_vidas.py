def chequear_vidas(vidas_clues):
    if vidas_clues['vidas'] <= 0:
        print('\n')
        print('SE TE ACABARON LAS VIDAS')
        print('\n')
        return False
    else:
        return True

import time

def chequear_tiempo(start, t):
    end = time.monotonic()
    t_transcurrido = int(end - start)
    if t_transcurrido > t:
        print('\n')
        print('SE TE ACABO EL TIEMPO')
        return False
    else:
        return True