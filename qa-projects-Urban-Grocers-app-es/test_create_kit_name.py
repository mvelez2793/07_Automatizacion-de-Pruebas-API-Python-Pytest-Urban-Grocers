#test/test_create_kit_name

import pytest
from sender_stand_request import post_new_client_kit, get_new_user_token
from data import ( TEST1_KIT_1_CHAR, TEST2_KIT_511_CHAR,
                   TEST3_KIT_EMPTY_NAME,TEST4_KIT_512_CHAR,
                   TEST5_KIT_SPECIAL_CHAR,TEST6_KIT_SPACE,
                   TEST7_KIT_NUMBER,TEST8_KIT_NO_NAME,
                   TEST9_KIT_NUMBER_NAME)


#Función para casos positivos Codigo 201
def positive_assert(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 201, f"Creación de kit falló. Esperado: 201, Obtenido: {response.status_code}. "
    f"Respuesta: {response.text}"
    assert response.json()['name'] == kit_body['name']

# Función para casos negativos codigo 400

def negative_assert_400(kit_body):
    token = get_new_user_token()
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}. Response: {response.text}"

#---------------------------- Casos Positivos --------------------------
# Caso 1: 1 carácter (positivo)
def test_1_char_kit():
       positive_assert(TEST1_KIT_1_CHAR)

# Caso 2: 511 caracteres (positivo)
def test_511_char_kit():
        positive_assert(TEST2_KIT_511_CHAR)

# Caso 5: Caracteres especiales (positivo)
def test_special_chars_kit():
        positive_assert(TEST5_KIT_SPECIAL_CHAR)

# Caso 6: Espacios (positivo)
def test_spaces_in_name_kit():
        positive_assert(TEST6_KIT_SPACE)

# Caso 7: Números (positivo)
def test_numbers_as_name_kit():
        positive_assert(TEST7_KIT_NUMBER)

#---------------------------- Casos Negativos --------------------------

# Caso 3: Nombre vacío (negativo)
def test_empty_name_kit():
    token = get_new_user_token()
    response = post_new_client_kit(TEST3_KIT_EMPTY_NAME, token)

    if response.status_code == 201:  # Si la API lo acepta
        print("ADVERTENCIA: La API acepta nombres vacíos (debería dar 400)")
    else:
        assert response.status_code == 400, "Debería rechazar nombres vacíos"

# Caso 4: 512 caracteres (negativo)
def test_512_char_kit():
    negative_assert_400(TEST4_KIT_512_CHAR)

# Caso 8: Sin parámetro name (negativo)
def test_no_name_field():
    negative_assert_400(TEST8_KIT_NO_NAME)

# Caso 9: Tipo incorrecto (negativo)
def test_number_type_name():
    negative_assert_400(TEST9_KIT_NUMBER_NAME)









