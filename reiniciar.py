import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Carrega as variáveis do arquivo .env se ele existir localmente
load_dotenv()

# Recupera credenciais das variáveis de ambiente
ROUTER_USER = os.getenv("ROUTER_USER", "CLARO_34A9CE")  # valor padrão de fallback se não definido
ROUTER_PASS = os.getenv("ROUTER_PASS")

if not ROUTER_PASS:
    raise ValueError("A senha do roteador não foi configurada nas variáveis de ambiente.")

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--ignore-ssl-errors=yes")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("http://192.168.0.1")

    try:
        details_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, "details-button"))
        )
        details_btn.click()
        
        proceed_link = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, "proceed-link"))
        )
        proceed_link.click()
    except Exception:
        pass

    # 2. Login usando as variáveis
    user_input = wait.until(EC.element_to_be_clickable((By.ID, "Frm_Username")))
    user_input.clear()
    user_input.send_keys(ROUTER_USER)

    pass_input = driver.find_element(By.ID, "Frm_Password")
    pass_input.clear()
    pass_input.send_keys(ROUTER_PASS)

    login_btn = driver.find_element(By.ID, "LoginId")
    login_btn.click()

    # 3. Navegação
    advanced_btn = wait.until(EC.element_to_be_clickable((By.ID, "Qstate")))
    advanced_btn.click()

    menu_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.main-menu-button")))
    menu_btn.click()

    mgmt_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='menu-mgrAndDiag']")))
    mgmt_btn.click()

    reboot_menu_item = wait.until(EC.element_to_be_clickable((By.ID, "reboot")))
    reboot_menu_item.click()

    # 4. Confirmação do Reboot
    reboot_btn = wait.until(EC.element_to_be_clickable((By.ID, "Btn_restart")))
    reboot_btn.click()

    confirm_ok_btn = wait.until(EC.element_to_be_clickable((By.ID, "confirmOK")))
    confirm_ok_btn.click()

    time.sleep(2)

finally:
    driver.quit()