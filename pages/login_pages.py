from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


from utilities.logger import Logger


class Login_page(Base):

    url = 'https://elmart-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_registration_button = "//a[@href='https://elmart-shop.ru/login']"
    email_login = "//input[@id='login-email']"
    password = "//input[@id='login-pass']"
    login_button = "//button[@class='le-button huge']"
    main_word = "//a[contains(text(), 'Личный кабинет')]"


    # Getters

    def get_login_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_registration_button)))

    def get_email_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_login_registration_button(self):
        self.get_login_registration_button().click()
        print("Нажимаем на кнопку Войти в аккаунт")

    def input_email_login(self, email_login):
        self.get_email_login().send_keys(email_login)
        print("Вводим эл.почту")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Вводим пароль")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажимаем кнопку Войти")


    # Methods (шаги которые будем делать в методе)

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_registration_button()
            self.input_email_login("karpov.sti@bk.ru")
            self.input_password("Test808")
            self.click_login_button()
            self.assert_word(self.get_main_word(), "Личный кабинет")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
