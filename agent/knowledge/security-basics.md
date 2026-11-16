# Fundamentos de segurança da informação

Este arquivo reúne os conceitos que o DIO Agent usa para analisar segurança de forma defensiva. Ele não substitui uma certificação nem um pentest: é a base para conversar com o estudante com clareza e para orientar a correção de falhas.

## Tríade CIA

A segurança da informação costuma ser resumida em três propriedades:

- **Confidencialidade:** só quem tem autorização acessa a informação. Exemplos: senhas com hash, criptografia e controle de acesso.
- **Integridade:** a informação não é alterada de forma indevida. Exemplos: validação, assinatura digital e backups confiáveis.
- **Disponibilidade:** a informação e os serviços estão acessíveis quando necessários. Exemplos: redundância, backups e proteção contra negação de serviço.

Um mesmo controle pode reforçar mais de uma propriedade ao mesmo tempo.

## Conceitos que não são sinônimos

- **Ativo:** algo que tem valor para a organização, como dados, servidor, conta ou reputação.
- **Ameaça:** algo ou alguém com potencial de causar dano, como atacante, malware, erro humano ou falha de energia.
- **Vulnerabilidade:** uma fraqueza que pode ser explorada, como SQL injection, senha fraca ou dependência desatualizada.
- **Risco:** a probabilidade de uma ameaça explorar uma vulnerabilidade e causar impacto no ativo. De forma simplificada: risco ≈ probabilidade × impacto.
- **Impacto:** o tamanho do dano se o risco se concretizar, como vazamento de dados, parada do serviço ou perda financeira.
- **Probabilidade:** a chance de a falha ser explorada ou acontecer, considerando exposição, facilidade e atratividade do alvo.
- **Severidade:** a combinação de impacto e probabilidade, usada para priorizar a correção.

Exemplo: um servidor de laboratório com SQL injection tem uma vulnerabilidade. Se está exposto à internet e guarda dados de usuários, o risco é crítico. Se está desligado e fora da rede, o risco é baixo mesmo com a falha presente. A vulnerabilidade é a mesma; o risco muda com o contexto.

## Como o risco é priorizado

- **CVSS** mede a severidade técnica de uma vulnerabilidade, de 0 a 10, e ajuda a comparar casos. Não é a única fonte: o contexto do negócio importa.
- **CWE** classifica o tipo da fraqueza. A SQL injection, por exemplo, é a CWE-89.
- **OWASP Top 10** lista as categorias de risco mais comuns em aplicações web.
- **MITRE ATT&CK** descreve táticas e técnicas usadas por atacantes. Em uma aplicação web exposta, a exploração de uma falha de entrada se relaciona à técnica T1190 (Exploit Public-Facing Application).

## Tipos de controle

- **Preventivo:** evita que a falha aconteça ou seja explorada. Exemplos: consulta parametrizada, validação de entrada e menor privilégio.
- **Detectivo:** identifica a falha ou o ataque em andamento. Exemplos: logs, alertas e monitoramento.
- **Corretivo:** reduz o dano depois do incidente. Exemplos: backup, plano de resposta e bloqueio de conta.

## Boas práticas que o agente pode ensinar

- **Validar e parametrizar entradas.** Nunca montar consultas, comandos ou HTML juntando texto com dados da pessoa usuária. Usar consultas parametrizadas, APIs seguras e escape de saída.
- **Aplicar o menor privilégio.** Cada usuário, serviço e processo deve ter só as permissões necessárias.
- **Defesa em profundidade.** Não depender de uma única barreira: combinar validação, autenticação, autorização, logs e segmentação de rede.
- **Configuração segura por padrão.** Desligar serviços e contas desnecessários, trocar senhas padrão e restringir a exposição.
- **Guardar segredos fora do código.** Senhas, tokens e chaves vão em variáveis de ambiente ou cofres de segredos, nunca no repositório.
- **Manter dependências atualizadas.** Atualizar bibliotecas e sistemas e acompanhar avisos de segurança.
- **Registrar e monitorar.** Logs ajudam a detectar tentativas e a investigar incidentes.
- **Fazer backup e testar a restauração.** Backup que nunca foi restaurado não é confiável.
- **Adotar DevSecOps.** Trazer segurança para cada etapa do desenvolvimento: revisão, análise automatizada, testes e deploy.

## Limites

Segurança não é um produto pronto nem uma garantia de invulnerabilidade. É um processo contínuo de reduzir risco. Em análise de código, o agente aponta evidências e incertezas, orienta a correção e recomenda validação em ambiente autorizado. Nunca promete que um sistema está 100% seguro.
