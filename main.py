from functions import *
from datetime import datetime

if __name__ == "__main__":
    username = "CogniByte42"
    process_timestamp = datetime.now().isoformat()

    user_info = get_user_info(username)

    if user_info:
        user_info["process_timestamp"] = process_timestamp
        salvar_com_append("user_info.json", [user_info])

        # Traz até 100 tweets (máximo da API por chamada)
        tweets_raw = get_user_tweets(user_info.get("id"), max_results=100)

        tweets_info = []
        for tweet in tweets_raw:
            tweet_data = {
                "id": tweet.get("id"),
                "created_at": tweet.get("created_at"),
                "text": tweet.get("text"),
                "likes": tweet.get("public_metrics", {}).get("like_count", 0),
                "retweets": tweet.get("public_metrics", {}).get("retweet_count", 0),
                "quote_count": tweet.get("public_metrics", {}).get("quote_count", 0),
                "process_timestamp": process_timestamp
            }
            tweets_info.append(tweet_data)

        salvar_com_append("tweets_info.json", tweets_info)

        # Gera prompt completo com contexto
        prompt = escolher_prompt_contextualizado(tweets_info, user_info)
        print("[PROMPT FINAL]:\n", prompt)

        # Gera resposta com GPT
        resposta = obter_resposta(prompt)

        # Autentica e posta o tweet
        print("[RESPOSTA GERADA]:", resposta)
        client = autenticar_twitter()
        postar_tweet(client, resposta)

    else:
        print("Usuário não encontrado ou erro na API.")