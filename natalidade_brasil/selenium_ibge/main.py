from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# instala e ulizaremos como serviço
service = Service(executable_path="chromedriver.exe")

# utiliza o serviço de webdrive instalado
driver = webdriver.Chrome(service=service)

# chama a url
driver.get("https://censo2022.ibge.gov.br/panorama/")

driver.implicitly_wait(2)


def selecao():
    # espera da div redenrizar
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection.select2-selection--single"))
    ).click()
    
try:
    while True:
        selecao()

        # tags li onde será extraido os arquivos
        li_elements = WebDriverWait(driver, 40).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-autocomplete-results > li:nth-child(3) > ul > li.select2-results__option"))
        )

        if not li_elements:
            break
            
        # um laço em cada tag li
        for index, li in enumerate(li_elements):
            element = WebDriverWait(driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#select2-autocomplete-results > li:nth-child(3) > ul > li.select2-results__option:nth-child({index + 1})"))
            )      
            element.click()

            #clicar em baixar para expandir qual arquivo baixar
            baixar = WebDriverWait(driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.download.desktop-only'))
            )
            baixar.click()

            # download do arquivo csv
            csv_donwload = WebDriverWait(driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "li.downloadCSV"))
            )
            csv_donwload.click()

            # recomeçar o ciclo
            selecao()

finally:
    driver.quit()
