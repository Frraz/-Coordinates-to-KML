Ferramenta de Processamento de Dados Geográficos
Este repositório contém uma ferramenta para processamento de dados geográficos em formato CSV, KML e Shapefile. O objetivo é converter coordenadas geográficas em arquivos KML para visualização no Google Earth.

Pré-requisitos
Antes de tudo, será necessário instalar o Python. Após a instalação do Python, você também precisará instalar as dependências da ferramenta. Para isso, execute o seguinte comando no terminal:

bash
Copiar código
pip install -r requirements.txt
Passos para utilização
1. Preparação do Ambiente
Crie uma pasta para armazenar os dados geográficos, sugerimos o nome "GEOGRÁFICOS". Dentro dessa pasta, crie as seguintes subpastas:

CSV
KML
SHAPE FILE
A estrutura ficará como na imagem abaixo:



2. Download das Coordenadas
As coordenadas deverão ser baixadas do sistema Terras após a proposta ter sido enviada ao banco. Para isso, vá até o projeto desejado, clique em:

PROJETO > CROQUI > Baixar...

Salve o arquivo como coordenadas.csv dentro da pasta GEOGRÁFICOS/CSV.



3. Execução da Ferramenta
Execute o script Formatar CSV.py para processar o arquivo de coordenadas.

4. Ajustes no CSV
Após a execução, entre na pasta CSV e abra os arquivos no Excel. A única alteração necessária é excluir a última linha que contém apenas vírgulas (,,,,). Depois, salve e feche o arquivo.



5. Geração de Polígonos
Execute o script Poligonos.py para gerar os arquivos KML com os polígonos das áreas.

6. Download e Renomeação do Shapefile
Acesse o site do SiCar, localize a área pelo número do recibo do CAR, e faça o download do Shapefile correspondente. Salve o arquivo na pasta GEOGRÁFICOS/SHAPE FILE com o nome correto da fazenda.



7. Renomear Arquivos do Shapefile
Renomeie todos os arquivos do Shapefile, garantindo que todos tenham o nome correto da fazenda. Isso pode ser feito selecionando todos os arquivos e utilizando a função de renomear do sistema.



8. Visualização dos Arquivos no Google Earth
Após a geração dos arquivos, você poderá visualizar os polígonos no Google Earth Pro (ou na versão web). O arquivo KML gerado pode ser carregado para verificar se não há sobreposição entre as áreas.

