# Análise Exploratória dos Dados do ENEM

Este repositório contém uma análise exploratória dos dados do Exame Nacional do Ensino Médio (ENEM). O objetivo principal é fornecer insights valiosos sobre os dados coletados durante o exame. A análise utiliza diversas ferramentas e bibliotecas em Python para manipulação de dados e visualização.

## Configuração do Ambiente

O ambiente de desenvolvimento é gerenciado através do Docker e Docker Compose. O Docker Compose é configurado no arquivo `docker-compose.yml`. Esse arquivo especifica dois serviços: MySQL e `data_loader`. O MySQL é utilizado para armazenar os dados, e o `data_loader` é um serviço Python responsável por carregar os dados no banco.

O banco de dados MySQL é inicializado com o arquivo `init.sql`, que cria o banco de dados (`test_db`) e a tabela de teste (`test_table`). A tabela contém uma variedade de campos que representam diferentes aspectos dos dados do ENEM.

## Carregamento de Dados

Os dados do ENEM são fornecidos em um arquivo CSV (`enem.csv`). Para inserir esses dados no banco de dados, utilizamos um script Python chamado `load.py`. Esse script utiliza a biblioteca Pandas para manipulação de dados e a biblioteca pymysql para interagir com o banco de dados MySQL. O script realiza a leitura do CSV e insere os dados na tabela `test_table`.

## Análise Exploratória

A análise exploratória é dividida em diversas seções, cada uma focando em aspectos específicos dos dados do ENEM.

### Seção 1: Análise de Escolas

Nesta seção, exploramos dados relacionados às escolas dos participantes, destacando médias de notas totais por escola.

### Seção 2: Análise de Alunos

Esta seção concentra-se na análise das notas totais dos alunos, identificando o aluno com a maior média.

### Seção 3: Estatísticas Gerais

Apresentamos estatísticas gerais, como a média geral das notas e o percentual de ausentes nas provas.

### Seção 4: Análise de Disciplinas

Exploramos as médias de notas por disciplina nesta seção.

### Seção 5: Análise por Sexo e Etnia

Analisamos as médias de notas totais divididas por sexo e etnia dos participantes.

### Seção 6: Análise Socioeconômica

Nesta seção, abordamos a análise de aspectos socioeconômicos, utilizando histogramas e gráficos de dispersão.

### Seção 7: Análise de Correlações e Variáveis Independentes

Investigamos correlações entre variáveis independentes e a variável dependente (nota total).

### Seção 8: Análise de Escolaridade dos Pais e Renda Familiar

Finalizamos a análise com a relação entre a escolaridade dos pais, a renda familiar e as notas totais dos participantes.

## Conclusões e Insights

- **Disparidade nas Escolas:** Identificamos variações significativas nas médias de notas totais entre as escolas, sugerindo desigualdades na qualidade da educação.

...

Esta análise visa contribuir para uma compreensão mais profunda dos dados do ENEM e fornecer insights valiosos para melhorias no sistema educacional.

*Este projeto é uma iniciativa de [Seu Nome].*

*Última Atualização: [Data]*
