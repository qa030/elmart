import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс Main_page будет потомком класса Base
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    cart_button = "//a[@class='btn btn-primary']"
    test_word_1 = "//a[@href='/catalog/product/delonghi-ecam-290.31.sb']"
    test_word_2 = "//a[@href='/catalog/product/sentore-hc-450-grey']"
    test_word_3 = "//a[@href='/catalog/product/xiaomi-robot-vacuum-s10-eu']"


    # Getters

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_test_word_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word_1)))

    def get_test_word_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word_2)))

    def get_test_word_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word_3)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Нажимаем кнопку перейти в корзину")


    # Methods (шаги которые будем делать в методе)

    def product_confirmation(self):
        with allure.step("Product Confirmation 1"):
            self.get_current_url()
            self.click_cart_button()
            self.assert_word(self.get_test_word_1(), "DELONGHI ECAM 290.31.SB")



    def product_confirmation_2(self):
        with allure.step("Product Confirmation 2"):
            self.click_cart_button()
            self.assert_word(self.get_test_word_2(), "SENTORE HC-450 Grey")
            self.assert_word(self.get_test_word_3(), "Xiaomi Robot Vacuum S10 EU")



