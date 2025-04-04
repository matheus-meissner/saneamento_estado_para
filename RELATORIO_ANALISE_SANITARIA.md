# 🛰️ Análise Geoespacial do Saneamento Básico em Barcarena, Belém e Breves (PA)

## 🎯 Objetivo
Este projeto tem como objetivo analisar e visualizar, de forma geoespacial, a situação dos serviços de saneamento básico nos municípios de Barcarena, Belém e Breves (PA), com foco em:
- Abastecimento de água
- Coleta de lixo
- Coleta de esgoto

## 🗂️ Fontes de Dados
- **SNIS** (Sistema Nacional de Informações sobre Saneamento): Indicadores IN058, IN061, IN072
- **IBGE**: Censo e PNSB
- **MapBiomas**: Geometria dos municípios e uso do solo
- **Prefeituras locais**: Dados suplementares, quando disponíveis

## ⚙️ Metodologia

### 1. Coleta de Dados
Os dados foram obtidos em formato CSV e shapefile e organizados na pasta `dados_raw/`.

### 2. Processamento e Limpeza
Os dados foram tratados com **Pandas** para remoção de colunas irrelevantes e padronização de nomes de municípios.  
As geometrias foram adicionadas com **GeoPandas**, integrando shapefiles do estado do Pará com os dados do SNIS.

### 3. Visualização Geoespacial
Foram criados mapas cloropléticos para cada serviço e um gráfico comparativo entre os municípios usando:
- `matplotlib` para mapas
- `seaborn` e `pandas` para gráficos

## 🗺️ Resultados

### 🔹 Distribuição de Água
[Insira aqui um print do mapa gerado ou gráficos]

### 🔹 Coleta de Esgoto
[Print ou gráfico]

### 🔹 Coleta de Lixo
[Print ou gráfico]

### 📊 Gráfico Comparativo
[Print do gráfico de barras]

## 📌 Conclusões

- **Belém** apresentou o melhor desempenho em todos os serviços analisados.
- **Breves** apresentou baixa cobertura de esgoto, com reflexos possíveis na saúde pública.
- **Barcarena** demonstrou menor volume per capita de coleta de resíduos.

### 🧩 Repositório
O código completo e os dados tratados estão disponíveis neste repositório.

---

## 📬 Contato
Matheus Meissner – [GitHub](https://github.com/matheus-meissner)
