# 🧪 QA Automation Framework - Portafolio

Este proyecto es un framework de pruebas automatizadas para el sitio E-commerce [SauceDemo](https://www.saucedemo.com/), demostrando habilidades en **Frontend Automation**.

## 🚀 Tecnologías Usadas
* **Python** (Lenguaje principal)
* **Selenium WebDriver** (Interacción con navegador)
* **PyTest** (Runner de pruebas y aserciones)
* **Page Object Model (POM)** (Patrón de diseño para escalabilidad)

## 📂 Estructura del Proyecto
* `pages/`: Contiene los Page Objects (Locators y Acciones).
* `tests/`: Contiene los scripts de prueba.
* `conftest.py`: Configuraciones globales (Fixtures del Driver).

## ⚙️ Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/Portafolio-QA-Automation.git](https://github.com/TU_USUARIO/Portafolio-QA-Automation.git)

2. **Crear entorno virtual:**
    Bash

    python -m venv venv
    .\venv\Scripts\activate

3. **Instalar dependencias:**
    pip install -r requirements.txt

4. **Ejecutar los tests:**
    pytest tests/test_compra.py -v -s
