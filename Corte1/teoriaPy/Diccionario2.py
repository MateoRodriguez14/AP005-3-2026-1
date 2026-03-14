#################Diccionarios Parte 2####################

#Acceder a los valores por medio de la clave
alturaEdificios = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} 
print(alturaEdificios["Burj Khalifa"]) 
print(alturaEdificios["Ping An"])
#print(alturaEdificios["Ping A"]) En caso de ingresar una clave que no 
#esta en el diccionarios se generara un error

elementosZodiaco = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(elementosZodiaco["earth"]) #Tambien sirve para diccionarios cuyo valor son listas
print(elementosZodiaco["fire"])


#Revisar si una clave si se encuentra en el diccionario
revisarClave = "Landmark 81"

if revisarClave in alturaEdificios:
    print(alturaEdificios["Landmark 81"])
else:
    print("No se ha encontrado la clave Landmark 81")


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a Zodiac element"
if "energy" in zodiac_elements:
   print(zodiac_elements["energy"])


#Forma segura de obtener los valores
print(alturaEdificios.get("Shanghai Tower"))
print(alturaEdificios.get("BD Bacata"))#En este caso imprime none


user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
print(user_ids.get("teraCoder"))

if user_ids.get("teraCoder") == None:
    tc_id = 1000
else: 
    tc_id = user_ids.get("teraCoder")

print(tc_id)

if user_ids.get("superStackSmash") == None:
      stack_id = 100000

print(stack_id)


#Eliminar una clave
# .pop() elimina una clave espoecifica y devuelve su valor asociado
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
print(raffle)

#En el siguiente caso, al no existir la clave 10000 .pop retornara "No Prize"
raffle =  {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))


itemsDisponibles = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
puntosdeVida = 20
#EN el siguiente codigo emplea .pop para ir eliminando elementos del diccionario
#y obteniendo sus valores para realizar una operacion de suma a la variable puntosdeVida
puntosdeVida += itemsDisponibles.pop("stamina grains", 0)
puntosdeVida += itemsDisponibles.pop("power stew", 0)
puntosdeVida += itemsDisponibles.pop("mystic bread", 0)

print(itemsDisponibles)
print(puntosdeVida)

#Para oobtener todas las claves
puntajeTests = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(puntajeTests)) #almacena las claves en una lista momentanea
listaParticipantes = list(puntajeTests)
print(listaParticipantes)

#Otra forma de obtener las claves
for estudiante in puntajeTests.keys():
    print(estudiante)



user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
#Guarda las claves en un objeto de la clase dict_keys
users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)
print(type(users))
print(type(lessons))
print()
print()
print()
print("Para obtener todos los valores del diccionario puntajeTests")
print()
print()
print()
for listaPuntaje in puntajeTests.values():
    print(listaPuntaje)

puntajes = puntajeTests.values()
print(puntajes)
print(type(puntajes)) #Al igual que con las claves se pueden almacenar los valores
#en el objeto de la clase dict_values

#Obtener los valores y operarlos
numEjercicios = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
totalEjercicios = 0

for ejercicios in num_exercises.values():
   totalEjercicios += ejercicios
   print(totalEjercicios)

print(totalEjercicios)

#Para obtener todos los items y manejarlos

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
#.items() devuelve una vista dinamica de pares (clave, valor) de un diccionario en forma de tuplas
empresas = biggest_brands.items()
print(empresas)
print(type(empresas))

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
   print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 