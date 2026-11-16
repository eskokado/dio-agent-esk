# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🛡️ GuardAI: a especialização em cibersegurança

Este repositório é a minha entrega do Desafio de Projeto **GuardAI**. Sobre o DIO Agent original, criei uma especialização defensiva: em vez de responder de imediato, o agente pede contexto, separa vulnerabilidade de risco, avalia impacto, probabilidade e severidade, e orienta a correção.

**Por quê:** uma resposta genérica do tipo "use consultas parametrizadas" não forma um analista. Segurança depende de contexto: a mesma falha pode ser crítica em produção e de baixo risco em um laboratório isolado.

**O que mudou:**

- [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md): a skill com o processo de análise, da coleta de contexto à validação da correção.
- [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md): a base sobre tríade CIA, ativo, ameaça, vulnerabilidade, risco, impacto, probabilidade, severidade, CWE, CVSS, MITRE ATT&CK e boas práticas.
- [`agent/persona.md`](agent/persona.md): a mentalidade de analista defensivo.
- [`AGENTS.md`](AGENTS.md): o registro da skill e da base de conhecimento.
- [`lab/`](lab/README.md): um login intencionalmente vulnerável a SQL injection, a versão corrigida e um teste que comprova a mitigação; use apenas em ambiente local.

**A melhoria escolhida:** toda análise segue o mesmo formato (evidência, impacto, probabilidade, severidade, correção e validação) e cita referências públicas como CWE e MITRE ATT&CK.

**Como rodar:** instale um harness e abra esta pasta, como nos [3 passos](#-comece-em-3-passos). Depois peça, por exemplo, "Analise a segurança do `lab/app.py`". Para ver a prova da correção, rode `python3 lab/test_app.py`. O walkthrough completo está em [`lab/README.md`](lab/README.md).

**Stack e evidências:** o laboratório usa Python 3 e só a biblioteca padrão. O enunciado do desafio está em [`docs/evidence/desafio-guardai.pdf`](docs/evidence/desafio-guardai.pdf), e a saída real do teste fica em [`lab/README.md`](lab/README.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/eskokado/dio-agent-esk.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent-esk`; pelo .zip, `dio-agent-esk-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Avalia código e cenários de segurança com impacto, probabilidade e severidade | "Analise a segurança deste login." |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🛡️ Análise de vulnerabilidades**

```
Quero uma análise de segurança defensiva.
- O que analisar: [cole o código, a configuração ou descreva o cenário]
- Onde roda: [laboratório local, servidor interno, produção]
- Quem acessa: [só eu, equipe, internet]
- Dados envolvidos: [fictícios, dados pessoais, credenciais]
- O que já sei: [suspeita, teste que falhou, nada ainda]
Me pergunta o contexto que faltar antes de sugerir a correção.
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent-esk/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           O que o agente sabe sobre a DIO e sobre segurança
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
├── lab/                     Laboratório de SQL injection (app vulnerável, corrigido e teste)
└── docs/
    ├── evidence/            Enunciado do desafio
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
