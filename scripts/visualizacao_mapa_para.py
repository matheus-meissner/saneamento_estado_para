import geopandas as gpd
import matplotlib.pyplot as plt

# Caminhos dos arquivos
CAMINHO_PA = 'dados_shapefile/PA_Municipios_2022.shp'
CAMINHO_MUNICIPIOS = 'dados_finais/agua.geojson'

# Carrega o shapefile completo do Pará
gdf_para = gpd.read_file(CAMINHO_PA)

# Carrega os dados dos municípios com valores (ex: água)
gdf_municipios = gpd.read_file(CAMINHO_MUNICIPIOS)

# Normaliza os nomes
gdf_para['NM_MUN'] = gdf_para['NM_MUN'].str.upper()
gdf_municipios['municipio'] = gdf_municipios['municipio'].str.upper()

# Cria o mapa
fig, ax = plt.subplots(figsize=(12, 10))

# Mapa base: todos os municípios do Pará em cinza claro
gdf_para.plot(ax=ax, color='#eeeeee', edgecolor='black', linewidth=0.5)

# Destaque: nossos 3 municípios, com cor baseada no percentual
gdf_municipios.plot(column='agua_percentual', cmap='Blues', edgecolor='black', linewidth=1, legend=True, ax=ax)

# Adiciona texto com nomes e valores
for idx, row in gdf_municipios.iterrows():
    x, y = row.geometry.centroid.coords[0]
    nome = row['municipio'].capitalize()
    valor = row['agua_percentual']
    ax.text(x, y, f"{nome}\n{valor:.1f}%", ha='center', fontsize=9, weight='bold')

# Ajustes
ax.set_title('Distribuição de Água (%) nos Municípios do Pará', fontsize=16, pad=20)
ax.axis('off')
plt.tight_layout()
plt.show()
