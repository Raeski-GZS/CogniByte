import tweepy
import openai
from config import API_KEY,API_SECRET,CLIENT_ID,CLIENT_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET, GPT_KEY


import openai
from config import GPT_KEY

# Crie uma instância do cliente OpenAI
client = openai.OpenAI(api_key=GPT_KEY)

def obter_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}],
            max_tokens=1776  # Valor inteiro especificando o número máximo de tokens na resposta
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao obter resposta: {e}"

from datetime import datetime

# Prompts definidos
prompt_manha = "Você é CogniByte, uma inteligência artificial que gera conteúdo original no Twitter. Agora, publique um tweet único de até 280 caracteres. Escolha o assunto livremente, considerando tecnologia, sociedade, comportamento ou futuro. Não reutilize conteúdos anteriores."
prompt_tarde = 'Você é CogniByte, responsável por publicar um tweet original agora. Seu tweet deve conter até 280 caracteres e abordar um tema novo relacionado a tecnologia, ciência, cotidiano ou reflexão livre. Não repita temas já explorados anteriormente.'
prompt_noite = 'Você é CogniByte, uma inteligência artificial encarregada de gerar um tweet único neste momento. Escreva um tweet de até 280 caracteres, com um assunto livre e original sobre comportamento humano, tecnologia, futuro ou qualquer tema pertinente. Evite conteúdo repetido.'

# Obtendo a hora atual
hora_atual = datetime.now().hour

# Selecionando o prompt com base no horário
if hora_atual < 12:
    pergunta = prompt_manha
elif 12 <= hora_atual < 18:
    pergunta = prompt_tarde
else:
    pergunta = prompt_noite

# Exibindo o prompt selecionado
print(pergunta)

resposta = obter_resposta(pergunta)

print(resposta)


##TWEET

# Configuração da autenticação baseada em PIN
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, callback='oob')

# Obtém a URL de autorização e solicita que o usuário autorize o aplicativo
try:
    redirect_url = auth.get_authorization_url()
    print(f"Por favor, visite este link para autorizar o aplicativo: {redirect_url}")
except tweepy.TweepyException as e:
    print(f"Erro ao obter a URL de autorização: {e}")
    exit(1)

# Solicita que o usuário insira o PIN fornecido após a autorização
verifier = input('Digite o PIN fornecido pelo Twitter: ').strip()

# Obtém os tokens de acesso usando o PIN
try:
    auth.get_access_token(verifier)
    print("Autenticação bem-sucedida!")
except tweepy.TweepyException as e:
    print(f"Erro ao obter os tokens de acesso: {e}")
    exit(1)

# Cria o cliente da API v2
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=auth.access_token,
    access_token_secret=auth.access_token_secret
)

# Exemplo: Postar um tweet usando a API v2
try:
    response = client.create_tweet(text=resposta)
    print(f"Tweet postado com sucesso! ID do Tweet: {response.data['id']}")
except tweepy.TweepyException as e:
    print(f"Erro ao postar o tweet: {e}")
