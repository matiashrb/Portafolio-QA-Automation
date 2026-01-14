import pytest
from selenium import webdriver

#config
@pytest.fixture
def driver():
    print("Abriendo navegando...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver #compartimos
    print("Cerrando navegador...")
    driver.quit()

