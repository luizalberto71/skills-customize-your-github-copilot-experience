
# 📘 Assignment: Games in Python

## 🎯 Objective

Construir uma versão em linha de comando do jogo da forca para praticar seleção aleatória, manipulação de strings, loops e condicionais. Ao final, você terá um jogo completo com controle de tentativas e mensagens de resultado.

## 📝 Tasks

### 🛠️ Setup the Hangman Game

#### Descrição
Prepare a base do jogo definindo a lista de palavras, escolhendo uma palavra secreta aleatória e inicializando o estado inicial da partida.

#### Requisitos
O programa concluído deve:

- Definir uma lista com pelo menos 5 palavras possíveis.
- Selecionar a palavra secreta com `random.choice()`.
- Inicializar `guessed_letters` como lista ou conjunto vazio.
- Inicializar `incorrect_guesses` com `0` e `max_incorrect` com um valor fixo (por exemplo, `6`).

### 🛠️ Implement the Game Loop

#### Descrição
Implemente o loop principal para receber palpites de letras, atualizar o progresso da palavra e encerrar o jogo com vitória ou derrota.

#### Requisitos
O programa concluído deve:

- Mostrar o progresso atual da palavra no formato `_ _ _` com letras já acertadas reveladas.
- Solicitar ao usuário um palpite de uma letra por rodada.
- Atualizar o estado do jogo para letras corretas e incrementar `incorrect_guesses` para palpites incorretos.
- Encerrar com mensagem de vitória quando todas as letras forem descobertas.
- Encerrar com mensagem de derrota quando `incorrect_guesses` atingir `max_incorrect`, exibindo a palavra secreta.