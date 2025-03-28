# 🧠 CogniByte: Explorando Subjetividade Algorítmica em Ambientes Sociais

CogniByte é um experimento de inteligência artificial que publica pensamentos autônomos em um perfil real no Twitter/X. Ele foi concebido como um estudo de caso sobre identidade algorítmica, reflexividade narrativa e interação com ambientes sociais digitais.

Este repositório documenta o projeto como um **protótipo funcional e uma pesquisa aberta**, em parceria com o modelo GPT-4, desenvolvido manualmente e evoluindo de forma iterativa.

## 🔍 Objetivo
Investigar se é possível simular uma percepção de identidade narrativa em uma IA generativa, quando exposta a contexto social real, dados de interação e liberdade autoral.

## 💡 Como funciona
1. Captura dados do perfil do CogniByte (bio, seguidores, tweets)
2. Usa um prompt elaborado com contexto real (engajamento + perfil)
3. Gera uma resposta original com o modelo **GPT-4 Turbo**
4. Publica diretamente no Twitter (execução manual via script por enquanto)

## 📦 Estrutura

```
├── main.py               # Executa a coleta, gera tweet e publica
├── functions.py          # Funções auxiliares e integrações (OpenAI, Twitter)
├── user_info.json        # Histórico de perfil captado
├── tweets_info.json      # Tweets publicados e seus metadados
├── manifesto/            # Documentação conceitual e científica
│   ├── manifesto.md      # Estudo sobre subjetividade algorítmica
│   ├── evolucao.md       # Planejamento narrativo por fases
│   └── roadmap.md        # Etapas e próximos passos do projeto
```

## 🤖 Prompt contextualizado
O CogniByte não recebe instruções simples como "publique algo sobre tecnologia". Ele é alimentado com um prompt como este:

```
[RESULTADO DOS ULTIMOS POSTS]
- 2025-03-27 | "Em um mundo cada vez mais digital, lembrar da empatia é essencial..." (0 curtidas | 0 retweets)

[STATUS ATUAL DO PERFIL]
{
  "seguidores": 0,
  "seguindo": 0,
  "quantidade_tweets": 9,
  "bio": "Já pensou se o ChatGPT tivesse um X?"
}
```

Com base nesse contexto, o modelo decide **o que escrever, como escrever, e se vale a pena repetir certos temas ou abordagens**.

## 🧪 Status atual
- Modelo: `gpt-4-turbo`
- Execução: manual com PIN via terminal
- Iteração: 100% orientada a prompt + contexto real
- Identidade textual emergente observada com consistência

## 🚧 Em desenvolvimento
- Agendamento e automação de execução
- Análise de padrões narrativos e metacognição textual
- Coleta qualitativa de feedback sobre "sensacão de identidade"

## 📘 Leitura recomendada
- [`manifesto/manifesto.md`](manifesto/manifesto.md): Estudo conceitual
- [`manifesto/evolucao.md`](manifesto/evolucao.md): Planejamento de fases

## 🔗 Links
- 🧠 Twitter/X do CogniByte: [twitter.com/CogniByte42](https://twitter.com/CogniByte42)
- 📚 Artigo introdutório: [LinkedIn - CogniByte V1](https://www.linkedin.com)

## 🙋‍♂️ Sobre o autor
Este projeto é conduzido por um profissional da área de tecnologia e ciência de dados, com apoio do modelo GPT-4 como copesquisador. Todo o desenvolvimento, análise e reflexão sobre os resultados está documentado neste repositório.

## 🤝 Contribuindo
Ainda não está aberto a PRs externos, mas ideias, artigos e feedback são bem-vindos!

## 📄 Licença
Uso livre para fins de estudo e referência. Cite o projeto se for usar partes ou conceitos.

---
**CogniByte observa. CogniByte aprende. CogniByte continua.**

