import glob
import geopandas as gpd
from shapely.geometry import Polygon, Point
import pandas as pd
import os

def carregar_csv_para_geodataframe(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv)
        if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
            raise ValueError("O CSV deve conter colunas 'Latitude' e 'Longitude'.")
        
        df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
        df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
        df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

        pontos = [Point(lon, lat) for lon, lat in zip(df['Longitude'], df['Latitude'])]
        gdf = gpd.GeoDataFrame(df, geometry=pontos, crs="EPSG:4326")
        return gdf
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar o arquivo CSV {arquivo_csv}: {e}")

def criar_poligono_a_partir_dos_geometrias(gdf):
    if len(gdf) < 3:
        raise ValueError("Um polígono deve ter pelo menos 3 pontos.")
    
    poligono = Polygon(gdf.geometry.tolist())

    if not poligono.is_valid:
        raise ValueError("O polígono criado é inválido.")
    
    return poligono

def salvar_poligono_como_kml(gdf, caminho_saida, cor_preenchimento="7f000000"):
    try:
        poligono = criar_poligono_a_partir_dos_geometrias(gdf)
        gdf_poligono = gpd.GeoDataFrame(index=[0], crs=gdf.crs, geometry=[poligono])
        
        caminho_temporario = caminho_saida.replace(".kml", "_temp.kml")
        gdf_poligono.to_file(caminho_temporario, driver='KML')

        with open(caminho_temporario, 'r', encoding='utf-8') as file:
            conteudo_kml = file.read()
        
        estilo_kml = f"""
        <Style id="estiloPoligono">
            <LineStyle>
                <color>ff0000ff</color>
                <width>2</width>
            </LineStyle>
            <PolyStyle>
                <color>{cor_preenchimento}</color>
                <fill>1</fill>
                <outline>1</outline>
            </PolyStyle>
        </Style>
        """
        
        conteudo_kml = conteudo_kml.replace(
            "<Placemark>", 
            f"{estilo_kml}\n<Placemark><styleUrl>#estiloPoligono</styleUrl>"
        )
        
        with open(caminho_saida, 'w', encoding='utf-8') as file:
            file.write(conteudo_kml)

        os.remove(caminho_temporario)
        print(f"Arquivo salvo com sucesso: {caminho_saida}")
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar o arquivo KML: {e}")

def escolher_modelo():
    print("Escolha o modelo de cores para os polígonos:")
    print("1. Milho Safrinha: #B0BB58")
    print("2. Milho: #E3FF00")
    print("3. Soja: #096200")   
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == '1':
        return "7fb0bb58"
    elif escolha == '2':
        return "7fe3ff00"
    elif escolha == '3':
        return "7f096200"
    else:
        print("Escolha inválida, usando padrão Soja (#096200).")
        return "7f096200"

def processar_arquivos_csv(diretorio_csv, diretorio_saida):
    arquivos_csv = glob.glob(os.path.join(diretorio_csv, "*.csv"))
    
    if not arquivos_csv:
        print("Nenhum arquivo CSV encontrado.")
        return

    cor_preenchimento = escolher_modelo()

    for arquivo in arquivos_csv:
        try:
            print(f"Lendo o arquivo: {arquivo}")
            gdf = carregar_csv_para_geodataframe(arquivo)
            if gdf.empty:
                print(f"Nenhuma geometria encontrada no arquivo: {arquivo}")
                continue
            
            nome_arquivo_saida = os.path.splitext(os.path.basename(arquivo))[0].replace(" ", "_") + "_poligono.kml"
            caminho_saida = os.path.join(diretorio_saida, nome_arquivo_saida)

            salvar_poligono_como_kml(gdf, caminho_saida, cor_preenchimento)
        
        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")

diretorio_csv = input("Digite o caminho do diretório contendo os arquivos CSV: ").strip().strip('"')
diretorio_saida = input("Digite o caminho do diretório onde deseja salvar os arquivos KML de saída: ").strip().strip('"')

processar_arquivos_csv(diretorio_csv, diretorio_saida)

input("\nTarefa finalizada. Pressione Enter para fechar a janela...")
