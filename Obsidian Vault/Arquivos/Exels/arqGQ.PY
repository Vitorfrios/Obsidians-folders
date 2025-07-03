import openpyxl
import re
import os

# Lista com os nomes dos tópicos
topicos = [
    "Cálculos Percentuais",
    "Filtro",
    "Classificação",
    "Localizar e Substituir",
    "Ir Para e Ir Para Especial",
    "Preenchendo Linhas em Branco",
    "Não Copiar Linhas Ocultas",
    "Excluir Linhas Específicas",
    "Formatos Personalizados",
    "SOMA e MÉDIA (Novos Exemplos Práticos)",
    "Planilhas Online",
    "Planilhas Agrupadas",
    "Referências e Operações 3D",
    "Análises Rápidas",
    "Hiperlinks e Menus",
    "Configurações de Impressão (Parte 1)",
    "Configurações de Impressão (Parte 2)",
    "Opções de Cálculo",
    "Tradutor de Fórmulas",
    "Traduzir Dados",
    "Exercício 1 - Módulo 2",
    "Exercício 2 - Módulo 2",
    "Exercício 3 - Módulo 2",
    "Exercício 4 - Módulo 2",
    "Exercício 5 - Módulo 2",
    "Exercício 6 - Módulo 2"
]

# Função para limpar o nome do arquivo
def nome_arquivo_valido(texto):
    return re.sub(r'[\\/*?:"<>|]', "", texto)

# Criar uma pasta para os arquivos
os.makedirs("topicos_excel", exist_ok=True)

# Criar um arquivo para cada tópico com numeração
for i, topico in enumerate(topicos, start=1):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Conteúdo"
    sheet['A1'] = topico

    numero = f"{i:02d}"  # Ex: 01, 02, 03...
    nome_limpo = nome_arquivo_valido(topico)
    nome_arquivo = f"{numero} - {nome_limpo}.xlsx"

    caminho = os.path.join("topicos_excel", nome_arquivo)
    workbook.save(caminho)

print("✅ Arquivos Excel numerados criados na pasta 'topicos_excel'.")
