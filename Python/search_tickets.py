import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import re
from datetime import datetime
from twilio.rest import Client
import os

async def main():
    url = "https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI1LTA1LTE1ag0IAhIJL20vMDIycGZtcgwIAxIIL20vMDZnbXIaKRIKMjAyNS0wNS0yNmoMCAMSCC9tLzA2Z21ycg0IAhIJL20vMDIycGZtQAFIAXABggELCP___________wGYAQE&hl=pt-BR&gl=BR"

    async with async_playwright() as p:
        print("🚀 Abrindo navegador...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("🔍 Buscando preços...")
        await page.goto(url)
        await page.wait_for_timeout(10000)
        content = await page.content()
        await browser.close()

        soup = BeautifulSoup(content, 'html.parser')
        precos = set()
        for texto in soup.stripped_strings:
            if re.search(r'R\$\s?\d{1,3}(?:\.\d{3})*(?:,\d{2})?', texto):
                precos.add(texto)

        if not precos:
            print("⚠️ Nenhum preço encontrado.")
            return

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

        print("\n✅ Mensagem gerada:")
        print(mensagem)

        # ENVIO VIA TWILIO (WhatsApp)
        account_sid = "ACaeb3fd941aede827b7f0e8ca5cc5c196"
        auth_token = "c6407c55d4e1fca58235f861a551b7f6"
        client = Client(account_sid, auth_token)

        from_whatsapp = 'whatsapp:+14155238886'  # Twilio sandbox sender
        to_whatsapp = 'whatsapp:+5511995401192'  # Substitua com seu número verificado

        print("📲 Enviando via WhatsApp (Twilio)...")
        message = client.messages.create(
            from_=from_whatsapp,
            body=mensagem,
            to=to_whatsapp
        )

        print(f"✅ Mensagem enviada com sucesso! SID: {message.sid}")

# Executa
asyncio.run(main())
