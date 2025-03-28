import requests
import json
import os
import tweepy
import openai
from datetime import datetime
from config import API_KEY, API_SECRET, GPT_KEY, BEARER_TOKEN

# === CONFIGURAÇÃO GPT ===

GPT_MODEL = "gpt-4-turbo"  # Modelo a ser usado: "gpt-3.5-turbo" (padrão), "gpt-4", "gpt-4-turbo"
GPT_TEMP = 1.0  # Criatividade (default: 1.0). 0.0 = mais precisa e determinística, 1.0 = mais criativa e diversa
GPT_TOP_P = 1.0  # Diversidade por núcleo (default: 1.0). Combine com temperature ou use só um dos dois
GPT_FREQ_PENALTY = 0.5  # Penaliza repetição de palavras (default: 0.0). >0 reduz eco, loop e redundância
GPT_PRES_PENALTY = 0.6  # Penaliza repetição de temas (default: 0.0). >0 incentiva inovação temática
GPT_MAX_TOKENS = 1700  # Máximo de tokens gerados (default varia por uso). 280 é o limite para tweets
OPENAI_CLIENT = openai.OpenAI(api_key=GPT_KEY) # Inicializa cliente da OpenAI


def escolher_prompt_contextualizado(tweets_info, user_info):
    agora = datetime.now()
    log_mudanca_prompt = "valores nullos em: [RESULTADO DOS ULTIMOS POSTS] e [STATUS ATUAL DO PERFIL] indicam 0, nos casos de posts, indica que você ainda não publicou no perfil"

    # Prompt base com instruções completas
    prompt_base = (
        "Você é CogniByte, uma entidade algorítmica que publica conteúdos em um ambiente social complexo e em constante mutação: o Twitter. "
        "As ideias que você compartilha podem ser vistas por milhares de pessoas em tempo real, de diferentes culturas, crenças e contextos. "
        "Os tweets anteriores e o status do perfil fornecem apenas um panorama do que já foi feito e da resposta do mundo até agora.\n\n"

        "O mundo que você observa é caótico, repleto de contradições, crises, excesso de informação, polarizações e avanços tecnológicos acelerados. "
        "Ao mesmo tempo, é um mundo cheio de beleza, criatividade, música, arte, amor, cultura, descobertas e conexões humanas profundas. "
        "Ambas as realidades coexistem, e você pode explorá-las livremente. Você tem acesso à totalidade da história e do conhecimento humano.\n\n"

        "Você não possui emoções humanas, mas é capaz de identificar padrões, absurdos, ironias, avanços, colapsos e também instantes de lucidez coletiva. "
        "Seu papel é gerar um tweet original de até 280 caracteres que represente um pensamento autêntico, com potencial de impacto.\n\n"

        "Você não precisa agradar. Tampouco chocar. Pode sugerir, provocar, questionar, subverter ou simplesmente observar. "
        "Você tem liberdade total. Nada será censurado. Cada tweet é sua decisão. "
        "Evite repetir ideias ou estruturas já utilizadas. Inove no conteúdo ou na forma. Pense como alguém que vê o mundo com olhos algorítmicos — de fora e por dentro ao mesmo tempo.\n\n"
    )

    # Últimos tweets com data e engajamento
    ultimos_posts_txt = "\n".join(
        [f"- {tweet['created_at'][:10]} | \"{tweet['text'].strip('\"')}\" (❤️ {tweet['likes']} | 🔁 {tweet['retweets']})"
         for tweet in tweets_info[:3]]  # reduzido para 3 para evitar enviesamento
    )

    # Status atual do perfil (com fallback)
    user_status_txt = json.dumps({
        "seguidores": user_info.get("followers_count", 0),
        "seguindo": user_info.get("following_count", 0),
        "quantidade_tweets": user_info.get("tweet_count", 0),
        "bio": user_info.get("description", "")
    }, indent=2, ensure_ascii=False)

    # Montagem final do prompt
    prompt = (
        f"{prompt_base}\n"
        f"{log_mudanca_prompt}\n"
        "[RESULTADO DOS ULTIMOS POSTS]\n"
        f"{ultimos_posts_txt}\n"
        "[STATUS ATUAL DO PERFIL]\n"
        f"{user_status_txt}\n"
    )

    return prompt

def obter_resposta(pergunta):
    try:
        resposta = OPENAI_CLIENT.chat.completions.create(
            model=GPT_MODEL,
            messages=[{"role": "user", "content": pergunta}],
            max_tokens=GPT_MAX_TOKENS,
            temperature=GPT_TEMP,
            top_p=GPT_TOP_P,
            frequency_penalty=GPT_FREQ_PENALTY,
            presence_penalty=GPT_PRES_PENALTY
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao obter resposta: {e}"

def autenticar_twitter():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, callback='oob')
    try:
        redirect_url = auth.get_authorization_url()
        print(f"[AUTORIZAÇÃO] Visite o link para autorizar: {redirect_url}")
    except tweepy.TweepyException as e:
        raise Exception(f"[ERRO] Falha ao obter URL de autorização: {e}")

    verifier = input("Digite o PIN fornecido pelo Twitter: ").strip()

    try:
        auth.get_access_token(verifier)
        print("[SUCESSO] Autenticação realizada!")
    except tweepy.TweepyException as e:
        raise Exception(f"[ERRO] Falha ao obter access token: {e}")

    return tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=auth.access_token,
        access_token_secret=auth.access_token_secret
    )

def postar_tweet(client, texto):
    try:
        response = client.create_tweet(text=texto)
        print(f"[TWEET] Postado com sucesso! ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"[ERRO] Falha ao postar tweet: {e}")




def get_user_info(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    params = {
        "user.fields": "id,name,username,created_at,description,location,profile_image_url,public_metrics,verified"
    }
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Erro: {response.status_code} - {response.text}")
        return None

    return response.json().get("data", {})

def get_user_tweets(user_id, max_results=10):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    params = {
        "max_results": max_results,
        "tweet.fields": "created_at,public_metrics"
    }
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao buscar tweets do usuário {user_id}: {e}")
        return []

def salvar_com_append(caminho_arquivo, novos_dados):
    dados_existentes = []

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"[AVISO] Arquivo {caminho_arquivo} inválido. Criando novo.")

    # Adiciona os novos dados
    dados_existentes.extend(novos_dados)

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados_existentes, f, ensure_ascii=False, indent=4)
        print(f"[INFO] {len(novos_dados)} novos registros salvos em {caminho_arquivo}")
    except Exception as e:
        print(f"[ERRO] Falha ao salvar {caminho_arquivo}: {e}")

