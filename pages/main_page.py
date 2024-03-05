from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Проверка открытия главной страницы
    # def current_main_url(self):
    #     main_url = self.domain + '/summary'
    #     assert self.get_current_url() is main_url, f"Не корректный URL, ожидается страница {main_url}, открыта {self.get_current_url()}"
    #     print("Открыта главная страница")

    #Открыть главную страницу




    #Locators

    user_name = "//input[@id = 'user-name']"
    password = "//input[@id = 'password']"
    login_button = "//input[@id = 'login-button']"
    main_word = "//span[@class='title']"

    #Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    # def autorization(self):
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.get_current_url()
    #     self.input_user_name("standard_user")
    #     self.input_password("secret_sauce")
    #     self.click_login_button()
    #     self.assert_word(self.get_main_word(), "Products")



    def logout_page(self):
        burger_menu_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-burger-menu-btn")))
        burger_menu_button.click()
        print("Click burger menu")

        logout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
        logout_button.click()
        print("Click logout button")

        autorisation_page_title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.login_logo")))
        value_autorisation_page_title = autorisation_page_title.text
        assert value_autorisation_page_title == "Swag Labs"
        print("Успешное разлогинивание!!\n ----------------------------------------------------")