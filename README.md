## 🎥 Movie & TV Show Analysis Project
Análise de filmes e séries utilizando técnicas de wrangling de dados.

## 📖 Sobre o Projeto
Este projeto é parte do curso de Wrangling do MBA em Data Science and Analytics. O objetivo principal é explorar, limpar e unificar dois datasets diferentes (um de filmes e outro de séries de TV) para realizar análises avançadas e gerar insights relevantes.

## 🎯 Objetivo
  - Unificar datasets de filmes e séries em uma estrutura comum.
  - Corrigir e preencher valores ausentes nas colunas relevantes.
  - Classificar e identificar os melhores filmes e séries com base em avaliações no IMDb e Rotten Tomatoes.
  - Visualizar graficamente os rankings dos melhores títulos.

## 📂 Estrutura do Projeto
  1. Leitura dos Datasets:
       - Carregamos os arquivos ```MoviesOnStreamingPlatforms_updated.csv``` e ```tv_shows.csv```.
  2. Limpeza e Transformação:
       - Padronização de colunas e estrutura dos datasets.
       - Extração e conversão das notas de avaliações em formatos numéricos.
       - Preenchimento de valores ausentes com zero (0).
       - Unificação dos Dados:
       - Unimos os dois datasets em um único dataframe usando o método concat.
  3. Classificação:
       - Classificamos os títulos em categorias (minors e majors) com base no percentil 95 das avaliações.
  4. Visualização:
       - Geramos gráficos de barras para exibir os 10 melhores filmes e as 10 melhores séries de TV com base nas avaliações.
    
## 🔍 Técnicas Utilizadas
  - Manipulação de Dados:
      - Pandas para limpeza, preenchimento e unificação de datasets.
      - Transformação de colunas com valores textuais para numéricos.
      - Uso de ```qcut``` para categorizar os dados com base em percentis.
  - Visualização de Dados:
      - Matplotlib para criar gráficos de barras ilustrando os rankings.
  - Wrangling Avançado:
      - Preenchimento de valores nulos.
      - Renomeação de colunas e reestruturação de dados.

## 🚀 Como Executar o Projeto
  1. Certifique-se de ter o Python instalado (versão 3.x ou superior).
  2. Instale as bibliotecas necessárias:
  ```
  pip install pandas matplotlib
  ```
  3. Baixe os datasets:
    - ```MoviesOnStreamingPlatforms_updated.csv```
    - ```tv_shows.csv```
  4. Salve o código em um arquivo Python, por exemplo, movie_tv_analysis.py.
  5. Execute o script no terminal:
    ```
    python movie_tv_analysis.py
    ```
## 📊 Exemplos de Resultados
Top 10 Séries de TV  
![10BestTVShows](https://github.com/user-attachments/assets/e51d6d83-f6d2-48cf-8708-328ed05c4e60)

Top 10 Filmes  
![10BestMovies](https://github.com/user-attachments/assets/2ccc32be-8bbd-4413-beff-10cf8097dd6d)

## 🛠️ Próximas Melhorias
  - Adicionar suporte para mais plataformas de streaming.
  - Explorar relações entre gêneros, anos de lançamento e avaliações.
  - Incorporar outros métodos de visualização, como heatmaps.
###






