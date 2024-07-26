import time
import allure
from selenium.webdriver import Keys

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from utilities.logger import Logger

# класс Main_page будет потомком класса Base
class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    menu_gl = "(//a[@class='dropdown-toggle'])[7]"
    coffee_makers = "//a[@href='/catalog/category/kofevarki']"
    price = "(//div[@class='slider-handle'])[1]"
    price_max = "//input[@name='price-max']"
    apply_filters_button = "//button[@class='btn btn-primary btn-block']"
    delonghi = "//img[@alt='DELONGHI ECAM 290.31.SB']"
    select_cart_product_1 = "//a[@data-id='47996']"
    close_button = "(//button[contains(text(),'Закрыть')])[2]"

    menu_gl_2 = "(//a[@class='dropdown-toggle'])[16]"
    thermos = "//a[@href='/catalog/category/termosy']"
    manufacturer = "/html/body/div[1]/section/div/div/div[2]/div/div[2]/div/div/form/div[1]/ul/li[7]"
    sentore = "(//div[@class='product-item'])[3]"
    select_cart_product_2 = "//a[@data-id='38500']"

    appliances = "//a[@data-id='1']"
    robot_vacuum_cleaners = "//a[@data-id='435']"
    price_lef = "(//div[@class='slider-handle'])[2]"
    xiaomi_s10 = "//img[@alt='Xiaomi Robot Vacuum S10 EU']"
    select_cart_product_3 = "//a[@data-id='48043']"

    discounts = "//a[@href='/catalog/discounts']"


    # Getters

    def get_menu_gl(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_gl)))

    def get_coffee_makers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee_makers)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_apply_filters_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters_button)))

    def get_delonghi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delonghi)))

    def get_select_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart_product_1)))

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_button)))


    def get_menu_gl_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_gl_2)))

    def get_thermos(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.thermos)))

    def get_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer)))

    def get_sentore(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sentore)))

    def get_select_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart_product_2)))


    def get_appliances(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.appliances)))

    def get_robot_vacuum_cleaners(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.robot_vacuum_cleaners)))

    def get_price_lef(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_lef)))

    def get_xiaomi_s10(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi_s10)))

    def get_select_cart_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart_product_3)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_coffee_makers(self):
        self.get_coffee_makers().click()
        print("Нажимаем кнопку кофеварки")

    def input_price_max(self, price_max):
        self.get_price_max().send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        self.get_price_max().send_keys(price_max)
        print("Вводим сумму в поле максимального значения")

    def click_apply_filters_button(self):
        self.get_apply_filters_button().click()
        print("Нажимаем кнопку применить фильтр")


    def click_select_cart_product_1(self):
        self.get_select_cart_product_1().click()
        print("Нажимаем кнопку перенести в корзину")

    def click_close_button(self):
        self.get_close_button().click()
        print("Нажимаем кнопку закрыть")

    def click_thermos(self):
        self.get_thermos().click()
        print("Нажимаем термосы")

    def click_manufacturer(self):
        self.get_manufacturer().click()
        print("Ставим фильтр по производителю")

    def click_select_cart_product_2(self):
        self.get_select_cart_product_2().click()
        print("Нажимаем кнопку перенести в корзину")

    def click_appliances(self):
        self.get_appliances().click()
        print("Нажимаем кнопку бытовая техника")

    def click_robot_vacuum_cleaners(self):
        self.get_robot_vacuum_cleaners().click()
        print("Нажимаем кнопку роботы-пылесосы")

    def click_select_cart_product_3(self):
        self.get_select_cart_product_3().click()
        print("Нажимаем кнопку перенести в корзину")


    # Methods (шаги которые будем делать в методе)

    def select_product_1(self):
        with allure.step("Select Product"):
            Logger.add_start_step(method="select_product_1")
            self.get_current_url()
            self.move_to_element(self.get_menu_gl)
            self.click_coffee_makers()
            self.scroll_page(0, 1500)
            self.moving_the_slider(self.get_price(), 50, 0)
            self.input_price_max("105000")
            self.click_apply_filters_button()
            self.scroll_page(0, 700)
            self.move_to_element(self.get_delonghi)
            self.click_select_cart_product_1()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_1")

    def select_products_2(self):
        with allure.step("Select Product"):
            Logger.add_start_step(method="select_product_2")
            self.get_current_url()
            self.move_to_element(self.get_menu_gl_2)
            self.click_thermos()
            self.scroll_page(0, 1100)
            self.click_manufacturer()
            self.move_to_element(self.get_sentore)
            self.click_select_cart_product_2()
            self.click_close_button()
            self.click_appliances()
            self.click_robot_vacuum_cleaners()
            self.scroll_page(0, 1500)
            self.moving_the_slider(self.get_price(), 60, 0)
            self.moving_the_slider(self.get_price_lef(), -60, 0)
            self.click_apply_filters_button()
            self.move_to_element(self.get_xiaomi_s10)
            self.click_select_cart_product_3()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_2")

    def sel(self):
        with allure.step("Select sel"):
            Logger.add_start_step(method="sel")
            self.get(self.discounts)
            self.click_element(self.discounts)
            Logger.add_end_step(url=self.driver.current_url, method="sel")


