from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from datetime import datetime

SPECIFIC_MONTH = None
SPECIFIC_YEAR = None

MONTH_MAP = {
    "1": "Janeiro",
    "2": "Fevereiro",
    "3": "Março",
    "4": "Abril",
    "5": "Maio",
    "6": "Junho",
    "7": "Julho",
    "8": "Agosto",
    "9": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

current_month = SPECIFIC_MONTH if SPECIFIC_MONTH else MONTH_MAP[str(datetime.now().month - 1)]
current_year = SPECIFIC_YEAR if SPECIFIC_YEAR else str(datetime.now().year)

def formatter_month(month):
    return month[0].upper() + month[1:].lower()

date_statement =  f'{formatter_month(current_month)}/{current_year}'

def get_statement():

    TIMER = 5

    driver = webdriver.Edge()

    driver.maximize_window()

    driver.get("https://internetbanking.caixa.gov.br/sinbc/#!nb/login")

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//input[@id="nomeUsuario"]').send_keys(USERNAME.lower())

    driver.find_element(By.XPATH, '//button[@name="btnLogin"]').click()

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//button[@class="iniciaisNomeUsuario"]').click()

    driver.implicitly_wait(TIMER)

    for letter in PASSWORD:
        driver.find_element(By.XPATH, f'//li[contains(text(), "{letter.lower()}")]').click()

    driver.find_element(By.XPATH, '//button[@id="btnConfirmar"]').click()
    
    driver.implicitly_wait(TIMER * 2)

    input('Pressione "Enter" para fechar o navegador...')

    driver.quit()


if __name__ == "__main__":
    get_statement()
    ...