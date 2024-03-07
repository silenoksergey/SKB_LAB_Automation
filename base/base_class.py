import fake_useragent
import requests, json, pickle, time
from pip._internal.network import session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class Base():

    def __init__(self, driver):
        self.driver = driver
        options = Options()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36')
        options.add_argument('contant-type=application/json')
        options.add_argument('accept=application/json, text/plain, */*')
        options.add_argument('accept-encoding=gzip, deflate, br')
        options.add_argument('connection=keep-alive')
        options.add_argument('Accept-Language=ru,en;q=0.9')
        options.add_argument('authority=delo-prod.skblab.ru')
        options.add_argument('scheme=https')
        options.add_argument('Referer=https://delo-prod.skblab')
        options.add_argument('Sec-Ch-Ua-Platform=Windows')
        options.add_argument('Sec-Fetch-Dest=empty')
        options.add_argument('Sec-Fetch-Mode=cors')
        options.add_argument('Sec-Fetch-Site=same-origin')


    #Стенд
    domain = "https://delo-prod.skblab.ru"

    #Сессия
    session = requests.Session()

    # #User agent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}



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
        login = self.session.post(link_login_page, headers=self.headers,  data=data_login)
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




    #Получение текущего URL
    def get_current_url(self):
        return self.driver.current_url


    #Переход на главную страницу
    def go_to_main_page(self):

        self.driver.get(self.domain)
        self.driver.delete_all_cookies()
        cookies = self.session.cookies

        for cookie in cookies:
            self.driver.add_cookie({"name": cookie.name, "value": cookie.value, "domain": cookie.domain,
                                    "path": cookie.path, "secure": cookie.secure, "expires": cookie.expires})




        self.driver.get(self.domain + "/summary")

        driver_cookies = self.driver.get_cookies()
        print(driver_cookies)
        time.sleep(10)




        # assert self.get_current_url() is main_url, f"Не корректный URL, ожидается страница {main_url}, открыта {self.get_current_url()}"
        # print("Открыта главная страница")




    #Проверка текста
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


