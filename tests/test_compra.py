import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")

    #LOGIN
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    print("\n⏳ Esperando que cargue el inventario...")
    time.sleep(3) #3 segundos de espera

    print(f"📍 URL Actual: {driver.current_url}")

    #VALIDACION
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in titulo, "Fallo el login, no estamos en el inventario"
    print("Login exitoso, prueba superada!")
