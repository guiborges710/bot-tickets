import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import re
import pywhatkit as kit
import pyautogui
import time
from datetime import datetime

async def main():
    url = "https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI1LTA1LTE1ag0IAhIJL20vMDIycGZtcgwIAxIIL20vMDZnbXIaKRIKMjAyNS0wNS0yNmoMCAMSCC9tLzA2Z21ycg0IAhIJL20vMDIycGZtQAFIAXABggELCP___________wGYAQE&hl=pt-BR&gl=BR"

    async with async_playwright() as p:
        print("🚀 Abrindo navegador...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print(f"🔍 Acessando Google Flights e pesquisando os melhores preços para SP - LYON")
        await page.goto(url)
        await page.wait_for_timeout(10000)

        content = await page.content()
        await browser.close()

        soup = BeautifulSoup(content, 'html.parser')

        # Procurar por preços em formato R$ 1.234,56
        precos = set()
        for texto in soup.stripped_strings:
            if re.search(r'R\$\s?\d{1,3}(?:\.\d{3})*(?:,\d{2})?', texto):
                precos.add(texto)

        if not precos:
            print("⚠️ Nenhum preço encontrado.")
            return

        # Converter os preços para float e ordenar
        def limpar_preco(p):
            return float(p.replace("R$", "").replace(".", "").replace(",", ".").strip())

        lista_precos = sorted(precos, key=limpar_preco)

        mais_baratos = lista_precos[:3]
        mais_caros = lista_precos[-3:]

        mensagem = "✈️ *RESULTADOS DAS PASSAGENS DE AVIÃO:*\n\n"
        mensagem += "*🔽 3 MAIS BARATOS:*\n"
        for preco in mais_baratos:
            mensagem += f"→ {preco}\n"
        mensagem += "\n*🔼 3 MAIS CAROS:*\n"
        for preco in mais_caros:
            mensagem += f"→ {preco}\n"

        mensagem += f"\nConfira os preços clicando aqui -> {url}"
        print("\n✅ Mensagem gerada para o WhatsApp:\n")
        print(mensagem)

        # Enviar mensagem via WhatsApp
        numero = "+11995401192"  # exemplo: +5511999999999

        agora = datetime.now()
        hora = agora.hour
        minuto = agora.minute + 2  # envia daqui 2 minutos

        print("\n📲 Abrindo o WhatsApp Web...")
        kit.sendwhatmsg(numero, mensagem, hora, minuto)

        # Espera abrir e pressiona ENTER para enviar
        print("⏳ Aguardando envio automático...")
        time.sleep(15)  # Aguarda o carregamento do WhatsApp
        pyautogui.press("enter")
        print("✅ Mensagem enviada com sucesso!")

# Executa
asyncio.run(main())
