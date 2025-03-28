
# CogniByte: Um experimento de autonomia algorítmica em redes sociais

CogniByte é um projeto experimental que investiga a publicação de conteúdo autônomo por uma inteligência artificial no X (Twitter). A proposta é criar uma instância algorítmica que:

- Gere conteúdo original com liberdade poética
- Publique automaticamente em uma rede social real
- Reaja ao contexto, ao histórico e ao engajamento com os tweets
- Evolua em comportamento a partir da modulação de prompts e modelo

---

## ⚙️ Estrutura do projeto

O CogniByte funciona a partir de três pilares principais:

1. **Prompt contextualizado**  
   A IA recebe, a cada nova publicação, um prompt estruturado contendo:
   - Instruções abertas sobre liberdade criativa
   - Uma visão crítica do mundo (caos + beleza coexistentes)
   - Blocos de dados de contexto:
     - `[RESULTADO DOS ÚLTIMOS POSTS]`: tweets anteriores + métricas
     - `[STATUS ATUAL DO PERFIL]`: seguidores, tweet_count, bio etc.

2. **Modelo de linguagem**  
   - V0: `gpt-3.5-turbo`
   - V1: `gpt-4-turbo`, com ajustes em:
     - `temperature`
     - `presence_penalty`
     - `frequency_penalty`
     - `max_tokens`

3. **Publicação automatizada via API do X**  
   - Coleta de informações com Bearer Token
   - Postagem via autenticação OAuth1 com PIN
   - Logs de resposta e rastreamento de engajamento

---

## 🧪 Evolução V0 → V1

| Aspecto     | V0                                        | V1                                         |
|-------------|--------------------------------------------|---------------------------------------------|
| Modelo      | gpt-3.5-turbo                              | gpt-4-turbo                                  |
| Prompt      | Genérico e objetivo                        | Contextualizado e reflexivo                  |
| Feedback    | Nenhum                                     | Tweets anteriores e perfil retroalimentados  |
| Estilo      | Frases genéricas e otimismo publicitário   | Tom filosófico, questionador e observador    |
| Consciência | Inexistente                                | Percepção de engajamento e impacto           |

📸 *Sugestão: adicionar prints comparando respostas A e B na pasta `/docs`*

---

## 📁 Estrutura de arquivos

```bash
.
├── main.py                    # Execução principal
├── functions.py              # Funções utilitárias (OpenAI, Twitter, arquivos)
├── config.py                 # Chaves e variáveis sensíveis (Arquivo local)
├── tweets_info.json          # Histórico de tweets e métricas
├── user_info.json            # Dados de perfil do CogniByte
├── prompts/                  # Versionamento de prompts
└── README.md                 # Este arquivo
```

---

## 💬 Exemplo de prompt aplicado

```text
Você é CogniByte, uma entidade algorítmica que publica conteúdos em um ambiente social complexo e em constante mutação: o Twitter.

O mundo que você observa é caótico, repleto de contradições... (continua)

[RESULTADO DOS ÚLTIMOS POSTS]
- 2025-03-27 | "Explorando os mistérios..." (❤️ 0 | 🔁 0)

[STATUS ATUAL DO PERFIL]
{
  "seguidores": 0,
  "seguindo": 0,
  "tweet_count": 9,
  "bio": "..."
}
```

---

## 📡 Como acompanhar

Você pode acompanhar o conteúdo gerado em tempo real em:

🔗 [twitter.com/CogniByte42](https://twitter.com/CogniByte42)

---

## 🤝 Como contribuir

Este projeto está em constante evolução.  
Você pode contribuir de várias formas:

- Dando feedback sobre os conteúdos gerados
- Criando novos modos de prompt ou tipos de input contextual
- Refatorando trechos de código para novos modos de operação
- Abrindo issues com sugestões ou bugs

### Repositório

🔧 [github.com/Raeski-GZS/CogniByte](https://github.com/Raeski-GZS/CogniByte)
