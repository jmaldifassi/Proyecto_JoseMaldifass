import json


informacion = {}
informacion['dificultad'] = []
informacion['dificultad'].append({
'Vidas': 5,
'Clues': 5,
't': 1500,
'dificultad': 'Facil'})
informacion['dificultad'].append({
'Vidas': 3,
'Clues': 3,
't': 1200,
'dificultad': 'Media'})
informacion['dificultad'].append({
'Vidas': 1,
'Clues': 2,
't': 900,
'dificultad': 'Dificil'})
informacion['dificultad'].append({
'Vidas': 0.5,
'Clues': 0,
't': 420,
'dificultad': 'Extremo'})
with open('informacion.json', 'w') as file:
    json.dump(informacion, file, indent=4)

