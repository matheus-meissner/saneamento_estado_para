import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'figure.figsize': (10, 6)})

# Cores para os mapas
cmap_agua = 'Blues'
cmap_esgoto = 'Purples'
cmap_lixo = 'Greens'

def plot_mapa(gdf, coluna, titulo, cmap):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Mapa base
    gdf.plot(column=coluna, cmap=cmap, edgecolor='black', linewidth=0.8, legend=True, ax=ax)

    # Adiciona os nomes e os valores sobre o mapa
    for idx, row in gdf.iterrows():
        x, y = row.geometry.centroid.coords[0]
        nome_mun = row['municipio'].capitalize()
        valor = row[coluna]
        ax.text(x, y, f'{nome_mun}\n{valor:.1f}%', fontsize=10, ha='center', va='center', weight='bold', color='black')

    # Título e ajustes
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
    print('\n--- VISUALIZAÇÃO DOS DADOS DE SANEAMENTO ---\n')

    # Carregar os GeoDataFrames
    gdf_agua = gpd.read_file('dados_finais/agua.geojson')
    gdf_esgoto = gpd.read_file('dados_finais/esgoto.geojson')
    gdf_lixo = gpd.read_file('dados_finais/lixo.geojson')

    # Mapas cloropléticos
    plot_mapa(gdf_agua, 'agua_percentual', 'Distribuição de Água (%)', cmap_agua)
    plot_mapa(gdf_esgoto, 'esgoto_percentual', 'Coleta de Esgoto (%)', cmap_esgoto)
    plot_mapa(gdf_lixo, 'residuos_per_capita', 'Coleta de Resíduos Per Capita', cmap_lixo)

    # Gráfico comparativo
    plot_grafico_barra(
        [gdf_agua, gdf_esgoto, gdf_lixo],
        ['agua_percentual', 'esgoto_percentual', 'residuos_per_capita'],
        'Comparativo entre Municípios'
    )

    print('\n[✓] Visualizações geradas com sucesso!')

if __name__ == '__main__':
    main()
