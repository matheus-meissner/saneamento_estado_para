import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'figure.figsize': (10, 6)})

# Caminhos dos arquivos
CAMINHO_PA = 'dados_shapefile/PA_Municipios_2022.shp'
CAMINHO_AGUA = 'dados_finais/agua.geojson'
CAMINHO_ESGOTO = 'dados_finais/esgoto.geojson'
CAMINHO_LIXO = 'dados_finais/lixo.geojson'

# Cores
cmap_agua = 'Blues'
cmap_esgoto = 'Purples'
cmap_lixo = 'Greens'

def plot_mapa_com_estado(gdf_para, gdf_dados, coluna, titulo, cmap):
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Mapa base: estado todo
    gdf_para.plot(ax=ax, color='#eeeeee', edgecolor='black', linewidth=0.5)
    
    # Municípios com dados
    gdf_dados.plot(column=coluna, cmap=cmap, edgecolor='black', linewidth=1, legend=True, ax=ax)

    for idx, row in gdf_dados.iterrows():
        x, y = row.geometry.centroid.coords[0]
        nome = row['municipio'].capitalize()
        valor = row[coluna]
        ax.text(x, y, f"{nome}\n{valor:.1f}%", ha='center', fontsize=9, weight='bold')

    ax.set_title(titulo, fontsize=16, pad=20)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

def plot_grafico_barra(gdfs, colunas, titulo):
    df = gdfs[0][['municipio', colunas[0]]].copy()
    df[colunas[1]] = gdfs[1][colunas[1]]
    df[colunas[2]] = gdfs[2][colunas[2]]
    df.set_index('municipio', inplace=True)
    df.plot(kind='bar')
    plt.title(titulo)
    plt.ylabel('% / Volume per capita')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def main():
    print('\n--- VISUALIZAÇÃO GEOGRÁFICA DO PARÁ + MUNICÍPIOS COM DADOS ---\n')

    gdf_para = gpd.read_file(CAMINHO_PA)
    gdf_agua = gpd.read_file(CAMINHO_AGUA)
    gdf_esgoto = gpd.read_file(CAMINHO_ESGOTO)
    gdf_lixo = gpd.read_file(CAMINHO_LIXO)

    # Normaliza nomes
    gdf_para['NM_MUN'] = gdf_para['NM_MUN'].str.upper()
    for gdf in [gdf_agua, gdf_esgoto, gdf_lixo]:
        gdf['municipio'] = gdf['municipio'].str.upper()

    # Mapas com estado de fundo
    plot_mapa_com_estado(gdf_para, gdf_agua, 'agua_percentual', 'Distribuição de Água (%)', cmap_agua)
    plot_mapa_com_estado(gdf_para, gdf_esgoto, 'esgoto_percentual', 'Coleta de Esgoto (%)', cmap_esgoto)
    plot_mapa_com_estado(gdf_para, gdf_lixo, 'residuos_per_capita', 'Coleta de Resíduos Per Capita', cmap_lixo)

    # Gráfico comparativo
    plot_grafico_barra(
        [gdf_agua, gdf_esgoto, gdf_lixo],
        ['agua_percentual', 'esgoto_percentual', 'residuos_per_capita'],
        'Comparativo entre Municípios'
    )

    print('\n[✓] Visualizações completas com fundo do Pará geradas com sucesso!')

if __name__ == '__main__':
    main()
