class Username:
    def __init__(self, username, password, age, avatar):
        self.__username = username
        self.__password = password
        self.__age = age
        self.avatar = avatar
    
    def mostrar(self):
        print(f'''
            Username = {self.__username}
            Pasword = {self.__password}
            Age = {self.__age}
            Avatar = {self.avatar}
        ''')
           
    def get_username(self):
        return self.__username

    def set_username(self):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self):
        self.__password = password
    
    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age = age

class Game(Username):
    def __init__(self, username, pasword, age, avatar, time, result, dificulty, cuarto_f, partidas_jugadas):
        super().__init__(username, pasword, age, avatar)
        self.time = time
        self.result = result
        self.dificulty = dificulty
        self.cuarto_f = cuarto_f
        self.partidas_jugadas = partidas_jugadas



class Cuarto():
    def __init__(self,cuarto_name):
        self.cuarto_name = cuarto_name

class Objeto(Cuarto):
    def __init__(self, cuato_name, name_obj, posicion, juego):
        super.__init__(cuato_name)
        self.name_obj = name_obj
        self.posicion = posicion
        self.juego = juego # esto es un objeto de algún hijo la clase Juego

from abc import ABC, abstractclassmethod

class Juego(ABC):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules):
        self.requirement = requirement
        self.name = name
        self.award = award
        self.rules = rules
        # @abstractclassmethod

class Inventario():
    def __init__(self, carnet, llave, cable_hdmi, mensaje_graduarte, disco_duro, libro_mate, martillo, libro_fisica, contrasena, titulo_universitario):
        self.carnet = carnet
        self.llave = llave
        self.cable_hdmi = cable_hdmi
        self.mensaje_graduarte = mensaje_graduarte
        self.disco_duro = disco_duro
        self.libro_mate = libro_mate
        self.martillo = martillo
        self.contrasena = contrasena
        self.libro_fisica = libro_fisica
        self.titulo_universitario = titulo_universitario

class Sopa_letras(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, answer_1, answer_2, answer_3, clue_1, clue_2, clue_3):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.clue_1 = clue_1
        self.clue_2 = clue_2
        self.clue_3 = clue_3

class Preguntas_python(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, answer, clue_1, clue_2, clue_3):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.answer = answer
        self.clue_1 = clue_1
        self.clue_2 = clue_2
        self.clue_3 = clue_3

class Adivinanzas(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, answers, clue_1, clue_2, clue_3):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.answers = answers
        self.clue_1 = clue_1
        self.clue_2 = clue_2
        self.clue_3 = clue_3

class Ahorcado(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, answer, clue_1, clue_2, clue_3):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.answer = answer
        self.clue_1 = clue_1
        self.clue_2 = clue_2
        self.clue_3 = clue_3

class Preguntas_mate(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, answer, clue_1):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.answer = answer
        self.clue_1 = clue_1

class Criptograma(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, desplazamiento):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.desplazamiento = desplazamiento

class Logica(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question

class Quiz_cultura_unimetana(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, correct_answer, answer_2, answer_3, answer_4, clue_1):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.correct_answer = correct_answer
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        self.clue_1 = clue_1

class Memoria(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, clue_1):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.clue_1 = clue_1

class Logicab(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, answer):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.answer = answer

class Palabra_mezclada(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, category, words):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.category = category
        self.words = words


class Numero_entre(Juego):
    def __init__(self, cuarto_name, name_obj, posicion, requirement, name, award, rules, question, clue_1):
        super.__init__(cuarto_name, name_obj, posicion, requirement, name, award, rules)
        self.question = question
        self.clue_1 = clue_1