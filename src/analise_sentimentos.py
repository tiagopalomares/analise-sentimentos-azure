from azure.ai.textanalytics import TextAnalyticsClient # type: ignore
from azure.core.credentials import AzureKeyCredential # type: ignore
import os
from dotenv import load_dotenv # type: ignore

# Carregar as variáveis do arquivo .env
load_dotenv()

# Pegar as variáveis de ambiente
API_KEY = os.getenv("AZURE_API_KEY")
ENDPOINT = os.getenv("AZURE_ENDPOINT")

def autenticar_cliente():
    return TextAnalyticsClient(endpoint=ENDPOINT, credential=AzureKeyCredential(API_KEY))

cliente = autenticar_cliente()

# Lendo frases do arquivo
with open("./inputs/frases.txt", "r", encoding="utf-8") as arquivo:
    frases = [linha.strip() for linha in arquivo.readlines()]

# Enviar frases para análise
resposta = cliente.analyze_sentiment(documents=frases)

# Exibir resultados
for i, doc in enumerate(resposta):
    print(f"Frase: {frases[i]}")
    print(f"Sentimento: {doc.sentiment} (Positivo: {doc.confidence_scores.positive: .2f}," 
          f"Neutro: {doc.confidence_scores.neutral: .2f}, Negativo: {doc.confidence_scores.negative: .2f}")
    print("-" * 50)

    