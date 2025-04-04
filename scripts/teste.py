import geopandas as gpd

gdf = gpd.read_file('dados_shapefile/PA_Municipios_2022.shp')
print(gdf[gdf['NM_MUN'].str.contains('BEL', case=False)])
