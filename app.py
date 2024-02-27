# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px
import streamlit as st

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
fig_escola = px.bar(media_por_escola, x='CODIGO_ESCOLA', y='NU_NOTA_TOTAL',
                    title='Média de Nota Total por Escola',
                    labels={'CODIGO_ESCOLA': 'Código da Escola', 'NU_NOTA_TOTAL': 'Média de Nota Total'})
st.plotly_chart(fig_escola)

# Seção 2: Análise de Alunos
st.header('Análise de Alunos')

media_por_aluno = df.groupby('NU_INSCRICAO')['NU_NOTA_TOTAL'].mean().reset_index()
aluno_maior_media = media_por_aluno.loc[media_por_aluno['NU_NOTA_TOTAL'].idxmax()]
st.write(f"Aluno com maior média: Inscrição {aluno_maior_media['NU_INSCRICAO']}, Média: {aluno_maior_media['NU_NOTA_TOTAL']:.2f}")
fig_aluno = px.histogram(media_por_aluno, x='NU_NOTA_TOTAL',
                         title='Distribuição da Média de Nota Total por Aluno',
                         labels={'NU_NOTA_TOTAL': 'Média de Nota Total'})
st.plotly_chart(fig_aluno)

# Seção 3: Estatísticas Gerais
st.header('Estatísticas Gerais')

media_geral = df['NU_NOTA_TOTAL'].mean().round(2)
st.write(f"Média Geral: {media_geral:.2f}")

percentual_ausentes = (df['TP_PRESENCA_CN'] + df['TP_PRESENCA_CH'] + df['TP_PRESENCA_LC'] + df['TP_PRESENCA_MT']).eq(0).mean() * 100
fig_pie_ausentes = px.pie(names=['Presentes', 'Ausentes'], values=[100 - percentual_ausentes, percentual_ausentes],
                          title='Percentual de Ausentes nas Provas')
st.plotly_chart(fig_pie_ausentes)

total_inscritos = len(df)
st.write(f"Total de Inscritos: {total_inscritos}")
fig_total_inscritos = px.bar(x=['Total de Inscritos'], y=[total_inscritos],
                             title='Total de Inscritos',
                             labels={'y': 'Número de Inscritos'})
st.plotly_chart(fig_total_inscritos)

# Seção 4: Análise de Disciplinas
st.header('Análise de Disciplinas')

media_disciplinas = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']].mean().round(2).reset_index()
fig_disciplinas = px.bar(media_disciplinas, x='index', y=0,
                         title='Média de Notas por Disciplina',
                         labels={'index': 'Disciplina', 0: 'Média de Nota'},
                         color='index')
st.plotly_chart(fig_disciplinas)

# Seção 5: Análise por Sexo e Etnia
st.header('Análise por Sexo e Etnia')

media_por_sexo = df.groupby('TP_SEXO')['NU_NOTA_TOTAL'].mean().round(2).reset_index()
fig_sexo = px.bar(media_por_sexo, x='TP_SEXO', y='NU_NOTA_TOTAL',
                  title='Média de Nota Total por Sexo',
                  labels={'TP_SEXO': 'Sexo', 'NU_NOTA_TOTAL': 'Média de Nota Total'})
st.plotly_chart(fig_sexo)

media_por_etnia = df.groupby('TP_COR_RACA')['NU_NOTA_TOTAL'].mean().round(2).reset_index()
fig_etnia = px.bar(media_por_etnia, x='TP_COR_RACA', y='NU_NOTA_TOTAL',
                   title='Média de Nota Total por Etnia',
                   labels={'TP_COR_RACA': 'Etnia', 'NU_NOTA_TOTAL': 'Média de Nota Total'})
st.plotly_chart(fig_etnia)

# Seção 6: Análise Socioeconômica
st.header('Análise Socioeconômica')

fig_cn = px.histogram(df, x='NU_NOTA_CN', title='Distribuição das Notas de Ciências da Natureza')
st.plotly_chart(fig_cn)

fig_lc = px.box(df, y='NU_NOTA_LC', title='Box Plot das Notas de Linguagens e Códigos')
st.plotly_chart(fig_lc)

fig_ch_mt = px.scatter(df, x='NU_NOTA_CH', y='NU_NOTA_MT', title='Dispersão entre Notas de Ciências Humanas e Matemática')
st.plotly_chart(fig_ch_mt)

fig_redacao_sexo = px.box(df, x='TP_SEXO', y='NU_NOTA_REDACAO', title='Distribuição das Notas de Redação por Sexo',
                           labels={'TP_SEXO': 'Sexo', 'NU_NOTA_REDACAO': 'Nota de Redação'})
st.plotly_chart(fig_redacao_sexo)

fig_redacao_cor_raca = px.box(df, x='TP_COR_RACA', y='NU_NOTA_REDACAO', title='Distribuição das Notas de Redação por Cor/Raça',
                              labels={'TP_COR_RACA': 'Cor/Raça', 'NU_NOTA_REDACAO': 'Nota de Redação'})
st.plotly_chart(fig_redacao_cor_raca)

# Seção 7: Análise de Correlações e Variáveis Independentes
st.header('Análise de Correlações e Variáveis Independentes')

variaveis_independentes = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_TOTAL']
correlacoes = df[variaveis_independentes].corr()

fig_correlacoes = px.imshow(correlacoes,
                            labels=dict(color='Correlação'),
                            x=variaveis_independentes,
                            y=variaveis_independentes,
                            title='Matriz de Correlação entre Variáveis Independentes e a Variável Dependente')
st.plotly_chart(fig_correlacoes)

# Seção 8: Análise de Escolaridade dos Pais e Renda Familiar
st.header('Análise de Escolaridade dos Pais e Renda Familiar')

fig_escolaridade_pais = px.bar(df, x='Q001', y='NU_NOTA_TOTAL', color='Q002',
                                title='Média de Notas Totais por Escolaridade dos Pais',
                                labels={'Q001': 'Escolaridade do Pai', 'NU_NOTA_TOTAL': 'Nota Total'},
                                category_orders={'Q001': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                                                 'Q002': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']})
st.plotly_chart(fig_escolaridade_pais)

fig_renda_familiar = px.bar(df, x='Q006', y='NU_NOTA_TOTAL', color='Q006',
                             title='Média de Notas Totais por Renda Familiar',
                             labels={'Q006': 'Renda Familiar', 'NU_NOTA_TOTAL': 'Nota Total'},
                             category_orders={'Q006': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']})
st.plotly_chart(fig_renda_familiar)