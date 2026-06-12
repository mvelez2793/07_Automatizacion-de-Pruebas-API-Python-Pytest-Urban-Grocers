# ⚙️ Automatización de Pruebas de API: Urban Grocers

![Project](https://img.shields.io/badge/Project-API_Test_Automation-blue) ![Language](https://img.shields.io/badge/Language-Python_3.1-yellow) ![Framework](https://img.shields.io/badge/Framework-Pytest-green) ![Library](https://img.shields.io/badge/Library-Requests-lightgray)

## 📌 Descripción del Proyecto
Este proyecto contiene una suite de pruebas automatizadas para validar la lógica del backend de la aplicación **Urban Grocers**. Específicamente, automatiza las pruebas de validación (Negative y Positive Testing) para el campo `name` en el endpoint de creación de kits de productos (`/api/v1/kits`), siguiendo las especificaciones del equipo de QA.

Las pruebas verificaran de forma automatizada:
*   Manejo correcto de códigos de estado HTTP (201 Created vs 400 Bad Request).
*   Validación de límites de caracteres (Análisis de Valores Límite).
*   Soporte de caracteres especiales y tipos de datos en payloads JSON.
*   Gestión de errores y campos obligatorios omitidos.

---

## 🛠️ Tecnologías y Arquitectura del Proyecto

El framework fue diseñado bajo principios de modularidad para asegurar su mantenibilidad y escalabilidad, utilizando las siguientes herramientas:

*   **Python 3.1:** Lenguaje base.
*   **Pytest:** Framework principal de aserciones y ejecución de pruebas.
*   **Requests:** Librería para la intercepción y envío de peticiones HTTP.
*   **apiDoc:** Documentación de referencia para los endpoints.

### 📂 Estructura de Archivos
El código está separado lógicamente para no mezclar configuraciones con casos de prueba:
*   📄 `configuration.py`: Almacena la URL base del servidor y las rutas de los endpoints.
*   📄 `data.py`: Contiene las cabeceras (headers) y parametrización de los cuerpos de solicitud (payloads JSON).
*   📄 `sender_stand_request.py`: Módulo que encapsula las peticiones HTTP (POST) y la generación dinámica de tokens de autenticación (`authToken`).
*   📄 `test_create_kit_name.py`: Runner principal de Pytest que contiene las aserciones positivas y negativas.

---

## 🧪 Cobertura de Pruebas y Resultados (Bugs Detectados)

Se implementaron 9 casos de prueba basados en partición de equivalencia. Durante la ejecución automatizada, **se descubrieron vulnerabilidades críticas en el backend (Bugs)** donde el servidor devolvía respuestas exitosas ante datos inválidos.

| # | Descripción del Escenario (Campo `name`) | Código Esperado | Código Obtenido | Estado / Resultado |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Límite inferior permitido (1 carácter). | `201` | `201` | ✅ PASSED |
| **2** | Límite superior permitido (511 caracteres). | `201` | `201` | ✅ PASSED |
| **3** | Límite inferior no permitido (0 caracteres / Vacío). | `400` | `201` | ❌ **FAILED (BUG)** |
| **4** | Límite superior no permitido (512 caracteres). | `400` | `400` | ✅ PASSED |
| **5** | Uso de caracteres especiales (`№%@`). | `201` | `201` | ✅ PASSED |
| **6** | Uso de espacios en blanco. | `201` | `201` | ✅ PASSED |
| **7** | Uso de números en formato string (`"123"`). | `201` | `201` | ✅ PASSED |
| **8** | El parámetro no se envía en la solicitud. | `400` | `400` | ✅ PASSED |
| **9** | Tipo de dato inválido (Número entero en vez de String). | `400` | `201` | ❌ **FAILED (BUG)** |

> ⚠️ **Nota sobre los Bugs:** Los casos 3 y 9 fallan en la ejecución de Pytest debido a que la API de Urban Grocers acepta nombres vacíos y números enteros, devolviendo un código `201` cuando la documentación exige que sea rechazado con un `400 Bad Request`.

---

## 🚀 Instrucciones de Ejecución

### Precondiciones
1. Contar con Git y Python 3 instalados en el entorno local.
2. Iniciar el servidor de Urban Grocers y actualizar la variable `BASE_URL` en el archivo `configuration.py`.

### Comandos de Consola
Para ejecutar la suite completa de pruebas y visualizar el reporte detallado:
```bash
pytest test_create_kit_name.py -v
```

Para ejecutar una prueba específica (ejemplo, la prueba de 1 carácter):
```bash
pytest test_create_kit_name.py::test_1_char_kit -v
```

---
Documentación técnica estructurada por **María Auxiliadora Vélez Mendoza** - *QA Engineer*.


