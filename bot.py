import os
import requests
import sys

# --- CONFIGURAÇÕES ---
# Pega as senhas do ambiente (segurança máxima)
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Se não tiver as senhas, o bot nem tenta rodar
if not TOKEN or not CHAT_ID:
    print("ERRO CRÍTICO: Variáveis TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não encontradas!")
    sys.exit(1)

# Pega o tipo de mensagem que o GitHub mandou (entrada, almoco_ida, etc)
# Se não vier nada, assume "geral"
tipo = sys.argv[1] if len(sys.argv) > 1 else "geral"

def enviar_mensagem():
    # --- DICIONÁRIO DE MENSAGENS ---
    if tipo == "entrada":
        msg = "☀️ *Bom dia, Time SuperBid!* \n\n☕ Já bateu o ponto de entrada? Bora codar que o backlog não espera!"
    
    elif tipo == "almoco_ida":
        msg = "🍽️ *Hora do Almoço!* \n\n😋 Pausa pro rango! Não esquece de bater o ponto antes de sair. Bom apetite!"
    
    elif tipo == "almoco_volta":
        msg = "🔙 *De volta ao trabalho!* \n\n🔋 Baterias recarregadas? Bate o ponto da volta e bora resolver esses tickets!"
    
    elif tipo == "saida":
        msg = "🌙 *Fim de expediente!* \n\n🛑 Larga o VS Code, bate o ponto de saída e vai viver! Até amanhã."
    
    else:
        msg = "⚠️ *Lembrete de Ponto!* \nPassando pra lembrar de conferir seus registros hoje."

    # --- ENVIO PRO TELEGRAM ---
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown" # Permite usar negrito com asteriscos
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # Para o script se der erro 400 ou 500
        print(f"✅ Sucesso! Mensagem de '{tipo}' enviada.")
    except Exception as e:
        print(f"❌ Deu ruim ao enviar: {e}")
        sys.exit(1)

if __name__ == "__main__":
    enviar_mensagem()