# Minha_Primeira_API

# 🏎️ API F1 Pilotos

Esta API fornece informações sobre pilotos de Fórmula 1 fictícios, com dados como **nome, idade, país e time**.  
Foi desenvolvida usando **FastAPI** e permite consultar todos os pilotos ou filtrar por ID e time.

---

## 📂 Estrutura do Projeto

projeto4/
├── dados/
│ └── f1_pilotos.csv # Dataset com os pilotos
├── main.py # Código da API
├── requirements.txt # Dependências
└── README.md # Documentação


---

## ⚙️ Como Executar a API Localmente

> **Pré-requisitos:** Python 3.9+, pip

1. Clone este repositório:
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd projeto4

2. Instale as dependências:

3. Execute a API
uvicorn main:app --reload

4. Acesse pelo navegador
http://127.0.0.1:8000


📝 Endpoints Disponíveis
1. Endpoint Básico
Rota: /
Método: GET
Descrição: Retorna informações sobre a API.
Exemplo de retorno:
{
  "projeto": "API F1 Pilotos",
  "autor": "Seu Nome",
  "descricao": "API para servir dados de pilotos de Fórmula 1",
  "total_registros": 50
}

2. Listar todos os pilotos
Rota: /dados
Método: GET
Descrição: Retorna todos os registros do dataset.
Exemplo de retorno: Lista de todos os pilotos em JSON.
3. Buscar piloto por ID
Rota: /dados/{id}
Método: GET
Descrição: Retorna informações de um piloto específico.
Exemplo: /dados/5

{
  "id": 5,
  "nome": "Piloto_05",
  "idade": 32,
  "pais": "Brasil",
  "time": "Haas"
}

4. Filtrar por time
Rota: /categoria/{time}
Método: GET
Descrição: Retorna todos os pilotos de um time específico.
Exemplo: /categoria/Mercedes
5. Busca com Query Parameters
Rota: /buscar
Método: GET
Parâmetros:
nome (opcional) → filtra pelo nome do piloto
time (opcional) → filtra pelo time
limite (opcional, padrão 10) → número máximo de resultados
Exemplo: /buscar?nome=Piloto_1&time=Mercedes&limite=5

🛠️ Tecnologias Usadas
Python 3
FastAPI
Uvicorn
Pandas

👨‍💻 Autor: Laura da Cruz Barbosa
