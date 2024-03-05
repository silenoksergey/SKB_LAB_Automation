from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from pages.main_page import Main_page


def test_one_account_in_list():
    driver = webdriver.Chrome()
    base_class = Base(driver)
    main_page = Main_page(driver)


    print("Start test")
    base_class.autorization(user_login="338397")
    base_class.change_customer(customer_id=1618616861)  #ЮЛ - 1618616861   ФЛ - 1618616855
    base_class.go_to_main_page()









