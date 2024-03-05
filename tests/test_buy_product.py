from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base


def test_buy_product():
    driver = webdriver.Chrome()

    print("Start test")

    login = Base(driver)
    login.autorization(user_login="338397")
    login.change_customer(customer_id=1618616861)  #ЮЛ - 1618616861   ФЛ - 1618616855










