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

        #Тело запроса login
        data_login = {
            "bank": "DELO",
            "login": user_login,
            "osType": "WEB",
            "password": "1234"

        }

        #Тело запроса auth
        data_auth = {
            "auth_code": "1234"
        }

        #Метод login
        login = self.session.post(link_login_page, headers=self.headers, data=data_login)
        assert login.status_code == 200, f'Метод login вернул {login.json()}'

        #Метод auth
        auth = self.session.post(link_auth_page, headers=self.headers, data=data_auth)
        assert auth.status_code == 200, f'Метод auth вернул {auth.json()}'
        print("Успешная авторизация")


    #Переходим к ЮЛ или ФЛ, в зависимости от переданного в метод customer_id клиента
    def change_customer(self, customer_id=int):

        link_change_customer = self.domain + "/json/change/customer"

        data_chage_customer = {
            "customerId": customer_id,
            "setAsDefaultCustomer": True
        }

        change_customer = self.session.post(link_change_customer, headers=self.headers, data=data_chage_customer)
        response_change_customer = change_customer.json()
        if change_customer.status_code == 200:
            print('Переход к указанному пользователю')
        else:
            assert response_change_customer[0]['code'] == 'CUSTOMER_NOT_CHANGE', f'Не удалось сменить пользователя с помощью метода change/customer: {change_customer}{response_change_customer}'
            print('Переход к указанному пользователю')





