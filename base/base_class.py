import fake_useragent
import requests, json


class Base():
    def __init__(self, driver):
        self.driver = driver

    #Стенд
    domain = "https://delo-prod.skblab.ru"

    #Сессия
    session = requests.Session()

    #User-agent
    user = fake_useragent.UserAgent().random
    headers = {
        'User-Agent': user
    }

    #Получение текущего URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL is: " + get_url)


    #Проверка текста
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    #Авторизация
    def autorization(self, user_login):

        link_login_page = self.domain + "/json/login"
        link_auth_page = self.domain + "/json/auth"

        data_login = {
            "bank": "DELO",
            "login": user_login,
            "osType": "WEB",
            "password": "1234"

        }

        data_auth = {
            "auth_code": "1234"
        }
        #Метод login
        login = self.session.post(link_login_page, headers=self.headers, data=data_login)
        assert login.status_code == 200
        print("Login successful")

        #Метод auth
        auth = self.session.post(link_auth_page, headers=self.headers, data=data_auth)
        assert auth.status_code == 200
        print("Autorization successful")



    # Сменить пользователя ЮЛ/ФЛ, смотря какой customer_id передан в метод
    def change_customer(self, customer_id=int):

        link_change_customer = self.domain + "/json/change/customer"

        data_chage_customer = {
            "customerId": customer_id,
            "setAsDefaultCustomer": True
        }

        change_customer = self.session.post(link_change_customer, headers=self.headers, data=data_chage_customer).text





