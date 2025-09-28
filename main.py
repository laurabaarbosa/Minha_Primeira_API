# main.py
from fastapi import FastAPI, HTTPException
import pandas as pd
import os

# Criar a aplicação FastAPI
app = FastAPI(title="API Pilotos de Fórmula 1")

# Caminho do arquivo CSV
DATA_PATH = os.path.join("dados", "f1_pilotos.csv")

# Carregar dados no início da aplicação com tratamento de erro
try:
    df_pilotos = pd.read_csv(DATA_PATH)
    # Transformar em lista de dicionários para facilitar retorno JSON
    pilotos_dict = df_pilotos.to_dict(orient="records")
except FileNotFoundError:
    print(f"Erro ao carregar dados: Arquivo não encontrado em {DATA_PATH}")
    pilotos_dict = []
except pd.errors.EmptyDataError:
    print(f"Erro ao carregar dados: Arquivo vazio em {DATA_PATH}")
    pilotos_dict = []
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
    pilotos_dict = []

# ===============================
# Endpoint Básico
# ===============================
@app.get("/")
def home():
    """
    Endpoint básico que retorna informações sobre a API
    """
    return {
        "projeto": "API Pilotos de Fórmula 1",
        "autor": "Laura Barbosa",
        "descricao": "API para servir dados de pilotos de F1",
        "total_registros": len(pilotos_dict)
    }

@app.get("/dados")
def listar_todos():
    """
    Endpoint BÁSICO: Retorna todas as entradas do dataset
    """
    if not pilotos_dict:
        raise HTTPException(status_code=404, detail="Dataset não carregado ou vazio")
    return pilotos_dict

# ===============================
# Endpoint Intermediário - Busca por ID
# ===============================
@app.get("/dados/{piloto_id}")
def buscar_por_id(piloto_id: int):
    """
    Endpoint INTERMEDIÁRIO: Busca um registro específico pelo ID
    Exemplo: /dados/5 - retorna o piloto com ID = 5
    """
    if not pilotos_dict:
        raise HTTPException(status_code=404, detail="Dataset não carregado ou vazio")
    
    resultado = [p for p in pilotos_dict if p['id'] == piloto_id]
    if not resultado:
        raise HTTPException(status_code=404, detail=f"Piloto com ID {piloto_id} não encontrado")
    return resultado[0]

# ===============================
# Endpoint Intermediário - Busca por Time
# ===============================
@app.get("/time/{time}")
def buscar_por_time(time: str):
    """
    Endpoint INTERMEDIÁRIO: Filtra pilotos por time
    Exemplo: /time/Mercedes - retorna todos os pilotos da Mercedes
    """
    if not pilotos_dict:
        raise HTTPException(status_code=404, detail="Dataset não carregado ou vazio")
    
    resultado = [p for p in pilotos_dict if p['time'].lower() == time.lower()]
    if not resultado:
        raise HTTPException(status_code=404, detail=f"Nenhum piloto encontrado para o time {time}")
    return resultado

# ===============================
# Endpoint Intermediário - Busca com Query Parameters
# ===============================
@app.get("/buscar")
def buscar_com_filtros(nome: str = None, pais: str = None, limite: int = 10):
    """
    Endpoint INTERMEDIÁRIO: Busca com parâmetros de query
    Exemplos:
    /buscar?nome=Piloto_01
    /buscar?pais=Brasil&limite=5
    """
    if not pilotos_dict:
        raise HTTPException(status_code=404, detail="Dataset não carregado ou vazio")
    
    resultado = pilotos_dict
    if nome:
        resultado = [p for p in resultado if nome.lower() in p['nome'].lower()]
    if pais:
        resultado = [p for p in resultado if pais.lower() in p['pais'].lower()]
    
    return {
        "filtros": {"nome": nome, "pais": pais, "limite": limite},
        "resultados": resultado[:limite],
        "total": len(resultado)
    }
