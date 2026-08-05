# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construir uma API REST simples com FastAPI para praticar criação de rotas, validação de dados com Pydantic e respostas HTTP adequadas. Ao final, você terá um pequeno serviço de tarefas com operações de criação, listagem, consulta e remoção.

## 📝 Tarefas

### 🛠️ Configure a Base da API

#### Descrição
Crie a estrutura inicial da aplicação FastAPI e prepare um armazenamento em memória para representar tarefas.

#### Requisitos
O programa concluído deve:

- Criar uma instância FastAPI em um arquivo starter-code.py.
- Definir um modelo TaskCreate com os campos title (obrigatório) e done (opcional, padrão False).
- Definir um modelo Task com os campos id, title e done.
- Criar uma lista em memória para armazenar tarefas e uma variável para controlar o próximo id.

### 🛠️ Implemente Endpoints REST

#### Descrição
Implemente os endpoints principais para manipular tarefas e retornar respostas HTTP coerentes.

#### Requisitos
O programa concluído deve:

- Criar endpoint GET /health que retorne status ok.
- Criar endpoint POST /tasks para cadastrar uma tarefa e retornar status 201.
- Criar endpoint GET /tasks para listar todas as tarefas.
- Criar endpoint GET /tasks/{task_id} para buscar tarefa por id e retornar 404 quando não existir.
- Criar endpoint DELETE /tasks/{task_id} para remover tarefa e retornar 204 em caso de sucesso.

### 🛠️ Valide e Teste a API

#### Descrição
Teste manualmente os endpoints e garanta que os cenários básicos de sucesso e erro estejam funcionando.

#### Requisitos
O programa concluído deve:

- Executar a API localmente com uvicorn.
- Testar ao menos um cenário de criação, listagem e remoção de tarefa.
- Mostrar erro 404 ao consultar ou remover id inexistente.
- Registrar no código exemplos de chamadas em comentários curtos para facilitar validação dos testes.
