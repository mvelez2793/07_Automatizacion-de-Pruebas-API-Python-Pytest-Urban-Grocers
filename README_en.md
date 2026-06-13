<div align="right">
  🌍 <a href="README.md">Español</a> | <strong>English</strong>
</div>

# ⚙️ API Test Automation (Python + Pytest): Urban Grocers

#### 📌 Project Summary (STAR Methodology)
*   **Situation:** The QA team at Urban Grocers needed to optimize backend regression testing time. It was necessary to automate the validation of the `name` field in the product kit creation endpoint (`/api/v1/kits`), ensuring the server correctly handled length restrictions and data types.
*   **Task:** Design, code, and execute an automated testing framework from scratch using Python, integrating a modular design to cleanly separate data, configurations, and test logic (Test Runner).
*   **Action:**
    *   Developed an automated testing environment using the **Pytest** framework and the **Requests** library for HTTP requests.
    *   Automated the generation of preconditions (user creation and dynamic `authToken` retrieval) through auxiliary functions.
    *   Implemented 9 test cases based on **Boundary Value Analysis (BVA)**, stressing the system with extreme lengths (1, 511, and 512 characters), empty strings, special characters, and invalid data types (numbers).
    *   Designed both positive assertions (validating HTTP 201 codes) and negative assertions (validating HTTP 400 codes).
*   **Result:** The automated suite was successfully executed, allowing the isolation and reporting of **critical backend validation vulnerabilities**: the API was returning a 201 Created code instead of the expected 400 Bad Request when receiving empty kit names or numeric-type parameters.

---

#### 🛠️ Tech Stack and Architecture
*   **Language:** Python 3
*   **Testing Framework:** Pytest
*   **HTTP Requests:** `requests` library

##### 📂 Project Structure (Modularity)
*   📄 `configuration.py`: Storage for base URLs and endpoints.
*   📄 `data.py`: Parameterization of JSON payloads and headers.
*   📄 `sender_stand_request.py`: HTTP requests module (POST requests).
*   📄 `test_create_kit_name.py`: Runner for positive and negative assertions.

---

#### 💻 Code Sample: Assertions and Test Logic
To ensure code scalability, I encapsulated the validations in reusable functions that automate the checking of the HTTP status codes returned by the server:

```python
# Extract of negative assertion design (Error Validation)
def negative_assert_400(kit_body):
    token = get_new_user_token() # Obtención dinámica del token
    response = post_new_client_kit(kit_body, token)
    
    # Assertion: The server MUST reject the request with a 400 status code
    assert response.status_code == 400, (
        f"Expected 400, got {response.status_code}. Response: {response.text}"
    )
# Test case execution: Incorrect parameter type (Number instead of String)
def test_number_type_name():
    negative_assert_400(TEST9_KIT_NUMBER_NAME)
```
---
Technical documentation structured by **María Auxiliadora Vélez Mendoza** - *QA Engineer*.

