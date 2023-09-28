from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from month_map import MONTH_MAP
import time
import json


def read_data_json():
    with open("caixa.json") as file:
        return json.load(file)


def formatter_month(month):
    return month[0].upper() + month[1:].lower()


data = read_data_json()

USERNAME = data["username"]
PASSWORD = data["password"]
SPECIFIC_MONTH = data["specific_month"]
SPECIFIC_YEAR = data["specific_year"]
WAIT_TIME = data["wait_time"]
MAX_RETRIES = data["max_retries"]

MONTH = SPECIFIC_MONTH if SPECIFIC_MONTH else MONTH_MAP[str(datetime.now().month - 1)]
YEAR = SPECIFIC_YEAR if SPECIFIC_YEAR else str(datetime.now().year)
DATE_STATEMENT = f"{formatter_month(MONTH)}/{YEAR}"

URL_CAIXA = "https://internetbanking.caixa.gov.br/sinbc/#!nb/login"


def find_element_with_retry(
    driver, by, value, max_retries=MAX_RETRIES, wait_time=WAIT_TIME
):
    retries = 0
    while retries < max_retries:
        try:
            element = driver.find_element(by, value)
            wait = WebDriverWait(driver, wait_time)
            wait.until(lambda d: element.is_displayed())
            return element

        except NoSuchElementException:
            print(
                f'Elemento "{value}" não encontrado, tentando novamente ({retries+1}/{max_retries})...'
            )
            retries += 1
            time.sleep(wait_time)
    raise NoSuchElementException(
        f'Elemento "{value}" não encontrado após {max_retries} tentativas. O script foi encerrado.'
    )


def get_statement():
    try:
        driver = webdriver.Edge()

        driver.maximize_window()

        driver.get(URL_CAIXA)

        input_user = find_element_with_retry(
            driver, By.XPATH, '//input[@id="nomeUsuario"]'
        )
        input_user.send_keys(USERNAME.lower())

        btn_continue = find_element_with_retry(
            driver, By.XPATH, '//button[@name="btnLogin"]'
        )
        btn_continue.click()

        btn_initial_letters = find_element_with_retry(
            driver, By.XPATH, '//button[@id="lnkInitials"]'
        )
        btn_initial_letters.click()

        for letter in PASSWORD:
            li_letter = find_element_with_retry(
                driver, By.XPATH, f'//li[contains(text(), "{letter.lower()}")]'
            )
            li_letter.click()

        btn_confirma_password = find_element_with_retry(
            driver, By.XPATH, '//button[@id="btnConfirmar"]'
        )
        btn_confirma_password.click()

        btn_my_account = find_element_with_retry(
            driver, By.XPATH, '//*[@id="categoriaContainer"]/div/p'
        )
        btn_my_account.click()

        a_per_period = find_element_with_retry(
            driver, By.LINK_TEXT, "Extrato por Período"
        )
        a_per_period.click()

        radio_other_month = find_element_with_retry(
            driver, By.XPATH, '//input[@id="rdoTipoExtratoOutro"]'
        )
        radio_other_month.click()

        select_month = find_element_with_retry(
            driver, By.XPATH, '//div[@id="dk_container_sltOutroMes"]'
        )
        select_month.click()

        option_month = find_element_with_retry(
            driver, By.XPATH, f'//a[contains(text(), "{DATE_STATEMENT}")]'
        )
        option_month.click()

        btn_continue = find_element_with_retry(
            driver, By.XPATH, '//button[@id="confirma"]'
        ).click()

        btn_print_out = find_element_with_retry(
            driver, By.XPATH, '//button[@id="btnImprimir"]'
        )
        btn_print_out.click()

        input('Pressione "Enter" para fechar o navegador...')

    except NoSuchElementException as e:
        print(e)

    finally:
        driver.quit()


if __name__ == "__main__":
    get_statement()
