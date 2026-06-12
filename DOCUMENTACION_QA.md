# 📂 Documentación Técnica: Automatización API (Urban Grocers)

Este documento expone los hallazgos técnicos, el alcance de la cobertura y los defectos descubiertos durante la ejecución de la suite automatizada de pruebas API para la creación de kits de productos.

## 🧠 Estrategia de Automatización (Equivalence Partitioning)
La automatización se centró en someter el payload JSON del endpoint `POST /api/v1/kits` a pruebas exhaustivas de límites (BVA). La suite consta de 9 escenarios ejecutados a través de Pytest:

| ID | Objetivo de Prueba (Campo `name`) | Código HTTP Esperado |
| :--- | :--- | :--- |
| **Test 1** | Límite inferior válido (1 carácter). | `201 Created` |
| **Test 2** | Límite superior válido (511 caracteres). | `201 Created` |
| **Test 3** | Límite inferior inválido (0 caracteres / Vacío). | `400 Bad Request` |
| **Test 4** | Límite superior inválido (512 caracteres). | `400 Bad Request` |
| **Test 5** | Soporte de caracteres especiales (`№%@`). | `201 Created` |
| **Test 6** | Soporte de espacios en blanco. | `201 Created` |
| **Test 7** | Soporte de formato string con números (`"123"`). | `201 Created` |
| **Test 8** | Omisión del parámetro (Payload sin `name`). | `400 Bad Request` |
| **Test 9** | Tipo de dato inválido (Número entero en lugar de String). | `400 Bad Request` |

---

## 🐛 Reporte de Errores Detectados por Pytest (Bugs)

Durante la ejecución del comando `pytest test_create_kit_name.py -v` en la terminal, el framework automatizado identificó vulnerabilidades severas en las validaciones del servidor. 

### 🔴 Defecto 1: Ausencia de Validación de Longitud Mínima
*   **Caso Automatizado:** `test_empty_name_kit()`
*   **Payload Enviado:**
    ```json
    { "name": "" }
    ```
*   **Resultado Esperado:** Falla controlada del servidor con código `400 Bad Request`.
*   **Resultado Obtenido (BUG):** El servidor devuelve un `201 Created`, aceptando la creación de kits con nombres vacíos, lo cual viola la restricción de negocio.

### 🔴 Defecto 2: Fallo en Validación de Tipos de Datos (Data Type Validation)
*   **Caso Automatizado:** `test_number_type_name()`
*   **Payload Enviado:**
    ```json
    { "name": 123 }
    ```
*   **Resultado Esperado:** Falla controlada por incompatibilidad de tipos (`400 Bad Request`).
*   **Resultado Obtenido (BUG):** El servidor devuelve un `201 Created`. El backend no está aplicando un casteo estricto o validación de tipo, exponiendo la base de datos a posibles inconsistencias estructurales.

---

> ⚠️ **Nota de QA:** Estos defectos ocasionaron fallos (`FAILED`) en la terminal de Pytest, cumpliendo el objetivo principal de la automatización: descubrir regresiones y fallos lógicos antes de su despliegue a entornos superiores.

---
Documentación técnica estructurada por **María Auxiliadora Vélez Mendoza** - *QA Engineer*.
