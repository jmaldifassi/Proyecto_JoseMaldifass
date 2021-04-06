from Clases import Username

def check_user(users):
    existe = False
    print('Bienvenido de nuevo a scapemet, ingrese su username para acceder.')
    username = input('> ')
    password = input(f'Ingrese la contraseña del username {username}\n> ')
    cuenta = (username, password)
    account = []
    usuarios = []
    for n in range(len(users)):
        username_ = users[n].get_username()
        password_ = users[n].get_password()
        avatar = users[n].avatar
        age = users[n].get_age()
        user = [username, pasword, age, avatar]
        usuarios.append(user)
        cuenta_ = (username_, password_)
        account.append(cuenta_)
    while not cuenta in account:
        print('Ingreso mal la contraseña o el username, intente de nuevo')
        return False
    if cuenta_ in account:
        existe = True
        print(f'''
        - - - Bienvenido - - -
        Username = {username}
        Un gusto tenerte de vuelta
        ''')
        return user

def chequear_username(users, username):
    existe = True
    for n in range(len(users)):
        usernames = (n, users[n].get_username())
        while (username in usernames):
            username = input('El username que ingreso ya existe, porfavor intente ingresar otro\n> ')
        if not (username in usernames):
            print('Su username es unico y fue ingresado correctamente')
            existe = False

def longitud(pasword):
    if len(pasword) >= 8:
        return True
    else:
        False
def mayuscula(pasword):
    for caracter in pasword:
        if caracter.isupper():
            return True
        else:
            False
def minuscula(pasword):
    for caracter in pasword:
        if caracter.islower():
            return True
        else:
            False
def numero(pasword):
    for caracater in pasword:
        if caracater.isnumeric():
            return True
        else:
            False

def pasword():
    pasword = []
    print('Su nueva contraseña debe seguir los siguinetes parametros: \n- Debe ser de 8 Caracteres\n- Contener letras en miniuscula y mayuscula\n- Debe contener al menos un numero ')
    pasword = input('Ingrese su nueva contraseña\n> ')
    while (not longitud(pasword)) or (not mayuscula(pasword)) or (not minuscula(pasword)) or (not numero(pasword)):
        pasword = input('Porfavor ingrese una clave valida con los requisitos\n> ')
    print('Contraseña ingresada con exito!')
    return pasword

def add_user(users):
    print('\n')
    print('Bienvenido a scapemet, crea un nuevo username para tu cuenta, con este username guardaras todos los datos de tus juegos. ')  
    print('\n')
    username = input('Ingrese un Username que desee, este sera unico\n> ')
    while username == ' ' or username == '' or (len(username) >= 13):
        username = input('Porfavor ingrese un username valido, que no tenga espacios, ni sea nada\n> ')
    print('\n')
    chequear_username(users, username)
    print('\n')
    password = pasword()
    print('\n')
    age = input('Ingrese su edad\n> ')
    while (not age.isnumeric()) or (int(age) not in range(1,130)):
        age = input ('Por favor ingrese una edad vaida\n> ')
    print('\n')
    avatar = input('Por favor ingrese el numero del avatar que desea utilizar\n1.Scharifker\n2.Eugenio Mendoza\n3.Pelusa\n4.Gandhi,\n5.Morgan Fredman\n6.Lorenzo Mendoza\n7.Gamboa\n> ')
    while (not avatar.isnumeric()) or (int(avatar) not in range(1,8)):
        avatar = input('Por favor ingrese el nummero de un avatar valido\n> ')
    if avatar == '1':
        avatar = 'Scharifker'
    elif avatar == '2':
        avatar = 'Eugenio Mendoza'
    elif avatar == '3':
        avatar = 'Pelusa'
    elif avatar == '4':
        avatar = 'Gandhi'
    elif avatar == '5':
        avatar = 'Morgan Fredman'
    elif avatar == '6':
        avatar = 'Lorenzo Mendoza'
    else:
        avatar = 'Gamboa'
    user = Username(username,password,age,avatar)
    users.append(user)
    user.mostrar()
    return user

def ingresar_user(users):
    print('\n')
    usuario = check_user(users)
    return usuario
    print('\n')

    



