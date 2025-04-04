
# 🛰️ Análise Geoespacial do Saneamento Básico – Barcarena, Belém e Breves (PA)

Este projeto utiliza **Python**, **GeoPandas** e dados públicos para analisar e visualizar o acesso ao saneamento básico nos municípios de **Barcarena**, **Belém** e **Breves**, no estado do Pará. A análise cobre:  
- 💧 Abastecimento de água  
- 🚽 Coleta de esgoto  
- 🗑️ Coleta de resíduos sólidos

---

## 📁 Estrutura esperada de diretórios

```bash
.
├── dados_shapefile/        # Shapefile do estado do Pará (IBGE)
├── dados_processados/      # Intermediários (opcional)
├── dados_finais/           # GeoJSONs prontos para visualização
├── scripts/                # Scripts Python
│   ├── processamento_saneamento.py
│   ├── visualizacao_saneamento.py
│   └── visualizacao_mapa_para.py
```

---

## ⚙️ Requisitos

Instale os pacotes necessários com:

```bash
pip install pandas geopandas matplotlib seaborn unidecode
```

---

## 🚀 Como rodar o projeto

### 1️⃣ Prepare os dados

- Baixe os CSVs do SNIS:
  - `snis_agua_2022.csv`
  - `snis_esgoto_2022.csv`
  - `snis_lixo_2022.csv`

  ➕ Certifique-se de colocá-los dentro da pasta `dados_processados/`.

- Baixe o shapefile dos municípios do Pará (IBGE):
  - Coloque todos os arquivos (`.shp`, `.shx`, `.dbf`, etc) na pasta `dados_shapefile/`.

  > Você pode obter o shapefile em:  
  > https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/PA/PA_Municipios_2022.zip

---

### 2️⃣ Execute o processamento

```bash
python scripts/processamento_saneamento.py
```

🔧 Isso vai:
- Ler os dados do SNIS
- Cruzar com o shapefile
- Gerar arquivos `.geojson` para água, esgoto e lixo em `dados_finais/`

---

### 3️⃣ Visualize os resultados

#### 🌎 Visualizações com foco nos 2 municípios:

```bash
python scripts/visualizacao_saneamento.py
```

✅ Isso gerará:
- Mapas cloropléticos (água, esgoto, lixo)
- Gráfico de barras comparando os municípios

#### 🗺️ Mapa completo do estado com destaque dos municípios:

```bash
python scripts/visualizacao_mapa_para.py
```

✅ Isso exibirá:
- Mapa do Pará inteiro em cinza
- Destaque em azul dos 2 municípios com dados de água

---

## 📌 Observação

Este projeto utiliza `unidecode` para evitar problemas com acentuação em nomes de municípios ao fazer merges entre CSVs e shapefiles.

---

## 👨‍💻 Autor

**Matheus Meissner**  
🔗 [GitHub](https://github.com/matheus-meissner)  
🎓 Análise e Desenvolvimento de Sistemas | Produção Fonográfica
