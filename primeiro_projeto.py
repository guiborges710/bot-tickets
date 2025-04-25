from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do Chrome com User-Agent personalizado e desativação de detecção de automação
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em segundo plano
chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU para evitar problemas
chrome_options.add_argument("--no-sandbox")  # Desativar sandbox
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Impedir detecção de automação

# Desabilitar WebDriver
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

# Inicializando o driver
print("Inicializando o driver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessando o site
url = 'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI1LTA2LTEyag0IAhIJL20vMDIycGZtcgwIAxIIL20vMGRwcmcaKRIKMjAyNS0wOS0wMmoMCAMSCC9tLzBkcHJncg0IAhIJL20vMDIycGZtQAFIAXABggELCP___________wGYAQE&hl=pt-BR&gl=BR'
print(f"Acessando o site: Google Flight (SP - LYON)")
driver.get(url)

# Esperando 6 segundos para garantir que a página carregue completamente
print("Aguardando 15 segundos para garantir que a página carregue...")
time.sleep(15)

# Tirando o print da página
image_name = input("Digite o nome da imagem (sem extensão): ")
print(f"Tirando o print da página e salvando como '{image_name}.png'...")
driver.save_screenshot(f'{image_name}.png')

# Fechar o navegador
driver.quit()
print(f"Captura de tela salva como '{image_name}.png'.")
