# 📘 Atividade: Games in Python

## 🎯 Objetivo

Construir uma versão em linha de comando do jogo da forca para praticar seleção aleatória, manipulação de strings, loops e condicionais. Ao final, você terá um jogo funcional com controle de tentativas, validação básica de entrada e mensagens claras de vitória ou derrota.

## 📝 Tarefas

### 🛠️ Configure o Jogo da Forca

#### Descrição
Prepare a base do jogo definindo a lista de palavras, escolhendo uma palavra secreta aleatória e inicializando o estado inicial da partida.

#### Requisitos
O programa concluído deve:

- Definir uma lista com pelo menos 5 palavras possíveis.
- Selecionar a palavra secreta com `random.choice()`.
- Inicializar `guessed_letters` como lista ou conjunto vazio.
- Inicializar `incorrect_guesses` com `0` e `max_incorrect` com um valor fixo (por exemplo, `6`).
- Exibir ao iniciar o jogo a quantidade máxima de erros permitidos.

### 🛠️ Implemente o Loop do Jogo

#### Descrição
Implemente o loop principal para receber palpites de letras, atualizar o progresso da palavra e encerrar o jogo com vitória ou derrota.

#### Requisitos
O programa concluído deve:

- Mostrar o progresso atual da palavra no formato `_ _ _` com letras já acertadas reveladas.
- Solicitar ao usuário um palpite de uma letra por rodada.
- Validar a entrada para aceitar apenas uma letra por vez.
- Atualizar o estado do jogo para letras corretas e incrementar `incorrect_guesses` para palpites incorretos.
- Evitar penalizar o jogador quando uma letra já tentada for repetida.
- Encerrar com mensagem de vitória quando todas as letras forem descobertas.
- Encerrar com mensagem de derrota quando `incorrect_guesses` atingir `max_incorrect`, exibindo a palavra secreta.