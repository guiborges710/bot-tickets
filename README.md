# ✈️ Bot de Monitoramento de Passagens Aéreas

Este projeto é um **bot automatizado** que busca os preços de passagens no Google Flights e envia os resultados diretamente para o **WhatsApp**, utilizando o **Playwright**, **BeautifulSoup** e a API da **Twilio**. Ideal para acompanhar quedas de preços em tempo real e ser notificado com praticidade!

---

## 📸 Visão Geral

> 🔍 O bot acessa o Google Flights, simula a navegação, extrai os preços em reais (R$), ordena e envia um resumo com:
- Os **3 preços mais baratos**
- Os **3 preços mais caros**
- Link para consulta completa

---

## ⚙️ Tecnologias Utilizadas

- 🔸 [Playwright](https://playwright.dev/) – Para automação de navegador headless
- 🍜 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – Para parsing HTML
- ☁️ [Twilio API](https://www.twilio.com/whatsapp) – Para envio via WhatsApp
- 🐍 Python 3.10+

---

## 🚀 Como usar localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/tickets-bot-final.git
cd tickets-bot-final
```

### 2. Instale as dependências:

```bash
pip install -r requirements.txt
playwright install
```

### 3. Configure suas variáveis de ambiente:

Crie um arquivo `.env` ou defina no sistema:

```bash
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_token
```

Você também precisa estar conectado ao sandbox do WhatsApp Twilio.

---

## 🧪 Executando o Bot

```bash
python search_tickets.py
```

O bot vai:
1. Acessar o link do Google Flights
2. Aguardar o carregamento
3. Extrair os preços
4. Montar a mensagem
5. Enviar via WhatsApp ✅

---

## 🤝 Exemplo de saída no WhatsApp

```
✈️ RESULTADOS DAS PASSAGENS DE AVIÃO:

🔽 3 MAIS BARATOS:
→ R$ 4.533
→ R$ 5.004
→ R$ 5.145

🔼 3 MAIS CAROS:
→ R$ 6.339
→ R$ 6.380
→ R$ 6.502

Confira os preços clicando aqui -> [link do Google Flights]
```

---

## 📦 Roadmap futuro

- [ ] Envio programado com Render (cron job)
- [ ] Suporte para múltiplos destinos
- [ ] Histórico de preços (JSON ou banco de dados)
- [ ] Integração com Telegram Bot 📬

---

## 📬 Contato

Se tiver dúvidas, sugestões ou quiser colaborar, fique à vontade para abrir uma issue ou mandar uma mensagem!  
Feito com 💙 por [@guiborges710](https://github.com/guiborges710)
