# Definición de los datos de entrada y valores especificos

# Datos base para creación de usuario (como especifica la lección)

headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

# Función para generar cuerpos de kit

def get_kit_body(name):
    return {"name": name} if name is not None else {}


   #--- Casos de Prueba ---

#Casos positivos CD:(201)
TEST1_KIT_1_CHAR = get_kit_body("a")                   #Caso 1: 1 	El número permitido de caracteres (1)  (código 201 esperado
TEST2_KIT_511_CHAR = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC" )           #Caso 2: El número maximo permitido es 511 Caracteres (código 201 esperado)
TEST5_KIT_SPECIAL_CHAR = get_kit_body("№%@")           #Caso 3: Se permiten caracteres especiales (código 201 esperado)
TEST6_KIT_SPACE = get_kit_body("A Aaa")                #Caso 6: Se permiten espacios (código 201 esperado)
TEST7_KIT_NUMBER = get_kit_body("123")                 #Caso 7: Se permiten números (código 201 esperado)

#Casos negativos CD:(400)
TEST3_KIT_EMPTY_NAME = get_kit_body("")                #Caso 3: El número de caracteres es menor que la cantidad permitida (código 400 esperado)
TEST4_KIT_512_CHAR = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")           #Caso 4: El número de caracteres es mayor que la cantidad permitida (512) (código 400 esperado)
TEST8_KIT_NO_NAME = {"name": ""}                       #Caso 8: name vacío (código 400 esperado)
TEST9_KIT_NUMBER_NAME = {"name": 123}                  #Caso 9: Se ha pasado un tipo de parámetro diferente (número) (código 400 esperado)

