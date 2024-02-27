# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações para o Seaborn
sns.set_theme()

# Lê o CSV
df = pd.read_csv('analise1.csv')

# Converte a coluna Q005 para string
df['Q005'] = df['Q005'].astype(str)

# Cria uma nova coluna NU_NOTA_TOTAL
df['NU_NOTA_TOTAL'] = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']].sum(axis=1)
df['CODIGO_ESCOLA'] = df['CO_MUNICIPIO_ESC'].astype(str) + '_' + df['NO_MUNICIPIO_ESC']

# Título principal do aplicativo
st.title('Análise Exploratória dos Dados do ENEM')

# Seção 1: Análise de Escolas
st.header('Análise de Escolas')

media_por_escola = df.groupby('CODIGO_ESCOLA')['NU_NOTA_TOTAL'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='CODIGO_ESCOLA', y='NU_NOTA_TOTAL', data=media_por_escola)
plt.title('Média de Nota Total por Escola')
plt.xlabel('Código da Escola')
plt.ylabel('Média de Nota Total')
st.pyplot()

# Seção 2: Análise de Alunos
st.header('Análise de Alunos')

media_por_aluno = df.groupby('NU_INSCRICAO')['NU_NOTA_TOTAL'].mean().reset_index()
aluno_maior_media = media_por_aluno.loc[media_por_aluno['NU_NOTA_TOTAL'].idxmax()]
st.write(f"Aluno com maior média: Inscrição {aluno_maior_media['NU_INSCRICAO']}, Média: {aluno_maior_media['NU_NOTA_TOTAL']:.2f}")

plt.figure(figsize=(10, 6))
sns.histplot(data=media_por_aluno, x='NU_NOTA_TOTAL', kde=True)
plt.title('Distribuição da Média de Nota Total por Aluno')
plt.xlabel('Média de Nota Total')
plt.ylabel('Contagem')
st.pyplot()

# Seção 3: Estatísticas Gerais
st.header('Estatísticas Gerais')

media_geral = df['NU_NOTA_TOTAL'].mean().round(2)
st.write(f"Média Geral: {media_geral:.2f}")

percentual_ausentes = (df['TP_PRESENCA_CN'] + df['TP_PRESENCA_CH'] + df['TP_PRESENCA_LC'] + df['TP_PRESENCA_MT']).eq(0).mean() * 100
plt.figure(figsize=(8, 8))
plt.pie([100 - percentual_ausentes, percentual_ausentes], labels=['Presentes', 'Ausentes'], autopct='%1.1f%%')
plt.title('Percentual de Ausentes nas Provas')
st.pyplot()

total_inscritos = len(df)
st.write(f"Total de Inscritos: {total_inscritos}")
plt.figure(figsize=(8, 6))
plt.bar(x=['Total de Inscritos'], height=[total_inscritos])
plt.title('Total de Inscritos')
plt.ylabel('Número de Inscritos')
st.pyplot()

# Seção 4: Análise de Disciplinas
st.header('Análise de Disciplinas')

media_disciplinas = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']].mean().round(2).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='index', y=0, data=media_disciplinas, hue='index')
plt.title('Média de Notas por Disciplina')
plt.xlabel('Disciplina')
plt.ylabel('Média de Nota')
st.pyplot()


# Seção 5: Análise por Sexo e Etnia
st.header('Análise por Sexo e Etnia')

media_por_sexo = df.groupby('TP_SEXO')['NU_NOTA_TOTAL'].mean().round(2).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='TP_SEXO', y='NU_NOTA_TOTAL', data=media_por_sexo)
plt.title('Média de Nota Total por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Média de Nota Total')
st.pyplot()

media_por_etnia = df.groupby('TP_COR_RACA')['NU_NOTA_TOTAL'].mean().round(2).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='TP_COR_RACA', y='NU_NOTA_TOTAL', data=media_por_etnia)
plt.title('Média de Nota Total por Etnia')
plt.xlabel('Etnia')
plt.ylabel('Média de Nota Total')
st.pyplot()

# Seção 6: Análise Socioeconômica
st.header('Análise Socioeconômica')

plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='NU_NOTA_CN', kde=True)
plt.title('Distribuição das Notas de Ciências da Natureza')
st.pyplot()

plt.figure(figsize=(10, 6))
sns.boxplot(y='NU_NOTA_LC', data=df)
plt.title('Box Plot das Notas de Linguagens e Códigos')
st.pyplot()

plt.figure(figsize=(12, 8))
sns.scatterplot(x='NU_NOTA_CH', y='NU_NOTA_MT', data=df)
plt.title('Dispersão entre Notas de Ciências Humanas e Matemática')
st.pyplot()

plt.figure(figsize=(10, 6))
sns.boxplot(x='TP_SEXO', y='NU_NOTA_REDACAO', data=df)
plt.title('Distribuição das Notas de Redação por Sexo')
st.pyplot()

plt.figure(figsize=(12, 6))
sns.boxplot(x='TP_COR_RACA', y='NU_NOTA_REDACAO', data=df)
plt.title('Distribuição das Notas de Redação por Cor/Raça')
st.pyplot()

# ... (código anterior)

# Seção 7: Análise de Correlações e Variáveis Independentes
st.header('Análise de Correlações e Variáveis Independentes')

variaveis_independentes = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_TOTAL']
correlacoes = df[variaveis_independentes].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação entre Variáveis Independentes e a Variável Dependente')
st.pyplot()

# Seção 8: Análise de Escolaridade dos Pais e Renda Familiar
st.header('Análise de Escolaridade dos Pais e Renda Familiar')

plt.figure(figsize=(14, 6))
sns.barplot(x='Q001', y='NU_NOTA_TOTAL', hue='Q002', data=df,
            order=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
plt.title('Média de Notas Totais por Escolaridade dos Pais')
plt.xlabel('Escolaridade do Pai')
plt.ylabel('Nota Total')
st.pyplot()

plt.figure(figsize=(16, 6))
sns.barplot(x='Q006', y='NU_NOTA_TOTAL', hue='Q006', data=df,
            order=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'])
plt.title('Média de Notas Totais por Renda Familiar')
plt.xlabel('Renda Familiar')
plt.ylabel('Nota Total')
st.pyplot()
