# Análise Exploratória dos Dados do ENEM
# Link do Dashboard no Streamlit: https://testesx-2gaz575fcmbbwhhdvqqtxo.streamlit.app/


Neste repositório, apresento uma análise exploratória dos dados do Exame Nacional do Ensino Médio (ENEM). Meu principal objetivo é proporcionar insights valiosos sobre os dados coletados durante o exame. Utilizei diversas ferramentas e bibliotecas em Python para manipulação de dados e visualização.

## Configuração do Ambiente

O ambiente de desenvolvimento é gerenciado por meio do Docker e Docker Compose. Configurei o Docker Compose no arquivo `docker-compose.yml`. Esse arquivo especifica dois serviços: MySQL e `data_loader`. O MySQL é utilizado para armazenar os dados, e o `data_loader` é um serviço Python responsável por carregar os dados no banco.

Inicializo o banco de dados MySQL com o arquivo `init.sql`, que cria o banco de dados (`test_db`) e a tabela de teste (`test_table`). A tabela contém uma variedade de campos que representam diferentes aspectos dos dados do ENEM.

## Carregamento de Dados

Os dados do ENEM estão no arquivo CSV (`enem.csv`). Para inserir esses dados no banco de dados, utilizei um script Python chamado `load.py`. Este script usa a biblioteca Pandas para manipulação de dados e a biblioteca pymysql para interagir com o banco de dados MySQL. O script lê o CSV e insere os dados na tabela `test_table`.

## Análise Exploratória

Dividi a análise exploratória em diversas seções, cada uma focando em aspectos específicos dos dados do ENEM.

### Seção 1: Análise de Escolas

Explorei dados relacionados às escolas dos participantes, destacando médias de notas totais por escola.

### Seção 2: Análise de Alunos

Concentrei-me na análise das notas totais dos alunos, identificando o aluno com a maior média.

### Seção 3: Estatísticas Gerais

Apresentei estatísticas gerais, como a média geral das notas e o percentual de ausentes nas provas.

### Seção 4: Análise de Disciplinas

Explorei as médias de notas por disciplina nesta seção.

### Seção 5: Análise por Sexo e Etnia

Analisei as médias de notas totais divididas por sexo e etnia dos participantes.

### Seção 6: Análise Socioeconômica

Abordei a análise de aspectos socioeconômicos nesta seção, utilizando histogramas e gráficos de dispersão.

### Seção 7: Análise de Correlações e Variáveis Independentes

Investiguei correlações entre variáveis independentes e a variável dependente (nota total).

### Seção 8: Análise de Escolaridade dos Pais e Renda Familiar

Finalizei a análise com a relação entre a escolaridade dos pais, a renda familiar e as notas totais dos participantes.

## Conclusões e Insights

- **Disparidade nas Escolas:** Identifiquei variações significativas nas médias de notas totais entre as escolas, sugerindo desigualdades na qualidade da educação.
- **Desempenho do Aluno Destacado:** Identifiquei o aluno com a maior média de notas totais, destacando seu desempenho excepcional.
- **Estatísticas Gerais:** Foram apresentadas estatísticas gerais, incluindo a média geral das notas e o percentual de ausentes nas provas.
- **Análise de Disciplinas:** Explorei as médias de notas por disciplina, identificando áreas de destaque e oportunidades de melhoria.
- **Diferenças por Sexo e Etnia:** Analisei as médias de notas totais, destacando diferenças entre grupos de diferentes sexos e etnias.
- **Aspectos Socioeconômicos:** Abordei aspectos socioeconômicos, utilizando histogramas e gráficos de dispersão para insights adicionais.
- **Correlações entre Variáveis:** Investiguei correlações entre variáveis independentes e a variável dependente (nota total), identificando relações significativas.
- **Influência da Escolaridade dos Pais:** Analisei como a escolaridade dos pais está relacionada às notas totais dos participantes.
- **Impacto da Renda Familiar:** Explorei a influência da renda familiar nas notas totais dos participantes.
- **Contribuição para a Educação:** Esta análise visa contribuir para uma compreensão mais profunda dos dados do ENEM e fornecer insights valiosos para melhorias no sistema educacional.

