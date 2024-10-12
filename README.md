# -Coordinates-to-KML
Uma simples automação cujo o objetivo é transformar arquivos de coordenadas (em .csv) em arquivos de mapeamentos (.kml) configurando-os para utilização de controles relacionados a agricultura.

Antes de tudo, será necessário instalar o Python (https://www.python.org/downloads/) e após também será necessário instalar as dependências da ferramenta com seguinte comando no terminal. 

```bash
pip install -r requirements.txt
```

### 1º passo

Acessar a pasta da operação e criar uma pasta para colocarmos os dados geográficos.

Sugiro que o nome da pasta seja "GEOGRÁFICOS" e dentro dessa pasta deverão ser criadas mais três pastas que serão "CSV", "KML" e "SHAPE FILE", conforme a imagem abaixo

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/b9537ad5-170f-4e10-bb24-7a9638c02a4f/image.png)

### 2º passo

Fazer o download da coordenas, para isso a proposta já deve ter sido enviada para o banco, as coordenadas ficam disponível no terras, após localizar a proposta desejada,  segue abaixo como fazer o download das coordenadas que é em: PROJETO > CROQUI > Baixar…

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/cc9f4590-2319-447a-95cf-f0eac7023207/image.png)

O ideal é que o nome do arquivo fique “coordenadas.csv” e dentro da pasta “GEOGRÁFICOS”

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/f280aedd-3e14-405c-92f0-5ccff01b6980/image.png)

### 3º passo

Executar a ferramenta “Formatar CSV.py”

### 4º passo

Entrar na pasta “CSV” e abrir os arquivos no excel, a única alteração que deverá ser feita é a exclusão da última linha que possui 4 virgulas “,,,,” e após isso salvar e fechar os documentos

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/9041a4fc-9441-452e-8c4a-726696d800b6/40bef75a-642a-43d7-a5a2-d06635c16f21.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/e066f52d-2d8d-479c-a8c1-8735f2e0433a/a0c92514-313c-437a-ab70-96b5f64c1625.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/23e26de9-79b0-456c-8503-98902e9f3b15/image.png)

### 5º passo

Executar a ferramenta “Poligonos.py”

### 6º passo

Fazer o Fazer o Download do Shapefile e renomear, para isso basta acessar o site do SiCar, buscar a área desejada através do número do recibo do CAR e fazer o download do shapefile em zip. (lembre-se de salvar o arquivo com o nome correto da fazendas para evitar confusões quando a proposta tiver muitas áreas) após isso basta extrair a pasta.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/c76085b1-9dec-4404-aeb2-86716025dc52/image.png)

### 7º passo

Após isso vamos renomear todos os arquivos que estão presentes dentro da pasta do shapefile, para isso basta selecionar todos apertando a teclado “crtl + a” e depois clicar no botão de renomear, feito isso escreva o nome da fazenda que corresponda a esse shapefile e o nome será aplicado em todos os arquivos

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/a2e62906-325d-4fe0-a3dc-665a38147635/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/5068a7b4-4a17-48ed-9f61-63acb7c5f7d5/e68916af-f247-4c74-87d7-1a2472cbc249.png)

### 7º passo

Feito isso você terá dentro da pasta “KML” o desenho do croqui em formato .KML que poderá ser aberto no programa “Google Earth Pro” que é gratuito e também na versão web do Google Earth, com esse arquivos você pode carregar vários arquivos de uma vez para ter certeza de que não está havendo sobreposição de Gleba e na pasta “SHAPEFILE” você poderá encontrar o desenho inteiro da área das fazendas, esse arquivos também podem ser carregados no Google Earth

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9af10e63-caa6-4c20-85ba-cb70c238172a/d59a03d3-afa7-4fea-abeb-4a7082bfb76d/image.png)

Esse é o resultado final com o KML e o Shape da fazenda carregados ao mesmo tempo, se houver mais áreas desenhas nessa Fazenda nos podemos importar quantos arquivos KML forem necessários.
