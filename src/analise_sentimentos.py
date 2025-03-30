from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os 
endpoint = os.getenv("AZURE_ENDPOINT") 
api_key = os.getenv("AZuRE_API_KEY")

# Configuração do Azure
API_KEY = "jIv1xxciIorBWK7uEhxabt7cwdjJiLgXIk57ZI7BLgTkAUjmtcAGJQQJ99BCACYeBjFXJ3w3AAAaACOGKEne"
ENDPOINT = "https://languageidiomadiolab.cognitiveservices.azure.com/"

def autenticar_cliente():
    return TextAnalyticsClient(endpoint=ENDPOINT, credential=AzureKeyCredential(API_KEY))

cliente = autenticar_cliente()

# Lendo frases do arquivo
with open("../inputs/frases.txt", "r", encoding="utf-8") as arquivo:
    frases = [linha.strip() for linha in arquivo.readlines()]

# Enviar frases para análise
resposta = cliente.analyze_sentiment(documents=frases)

# Exibir resultados
for i, doc in enumerate(resposta):
    print(f"Frase: {frases[i]}")
    print(f"Sentimento: {doc.sentiment} (Positivo: {doc.confidence_scores.positive: .2f}," 
          f"Neutro: {doc.confidence_scores.neutral: .2f}, Negativo: {doc.confidence_scores.negative: .2f}")
    print("-" * 50)

    