from supabase import create_client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")


def enviar_mensagem(telefone, mensagem):
    url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    print("Enviado para", telefone, "Status:", response.status_code)


dados = supabase.table("contatos").select("*").limit(3).execute()

for contato in dados.data:

    nome = contato["nome"]
    telefone = contato["telefone"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    enviar_mensagem(telefone, mensagem)