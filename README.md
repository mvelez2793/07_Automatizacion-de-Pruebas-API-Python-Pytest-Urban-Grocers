    <div align="right">
     🌍 <strong>Español</strong> | <a href="README_en.md">English</a>
   </div>

# ⚙️ Automatización de Pruebas API (Python + Pytest): Urban Grocers

![Project](https://img.shields.io/badge/Project-API_Test_Automation-blue) ![Language](https://img.shields.io/badge/Language-Python-yellow) ![Framework](https://img.shields.io/badge/Framework-Pytest-green) ![Library](https://img.shields.io/badge/Library-Requests-lightgray)

## 📌 Resumen del Proyecto (Metodología STAR)

*   **Situación:** El equipo de QA de Urban Grocers requería optimizar el tiempo de pruebas de regresión en el backend. Era necesario automatizar la validación del campo `name` en el endpoint de creación de kits de productos (`/api/v1/kits`), asegurando que el servidor manejara correctamente las restricciones de longitud y tipos de datos.
*   **Tarea:** Diseñar, codificar y ejecutar un framework de pruebas automatizadas desde cero utilizando Python, integrando un diseño modular para separar datos, configuraciones y lógica de pruebas (Test Runner).
*   **Acción:** 
    *   Desarrollé un entorno de pruebas automatizadas utilizando el framework **Pytest** y la librería **Requests** para las peticiones HTTP.
    *   Automaticé la generación de precondiciones (creación de usuarios y obtención dinámica de `authToken`) a través de funciones auxiliares.
    *   Implementé 9 casos de prueba basados en **Análisis de Valores Límite**, estresando el sistema con longitudes extremas (1, 511 y 512 caracteres), strings vacíos, caracteres especiales y tipos de datos inválidos (números).
    *   Diseñé aserciones (`assert`) tanto positivas (validando códigos HTTP 201) como negativas (validando códigos HTTP 400).
*   **Resultado:** La suite automatizada se ejecutó con éxito, permitiendo aislar e informar **vulnerabilidades críticas en la validación del backend**: la API estaba devolviendo un código `201 Created` en lugar del esperado `400 Bad Request` al recibir nombres de kit vacíos o parámetros de tipo numérico.

---

## 🛠️ Stack Tecnológico y Arquitectura

*   **Lenguaje:** Python 3
*   **Framework de Pruebas:** Pytest
*   **Peticiones HTTP:** Librería `requests`

### 📂 Estructura del Proyecto (Modularidad)
*   📄 `configuration.py`: Almacenamiento de URLs base y endpoints.
*   📄 `data.py`: Parametrización de payloads JSON y cabeceras.
*   📄 `sender_stand_request.py`: Módulo de peticiones HTTP (POST requests).
*   📄 `test_create_kit_name.py`: Runner de aserciones positivas y negativas.

---

## 💻 Muestra de Código: Aserciones y Lógica de Prueba

Para garantizar la escalabilidad del código, encapsulé las validaciones en funciones reutilizables que automatizan la comprobación de los códigos de estado devueltos por el servidor:

```python
# Extracto del diseño de aserciones negativas (Validación de Errores)
def negative_assert_400(kit_body):
    token = get_new_user_token() # Obtención dinámica del token
    response = post_new_client_kit(kit_body, token)
    
    # Aserción: El servidor DEBE rechazar la petición con un 400
    assert response.status_code == 400, (
        f"Expected 400, got {response.status_code}. Response: {response.text}"
    )

# Ejecución de caso de prueba: Tipo de parámetro incorrecto (Número en vez de String)
def test_number_type_name():
    negative_assert_400(TEST9_KIT_NUMBER_NAME)
```

---
Documentación técnica estructurada por **María Auxiliadora Vélez Mendoza** - *QA Engineer*.
