from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
import json


def read_data_json():
    with open("caixa.json") as file:
        return json.load(file)


def formatter_month(month):
    return month[0].upper() + month[1:].lower()


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
    "12": "Dezembro",
}

data = read_data_json()

USERNAME = data["username"]
PASSWORD = data["password"]
SPECIFIC_MONTH = data["specific_month"]
SPECIFIC_YEAR = data["specific_year"]
TIMER = data["timer"]

MONTH = SPECIFIC_MONTH if SPECIFIC_MONTH else MONTH_MAP[str(datetime.now().month - 1)]
YEAR = SPECIFIC_YEAR if SPECIFIC_YEAR else str(datetime.now().year)

DATE_STATEMENT = f"{formatter_month(MONTH)}/{YEAR}"


def get_statement():
    driver = webdriver.Edge()

    driver.maximize_window()

    driver.get("https://internetbanking.caixa.gov.br/sinbc/#!nb/login")

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//input[@id="nomeUsuario"]').send_keys(
        USERNAME.lower()
    )

    driver.find_element(By.XPATH, '//button[@name="btnLogin"]').click()

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//button[@class="iniciaisNomeUsuario"]').click()

    driver.implicitly_wait(TIMER)

    for letter in PASSWORD:
        driver.find_element(
            By.XPATH, f'//li[contains(text(), "{letter.lower()}")]'
        ).click()

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//button[@id="btnConfirmar"]').click()

    driver.implicitly_wait(TIMER + (TIMER / 2))

    driver.find_element(By.XPATH, '//div[@data-menu-id="367"]').click()

    driver.find_element(By.LINK_TEXT, "Extrato por Período").click()

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//input[@id="rdoTipoExtratoOutro"]').click()

    driver.find_element(By.XPATH, '//div[@id="dk_container_sltOutroMes"]').click()

    driver.find_element(By.XPATH, f'//a[contains(text(), "{DATE_STATEMENT}")]').click()

    driver.find_element(By.XPATH, '//button[@id="confirma"]').click()

    driver.implicitly_wait(TIMER / 2)

    driver.find_element(By.XPATH, '//button[@id="btnImprimir"]').click()

    input('Pressione "Enter" para fechar o navegador...')

    driver.quit()


if __name__ == "__main__":
    get_statement()
