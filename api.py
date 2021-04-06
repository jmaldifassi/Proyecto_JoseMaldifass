import requests
import Clases

def api():
    url = 'https://api-escapamet.vercel.app/' 
    response = requests.get(url)
    response = response.json()

    for cuarto in response:
        cuarto_name = cuarto['name']

    for objeto in cuarto['objects']:
        name_obj = objeto['name']
        poscion = objeto['name']

        for game in objeto['game']:
            requerimiento = game['requirement']
            game_name = game['name']
            premio = game['award']
            rules = game['rules']

            for question in game['questions']:
                question = question['question']
                answers = question['answers']
                answer = question['answer']
                answer_1 = question['answer_1']
                answer_2 = question['answer_2']
                answer_3 = question['answer_3']
                answer_4 = question['answer_4']
                correct_answer = question['correct_answer']
                clue_1 = question['clue_1']
                clue_2 = question['clue_2']
                clue_3 = question['clue_3']
                desplazamiento = question['desplazamiento']
                category = question['category']
                words = question['words']
            
                sopa_letras = Clases.Sopa_letras(answer_1, answer_2, answer_3, clue_1, clue_2, clue_3)
                preguntas_python = Clases.Preguntas_python(question, answer, clue_1, clue_2, clue_3)
                adivinanzas = Clases.Adivinanzas(question, answers, clue_1, clue_2, clue_3)
                ahorcadoTemp = Clases.Ahorcado(question, answer, clue_1, clue_2, clue_3)
                preguntas_mate = Clases.Preguntas_mate(question, answer, clue_1)
                criptograma = Clases.Criptograma(question, desplazamiento)
                logica = Clases.Logica(question)
                quiz = Clases.Quiz_cultura_unimetana(question, correct_answer, answer_2, answer_3, answer_4, clue_1)
                memoria = Clases.Memoria(question, clue_1)
                logicab = Clases.Logicab(question, answer)
                palabra_mezclada = Clases.Palabra_mezclada(question, category, words)
                numero_entre = Clases.Numero_entre(question, answer, clue_1)
 
            game = Clases.Juego(requirement, name, award, rules)
        
        obj= Clases.Objeto(name_obj, posicion)
    
    Cuarto = Clases.Cuarto(cuarto_name)

url = 'https://api-escapamet.vercel.app/' 
response = requests.get(url)
response = response.json()
cuarto_1 = response[0]
cuarto_2 = response[1]
cuarto_3 = response[2]
cuarto_4 = response[3]
cuarto_5 = response[4]

