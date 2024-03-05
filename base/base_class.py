import fake_useragent
import requests, json, pickle, time
from pip._internal.network import session
from selenium import webdriver

class Base():

    def __init__(self, driver):
        self.driver = driver

    #Стенд
    domain = "https://delo-prod.skblab.ru"

    #Сессия
    session = requests.Session()

    #Headers до авторизации
    user = fake_useragent.UserAgent().random
    headers = {
        'User-Agent': user
    }
    #Куки после авторизации
    auth_cookies = {}





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

        # #Метод login
        login = self.session.post(link_login_page, headers=self.headers, data=data_login)
        assert login.status_code == 200, f'Метод login вернул {login.json()}'


        #Метод auth
        auth = self.session.post(link_auth_page, headers=self.headers, data=data_auth)
        assert auth.status_code == 200, f'Метод auth вернул {auth.json()}'
        print("Успешная авторизация")

        cookies = self.session.cookies.get_dict()
        self.auth_cookies = cookies
        print(self.auth_cookies)



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




    #Получение текущего URL
    def get_current_url(self):
        return self.driver.current_url

    def go_to_main_page(self):

        self.driver.get(self.domain + '/summary')
        self.driver.add_cookie({'name': 'foo', 'value': 'bar'})
        self.driver.delete_all_cookies()
        self.driver.add_cookie(self.auth_cookies)
        self.driver.refresh()


        time.sleep(5)


        # main_url = self.domain + '/summary'
        # self.session.get(main_url)

        # assert self.get_current_url() is main_url, f"Не корректный URL, ожидается страница {main_url}, открыта {self.get_current_url()}"
        # print("Открыта главная страница")



    #Проверка текста
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


