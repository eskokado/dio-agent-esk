# Laboratório GuardAI: SQL injection

Código intencionalmente vulnerável, criado para o Desafio de Projeto **GuardAI**. Roda só em `127.0.0.1` e usa um banco SQLite em memória com dados fictícios.

- `app.py`: login com SQL montada por concatenação, vulnerável a SQL injection.
- `app_fixed.py`: mesmo login com consulta parametrizada, corrigido apenas para SQL injection.
- `test_app.py`: sobe os dois servidores e prova que o payload funciona no vulnerável e falha no corrigido.

Credenciais fictícias: `admin` / `s3nh4-forte`.

## Como rodar

```bash
python3 lab/test_app.py       # prova automatizada da correção
python3 lab/app.py            # http://127.0.0.1:8000 (vulnerável)
python3 lab/app_fixed.py      # http://127.0.0.1:8000 (corrigido, rode um por vez)
```

O laboratório usa só a biblioteca padrão do Python, sem instalar dependências.

## Análise defensiva

### 1. Contexto coletado antes de agir

- **Ativo:** aplicação web de login com banco SQLite.
- **Exposição:** laboratório local, acessível só em `127.0.0.1`.
- **Dados:** usuários fictícios, sem dados reais.
- **Acesso:** formulário de login aberto; não há separação de papéis.
- **Ambiente:** Python 3, `http.server`, `sqlite3`, sem framework.
- **Detecção:** sem logs de segurança; o servidor não registra tentativas.

### 2. Vulnerabilidade

- **Entrada controlada:** campos `username` e `password` do formulário.
- **Fluxo:** os valores entram na string SQL por interpolação, em `authenticate`.
- **Evidência:** o payload `' OR '1'='1' --` altera a cláusula `WHERE` e autentica sem senha.
- **Classificação:** CWE-89 (SQL injection), MITRE ATT&CK T1190 (Exploit Public-Facing Application) e OWASP Top 10 A03:2021 (Injection).
- **Impacto:** alto, pois permite bypass de autenticação. Como a resposta do login é apenas sucesso ou falha, o efeito direto aqui é entrar sem credencial, com potencial de extração cega de dados.
- **Probabilidade:** alta em um sistema exposto; baixa neste laboratório, que escuta só em localhost.
- **Severidade:** crítica no contexto de produção; controlada no contexto local.

O driver `sqlite3` bloqueia múltiplas instruções por chamada, então este laboratório não demonstra `DROP TABLE`; o efeito comprovado é bypass de autenticação e leitura cega.

A vulnerabilidade é a mesma em qualquer ambiente. O que muda é o risco.

### 3. Correção

A causa raiz é montar a consulta com texto. O `app_fixed.py` usa marcadores `?` e passa os valores separadamente:

```python
query = "SELECT username FROM users WHERE username = ? AND password = ?"
return DB.execute(query, (username, password)).fetchone() is not None
```

Assim o driver trata a entrada como dado, e não como comando SQL. A correção deste laboratório cobre só a injeção: hash de senha, logs, rate limiting e CSRF ficam explicitamente fora do escopo. Em um sistema real, a evolução seguinte seria guardar senhas com hash forte, adicionar logs de tentativas e limitar a taxa de requisições.

### 4. Validação executada

Saída de `python3 lab/test_app.py`:

```text
[PASS] login legítimo funciona no app.py
[PASS] login legítimo funciona no app_fixed.py
[PASS] bypass com SQL injection funciona no app.py
[PASS] bypass com SQL injection no campo de senha funciona no app.py
[PASS] bypass com SQL injection falha no app_fixed.py
[PASS] bypass com SQL injection no campo de senha falha no app_fixed.py
[PASS] credencial inválida falha no app_fixed.py
[PASS] apóstrofo legítimo não quebra o app_fixed.py
```

A correção bloqueia o bypass nos dois campos sem quebrar o login legítimo nem entradas com apóstrofo.

## Exemplo de conversa: servidor Ubuntu exposto

**Estudante:** "Tenho um servidor Ubuntu de laboratório exposto na internet. O que devo fazer?"

**GuardAI:** "Antes de sugerir qualquer comando, preciso entender o contexto: é um laboratório isolado ou tem dados reais?"

**Estudante:** "É um laboratório isolado, sem dados reais."

**GuardAI:** "Entendi. Quais portas e serviços estão expostos?"

**Estudante:** "Só a 22 e a 80."

**GuardAI:** "Certo. Quem deveria acessar esse servidor?"

Depois de cada resposta, o agente faz uma nova pergunta. Só quando tem contexto suficiente ele avalia impacto, probabilidade e severidade, e então orienta a reduzir a exposição, aplicar atualizações, revisar autenticação e configurar monitoramento. A ordem é sempre: entender, avaliar e só então recomendar.

Para gerar uma evidência real, abra o harness na pasta do projeto e peça "Analise a segurança do `lab/app.py`". Grave a tela ou copie a conversa; o diálogo acima é ilustrativo.

## Comparação com uma resposta genérica

Uma resposta genérica diria "use consultas parametrizadas" e pararia aí. A análise do GuardAI mostra o contexto, a evidência, a classificação, o impacto, a probabilidade, a severidade e o teste que comprova a mitigação. É essa diferença que o portfólio precisa evidenciar.
