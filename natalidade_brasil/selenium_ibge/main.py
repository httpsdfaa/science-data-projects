from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#instalar webdrive correto
from webdriver_manager.chrome import ChromeDriverManager

# instala e ulizaremos como serviço
service = Service(ChromeDriverManager().install())

# utiliza o serviço de webdrive instalado
driver = webdriver.Chrome(service=service)

# chama a url
driver.get("https://censo2022.ibge.gov.br/panorama/")

driver.implicitly_wait(0.8)

try:
    # espera da div redenrizar
    elemento = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection.select2-selection--single"))
    )

    elemento.click()
    
    # espera da div redenrizar
    elemento_render = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-results__option"))
    )

    print(elemento_render.text)
finally:
    driver.quit()


driver.quit()