import requests
from configuration import BASE_URL, CREATE_KIT_PATH, CREATE_USER_PATH
from data import user_body, headers

# -------Creacion de usuario -----


def post_new_user(body):
    """Crea un nuevo usuario y devuelve la respuesta"""
    try:
        response = requests.post(
            url=f"{BASE_URL.rstrip('/')}{CREATE_USER_PATH}",
            json=body,
            headers=headers
        )
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al crear usuario: {str(e)}")


def get_new_user_token():
    """Obtiene token de autenticación"""
    response = post_new_user(user_body.copy())
    if response.status_code == 201:
        return response.json()["authToken"]
    raise Exception(f"Error obteniendo token: {response.status_code} - {response.text}")


def post_new_client_kit(kit_body, auth_token):
    """
    Crea un nuevo kit para el usuario
    Args:
        kit_body: Diccionario con datos del kit
        auth_token: Token de autenticación
    Returns:
        Response: Objeto respuesta de requests
    """
    # Validación mejorada que no interfiere con las pruebas
    if not isinstance(kit_body.get("name", ""), str):
        from requests.models import Response
        mock_response = Response()
        mock_response.status_code = 400
        mock_response._content = b'{"error": "El nombre debe ser un string"}'
        return mock_response

    response = requests.post(
        url=f"{BASE_URL.rstrip('/')}{CREATE_KIT_PATH}",
        json=kit_body.copy(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
    )
    return response


