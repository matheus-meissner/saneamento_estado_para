import pandas as pd
import geopandas as gpd
from unidecode import unidecode

# Municípios de interesse
MUNICIPIOS = ['BARCARENA', 'BELÉM', 'BREVES']

# Caminhos dos arquivos
CAMINHO_SHAPEFILE = 'dados_shapefile/PA_Municipios_2022.shp'
CAMINHO_SALVAR = 'dados_finais/'

# Função genérica para ler e filtrar dados do SNIS
def ler_dados_snis(caminho_arquivo, coluna_valor, novo_nome_coluna):
    df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')
    df = df[df['Municipio'].str.upper().isin(MUNICIPIOS)]
    df = df[['Municipio', coluna_valor]].rename(columns={
        'Municipio': 'municipio',
        coluna_valor: novo_nome_coluna
    })
    df['municipio'] = df['municipio'].str.upper()
    return df

# Função para integrar com shapefile
def integrar_com_geometria(df_valores, nome_coluna_valor, nome_arquivo_saida):
    gdf = gpd.read_file(CAMINHO_SHAPEFILE)
    gdf = gdf[gdf['NM_MUN'].str.upper().isin(MUNICIPIOS)]
    gdf['NM_MUN'] = gdf['NM_MUN'].str.upper()

    gdf_merged = gdf.merge(df_valores, left_on='NM_MUN', right_on='municipio')
    caminho_saida = f'{CAMINHO_SALVAR}{nome_arquivo_saida}.geojson'
    gdf_merged.to_file(caminho_saida, driver='GeoJSON')
    print(f'[✓] Arquivo salvo: {caminho_saida}')

# Processamento de cada tipo de serviço
def main():
    print('\n--- PROCESSAMENTO DE DADOS DE SANEAMENTO ---\n')

    df_agua = ler_dados_snis('dados_processados/snis_agua_2022.csv', 'IN058', 'agua_percentual')
    integrar_com_geometria(df_agua, 'agua_percentual', 'agua')

    df_esgoto = ler_dados_snis('dados_processados/snis_esgoto_2022.csv', 'IN061', 'esgoto_percentual')
    integrar_com_geometria(df_esgoto, 'esgoto_percentual', 'esgoto')

    df_lixo = ler_dados_snis('dados_processados/snis_lixo_2022.csv', 'IN072', 'residuos_per_capita')
    integrar_com_geometria(df_lixo, 'residuos_per_capita', 'lixo')

    print('\n[✓] Todos os arquivos processados com sucesso!')

if __name__ == '__main__':
    main()
