import pandas as pd
import re

def formatar_csv(arquivo_csv, pasta_saida):
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

        areas = []
        area_atual = []
        tamanho_area_atual = None
        
        for linha in linhas:
            if "Área:" in linha:
                if area_atual:
                    areas.append((area_atual, tamanho_area_atual))
                    area_atual = []
                match = re.search(r'\( Área: ([\d,\.]+) ha \)', linha)
                if match:
                    tamanho_area_atual = match.group(1)
            
            if linha.strip():
                area_atual.append(linha.strip())

        if area_atual:
            areas.append((area_atual, tamanho_area_atual))

        for area, tamanho_area in areas:
            dados = []
            for item in area:
                partes = item.split(',')
                if len(partes) >= 4:
                    ponto = partes[0]
                    latitude = partes[1].strip().replace(',', '.')
                    longitude = partes[2].strip().replace(',', '.')
                    altitude = partes[3].strip().replace(',', '.') if len(partes) > 3 else '0'
                    distancia = partes[4].strip().replace(',', '.') if len(partes) > 4 else '0'
                    dados.append([ponto, latitude, longitude, altitude, distancia])

            df_area = pd.DataFrame(dados, columns=['Ponto', 'Latitude', 'Longitude', 'Altitude', 'Distancia'])
            df_area = df_area.iloc[2:].reset_index(drop=True)
            df_area.dropna(how='all', inplace=True)
            df_area.dropna(axis=1, how='all', inplace=True)
            df_area = df_area.loc[:, (df_area != '').any(axis=0)]

            nome_arquivo = input(f"Digite o nome para salvar a área (Tamanho: {tamanho_area} ha): ")
            nome_arquivo = re.sub(r'[^\w\-_\. ]', '_', nome_arquivo)

            caminho_saida = f"{pasta_saida}\\{nome_arquivo}.csv"
            df_area.to_csv(caminho_saida, sep=',', index=False, encoding='utf-8')
            print(f"Área salva como: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivo_csv}: {str(e)}")

arquivo_csv = input("Digite o caminho completo do arquivo CSV de entrada: ").strip().strip('"')
pasta_saida = input("Digite o caminho da pasta onde deseja salvar os arquivos: ").strip().strip('"')

formatar_csv(arquivo_csv, pasta_saida)

input("\nTarefa finalizada. Pressione Enter para fechar a janela...")
