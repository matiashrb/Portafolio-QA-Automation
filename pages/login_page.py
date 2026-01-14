from selenium.webdriver.common.by import By

class LoginPage:
    #constructor
    def __init__(self, driver):
        self.driver = driver

        #locators
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    #metodos
    def login(self, usuario, password):
        self.driver.find_element(*self.username_input).send_keys(usuario) #le mandamos el usuario
        self.driver.find_element(*self.password_input).send_keys(password) #le mandamos el password
        self.driver.find_element(*self.login_btn).click() #apretamos el boton de enviar
        

